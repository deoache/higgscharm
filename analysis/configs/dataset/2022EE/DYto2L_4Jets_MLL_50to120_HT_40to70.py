from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="DYto2L_4Jets_MLL_50to120_HT_40to70",
    process="DY+Jets",
    path=(
        "/pnfs/iihe/cms/store/user/tvanlaer/PFNano_Run3/"
        "mc_summer22EE_MINIAODv4/DYto2L-4Jets_MLL-50to120_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/"
        "Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v1_BTV_Run3_2022_Comm_MINIAODv4/240827_142011/0000/"
    ),
    key="Events",
    year="2022EE",
    era="MC",
    xsec=None,
    partitions=4,
    stepsize=50_000,
)