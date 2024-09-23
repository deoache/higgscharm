from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="DYto2L_4Jets_MLL_4to50_HT_1500to2500",
    process="DY+Jets",
    path=(
        "/pnfs/iihe/cms/store/user/tvanlaer/PFNano_Run3/"
        "mc_summer22EE_MINIAODv4/DYto2L-4Jets_MLL-4to50_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/"
        "Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2_BTV_Run3_2022_Comm_MINIAODv4/240906_155423/0000/"
    ),
    key="Events",
    year="2022EE",
    era="MC",
    xsec=None,
    partitions=2,
    stepsize=50_000,
    filenames=(
        'MC_defaultAK4_1-1.root',
        'MC_defaultAK4_1-2.root',
        'MC_defaultAK4_1-3.root',
        'MC_defaultAK4_1-4.root',
        'MC_defaultAK4_1-5.root',
        'MC_defaultAK4_1.root',
        'MC_defaultAK4_10.root',
        'MC_defaultAK4_11.root',
        'MC_defaultAK4_12.root',
        'MC_defaultAK4_13.root',
        'MC_defaultAK4_14.root',
        'MC_defaultAK4_15.root',
        'MC_defaultAK4_16.root',
        'MC_defaultAK4_17.root',
        'MC_defaultAK4_18.root',
        'MC_defaultAK4_19.root',
        'MC_defaultAK4_2.root',
        'MC_defaultAK4_20.root',
        'MC_defaultAK4_21.root',
        'MC_defaultAK4_22.root',
        'MC_defaultAK4_23.root',
        'MC_defaultAK4_24.root',
        'MC_defaultAK4_25.root',
        'MC_defaultAK4_26.root',
        'MC_defaultAK4_27.root',
        'MC_defaultAK4_28.root',
        'MC_defaultAK4_29.root',
        'MC_defaultAK4_3.root',
        'MC_defaultAK4_30.root',
        'MC_defaultAK4_31.root',
        'MC_defaultAK4_32.root',
        'MC_defaultAK4_33.root',
        'MC_defaultAK4_34.root',
        'MC_defaultAK4_35.root',
        'MC_defaultAK4_36.root',
        'MC_defaultAK4_38.root',
        'MC_defaultAK4_4.root',
        'MC_defaultAK4_5.root',
        'MC_defaultAK4_6.root',
        'MC_defaultAK4_7.root',
        'MC_defaultAK4_8.root',
        'MC_defaultAK4_9.root',
    ),
)
