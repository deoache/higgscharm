from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="DYto2L_2Jets_10to50",
    process="DY+Jets",
    path=(
        "/pnfs/iihe/cms/store/user/daocampo/PFNano_Run3/"
        "mc_summer22_MINIAODv4/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/"
        "Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2_BTV_Run3_2022_Comm_MINIAODv4/240618_165543/0000/"
    ),
    key="Events",
    year="2022",
    era="MC",
    xsec=20950.0,
    partitions=10,
    stepsize=50_000,
)
