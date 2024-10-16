from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="MuonE",
    process="Data",
    path=(
        "/pnfs/iihe/cms/store/user/daocampo/PFNano_Run3/"
        "data_2022_MINIAODv4/Muon/Run2022E-22Sep2023-v1_BTV_Run3_2022_Comm_MINIAODv4/240429_092108/"
    ),
    key="Events",
    year="2022EE",
    era="E",
    xsec=None,
    stepsize=50_000,
)
