from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="WW",
    path=(
        "root://maite.iihe.ac.be:1094//store/user/daocampo/PFNano_Run3/"
        "mc_summer22EE_MINIAODv4/WW_TuneCP5_13p6TeV_pythia8/"
        "Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2_BTV_Run3_2022_Comm_MINIAODv4/240518_172311/0000/"
    ),
    key="Events",
    year="2022EE",
    era="MC",
    xsec=80.23,
    partitions=3,
    stepsize=50_000,
    filenames=(
        "MC_defaultAK4_173.root",
        "MC_defaultAK4_65.root",
        "MC_defaultAK4_20.root",
        "MC_defaultAK4_21.root",
        "MC_defaultAK4_129.root",
        "MC_defaultAK4_27.root",
        "MC_defaultAK4_61.root",
        "MC_defaultAK4_10.root",
        "MC_defaultAK4_22.root",
        "MC_defaultAK4_121.root",
        "MC_defaultAK4_126.root",
        "MC_defaultAK4_14.root",
        "MC_defaultAK4_124.root",
        "MC_defaultAK4_66.root",
        "MC_defaultAK4_12.root",
        "MC_defaultAK4_164.root",
        "MC_defaultAK4_68.root",
        "MC_defaultAK4_67.root",
        "MC_defaultAK4_70.root",
        "MC_defaultAK4_73.root",
        "MC_defaultAK4_23.root",
        "MC_defaultAK4_60.root",
        "MC_defaultAK4_62.root",
        "MC_defaultAK4_72.root",
        "MC_defaultAK4_71.root",
        "MC_defaultAK4_15.root",
        "MC_defaultAK4_26.root",
        "MC_defaultAK4_18.root",
        "MC_defaultAK4_122.root",
        "MC_defaultAK4_11.root",
        "MC_defaultAK4_16.root",
        "MC_defaultAK4_17.root",
        "MC_defaultAK4_13.root",
        "MC_defaultAK4_69.root",
        "MC_defaultAK4_25.root",
        "MC_defaultAK4_28.root",
        "MC_defaultAK4_125.root",
        "MC_defaultAK4_29.root",
        "MC_defaultAK4_19.root",
        "MC_defaultAK4_118.root",
        "MC_defaultAK4_24.root",
        "MC_defaultAK4_110.root",
        "MC_defaultAK4_78.root",
        "MC_defaultAK4_105.root",
        "MC_defaultAK4_77.root",
        "MC_defaultAK4_120.root",
        "MC_defaultAK4_74.root",
        "MC_defaultAK4_111.root",
        "MC_defaultAK4_113.root",
        "MC_defaultAK4_117.root",
        "MC_defaultAK4_108.root",
        "MC_defaultAK4_104.root",
        "MC_defaultAK4_75.root",
        "MC_defaultAK4_79.root",
        "MC_defaultAK4_101.root",
        "MC_defaultAK4_102.root",
        "MC_defaultAK4_109.root",
        "MC_defaultAK4_103.root",
        "MC_defaultAK4_107.root",
        "MC_defaultAK4_116.root",
        "MC_defaultAK4_128.root",
        "MC_defaultAK4_115.root",
        "MC_defaultAK4_106.root",
        "MC_defaultAK4_119.root",
        "MC_defaultAK4_114.root",
        "MC_defaultAK4_112.root",
        "MC_defaultAK4_76.root",
        "MC_defaultAK4_123.root",
        "MC_defaultAK4_163.root",
        "MC_defaultAK4_166.root",
        "MC_defaultAK4_172.root",
        "MC_defaultAK4_165.root",
        "MC_defaultAK4_162.root",
        "MC_defaultAK4_171.root",
        "MC_defaultAK4_168.root",
        "MC_defaultAK4_169.root",
        "MC_defaultAK4_167.root",
        "MC_defaultAK4_170.root",
        "MC_defaultAK4_64.root",
        "MC_defaultAK4_155.root",
        "MC_defaultAK4_153.root",
        "MC_defaultAK4_127.root",
        "MC_defaultAK4_151.root",
        "MC_defaultAK4_158.root",
        "MC_defaultAK4_63.root",
        "MC_defaultAK4_150.root",
        "MC_defaultAK4_157.root",
        "MC_defaultAK4_152.root",
        "MC_defaultAK4_156.root",
        "MC_defaultAK4_154.root",
        "MC_defaultAK4_160.root",
        "MC_defaultAK4_159.root",
        "MC_defaultAK4_161.root",
        "MC_defaultAK4_3-5.root",
        "MC_defaultAK4_3-1.root",
        "MC_defaultAK4_3-4.root",
        "MC_defaultAK4_3-2.root",
        "MC_defaultAK4_3-3.root",
        "MC_defaultAK4_30.root",
        "MC_defaultAK4_31.root",
        "MC_defaultAK4_32.root",
        "MC_defaultAK4_33.root",
        "MC_defaultAK4_34.root",
        "MC_defaultAK4_80.root",
        "MC_defaultAK4_35.root",
        "MC_defaultAK4_81.root",
        "MC_defaultAK4_36.root",
        "MC_defaultAK4_82.root",
        "MC_defaultAK4_37.root",
        "MC_defaultAK4_83.root",
        "MC_defaultAK4_38.root",
        "MC_defaultAK4_84.root",
        "MC_defaultAK4_39.root",
        "MC_defaultAK4_85.root",
        "MC_defaultAK4_86.root",
        "MC_defaultAK4_1.root",
        "MC_defaultAK4_87.root",
        "MC_defaultAK4_2.root",
        "MC_defaultAK4_88.root",
        "MC_defaultAK4_3.root",
        "MC_defaultAK4_89.root",
        "MC_defaultAK4_4.root",
        "MC_defaultAK4_5.root",
        "MC_defaultAK4_130.root",
        "MC_defaultAK4_6.root",
        "MC_defaultAK4_131.root",
        "MC_defaultAK4_7.root",
        "MC_defaultAK4_132.root",
        "MC_defaultAK4_8.root",
        "MC_defaultAK4_133.root",
        "MC_defaultAK4_9.root",
        "MC_defaultAK4_134.root",
        "MC_defaultAK4_135.root",
        "MC_defaultAK4_136.root",
        "MC_defaultAK4_137.root",
        "MC_defaultAK4_138.root",
        "MC_defaultAK4_139.root",
        "MC_defaultAK4_40.root",
        "MC_defaultAK4_41.root",
        "MC_defaultAK4_42.root",
        "MC_defaultAK4_43.root",
        "MC_defaultAK4_44.root",
        "MC_defaultAK4_90.root",
        "MC_defaultAK4_45.root",
        "MC_defaultAK4_91.root",
        "MC_defaultAK4_46.root",
        "MC_defaultAK4_92.root",
        "MC_defaultAK4_47.root",
        "MC_defaultAK4_93.root",
        "MC_defaultAK4_48.root",
        "MC_defaultAK4_94.root",
        "MC_defaultAK4_49.root",
        "MC_defaultAK4_95.root",
        "MC_defaultAK4_2-1.root",
        "MC_defaultAK4_96.root",
        "MC_defaultAK4_97.root",
        "MC_defaultAK4_98.root",
        "MC_defaultAK4_99.root",
        "MC_defaultAK4_140.root",
        "MC_defaultAK4_141.root",
        "MC_defaultAK4_142.root",
        "MC_defaultAK4_143.root",
        "MC_defaultAK4_144.root",
        "MC_defaultAK4_145.root",
        "MC_defaultAK4_146.root",
        "MC_defaultAK4_147.root",
        "MC_defaultAK4_148.root",
        "MC_defaultAK4_149.root",
        "MC_defaultAK4_50.root",
        "MC_defaultAK4_51.root",
        "MC_defaultAK4_52.root",
        "MC_defaultAK4_53.root",
        "MC_defaultAK4_54.root",
        "MC_defaultAK4_55.root",
        "MC_defaultAK4_56.root",
        "MC_defaultAK4_57.root",
        "MC_defaultAK4_58.root",
        "MC_defaultAK4_59.root",
        "MC_defaultAK4_100.root",
    ),
)