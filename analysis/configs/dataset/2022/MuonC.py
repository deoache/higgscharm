from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="MuonC",
    process="Data",
    path=(
        "/pnfs/iihe/cms/store/user/daocampo/PFNano_Run3/"
        "data_2022_MINIAODv4/Muon/Run2022C-22Sep2023-v1_BTV_Run3_2022_Comm_MINIAODv4/240429_092050/"
    ),
    key="Events",
    year="2022",
    era="C",
    xsec=None,
    stepsize=50_000,
)
