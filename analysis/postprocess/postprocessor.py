import glob
import json
from analysis.utils import paths
from analysis.configs import load_config
from analysis.postprocess.utils import open_output, print_header, accumulate


class Postprocessor:

    def __init__(
        self,
        processor: str,
        tagger: str,
        flavor: str,
        wp: str,
        year: str,
        output_dir: str,
    ):
        self.processor = processor
        self.year = year

        if output_dir:
            self.output_dir = output_dir
        else:
            self.output_dir = paths.processor_path(
                processor=processor,
                tagger=tagger,
                flavor=flavor,
                wp=wp,
                year=year,
            )

    def group_outputs(self) -> tuple:
        """
        group output .pkl files and group histograms and sum of weights by sample
        """
        extension = ".pkl"
        output_files = glob.glob(f"{self.output_dir}/*{extension}", recursive=True)

        n_output_files = len(output_files)
        assert n_output_files != 0, "No output files found"

        print_header("grouping outputs by sample")
        print(f"reading outputs from {self.output_dir}")
        
        # group output file paths by sample name
        grouped_outputs = {}
        for output_file in output_files:
            sample_name = output_file.split("/")[-1].split(extension)[0]
            if sample_name.rsplit("_")[-1].isdigit():
                sample_name = "_".join(sample_name.rsplit("_")[:-1])
            if sample_name in grouped_outputs:
                grouped_outputs[sample_name].append(output_file)
            else:
                grouped_outputs[sample_name] = [output_file]

        print(f"{n_output_files} output files were found:")
        n_grouped_outputs = {}
        for sample in grouped_outputs:
            dataset_config = load_config(
                config_type="dataset", config_name=sample, year=self.year
            )
            dataset_nfiles = dataset_config.partitions
            output_nfiles = len(grouped_outputs[sample])
            print(f"{sample}: {output_nfiles} (missing files: {dataset_nfiles - output_nfiles})")
        
        
        # open output dictionaries partitions ({<sample>_<i>: {"histograms": ..., "sumw": ...}})
        # and group histograms and sumw by <sample>
        grouped_histograms = {}
        accumulated_histograms = {}
        grouped_sumw = {}
        accumulated_sumw = {}
        for sample in grouped_outputs:
            grouped_histograms[sample] = []
            grouped_sumw[sample] = []
            for fname in grouped_outputs[sample]:
                output = open_output(fname)
                if output:
                    output_dataset_key = list(output.keys())[0]
                    grouped_sumw[sample].append(float(output[output_dataset_key]["sumw"]))
                    grouped_histograms[sample].append(
                        output[output_dataset_key]["histograms"]
                    )
            # accumulate sample histograms and sumw
            accumulated_sumw[sample] = accumulate(grouped_sumw[sample])
            accumulated_histograms[sample] = accumulate(
                grouped_histograms[sample]
            )
        self.accumulated_histograms = accumulated_histograms
        self.accumulated_sumw = accumulated_sumw

        
    def set_weights(self):
        """
        compute luminosity and set xsec-lumi weights

        set attributes:
            weights (dict)
            lumi (float)
        """
        # check which eras are present in the output histograms
        self.eras = [
            d.split("Muon")[-1]
            for d in self.accumulated_sumw.keys()
            if d.startswith("Muon")
        ]
        # compute luminosity
        lumis = {
            # https://docs.google.com/presentation/d/1F4ndU7DBcyvrEEyLfYqb29NGkBPs20EAnBxe_l7AEII/edit#slide=id.g289f499aa6b_2_52
            "2022": {"C": 5010.4, "D": 2970.0},
            "2022EE": {"E": 5807.0, "F": 17781.9, "G": 3082.8},
            # https://docs.google.com/presentation/d/1TjPem5jX0fzqvTGl271_nQFoVBabsrdrO0i8Qo1uD5E/edit#slide=id.g289f499aa6b_2_58
            "2023": {"C": 17794.0, "D": 9451.0},
        }
        self.lumi = 0
        for era in self.eras:
            self.lumi += lumis[self.year][era]
        
        # set lumi-xsec weights
        self.weights = {}
        self.xsecs = {}
        for sample, sumw in self.accumulated_sumw.items():
            dataset_config = load_config(
                config_type="dataset", config_name=sample, year=self.year
            )
            self.weights[sample] = 1
            self.xsecs[sample] = dataset_config.xsec
            if dataset_config.era == "MC":
                self.weights[sample] = self.lumi * dataset_config.xsec / sumw

        
    def scale_histograms(self):
        """scale histograms to lumi-xsec"""
        self.set_weights()
        print_header(f"scaling histograms to lumi-xsec weights")
        print(f"luminosity for eras {self.eras}: {self.lumi * 1e-3} fb^(-1)")
        print(f"sumw of weights: {json.dumps(self.accumulated_sumw, indent=2)}")
        print(f"cross sections: {json.dumps(self.xsecs, indent=2)}")
        print(f"lumi-xsec weights: {json.dumps(self.weights, indent=2)}")
        self.scaled_histograms = {}
        for sample, features in self.accumulated_histograms.items():
            self.scaled_histograms[sample] = {}
            for feature in features:
                self.scaled_histograms[sample][feature] = (
                    self.accumulated_histograms[sample][feature] * self.weights[sample]
                )

    def process_histograms(self) -> dict:
        """group scaled histograms by process"""
        self.group_outputs()
        self.scale_histograms()
        
        print_header("grouping scaled histograms by sample")
        
        processed_histograms = {}
        for sample in self.scaled_histograms:
            dataset_config = load_config(
                config_type="dataset", config_name=sample, year=self.year
            )
            process = dataset_config.process
            if process not in processed_histograms:
                print(f"Initializing {process} histograms with {sample} histograms")
                processed_histograms[process] = [self.scaled_histograms[sample]]
            else:
                print(f"Appending {sample} histograms to {process} histograms")
                processed_histograms[process].append(self.scaled_histograms[sample])
        for process in processed_histograms:
            processed_histograms[process] = accumulate(
                processed_histograms[process]
            )
        print(f"\nProcesses grouped: {list(processed_histograms.keys())}")
        return processed_histograms