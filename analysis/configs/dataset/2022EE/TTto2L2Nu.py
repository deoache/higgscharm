from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="TTto2L2Nu",
    process="tt",
    path=(
        "/pnfs/iihe/cms/store/user/daocampo/PFNano_Run3/"
        "mc_summer22EE_MINIAODv4/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/"
        "Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2_BTV_Run3_2022_Comm_MINIAODv4/240515_152841/0000/"
    ),
    key="Events",
    year="2022EE",
    era="MC",
    xsec=762.1,
    partitions=20,
    stepsize=50_000,
)