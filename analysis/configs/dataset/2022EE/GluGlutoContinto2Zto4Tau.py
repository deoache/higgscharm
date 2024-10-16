from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="GluGlutoContinto2Zto4Tau",
    process="ggToZZ",
    path=(
        "/pnfs/iihe/cms/store/user/daocampo/PFNano_Run3/"
        "mc_summer22EE_MINIAODv4/GluGlutoContinto2Zto4Tau_TuneCP5_13p6TeV_mcfm-pythia8/"
        "Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2_BTV_Run3_2022_Comm_MINIAODv4/240325_122551/0000/"
    ),
    key="Events",
    year="2022EE",
    era="MC",
    xsec=3.042,
    partitions=3,
    stepsize=50_000,
)
