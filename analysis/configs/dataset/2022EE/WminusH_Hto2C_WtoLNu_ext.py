from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="WminusH_Hto2C_WtoLNu_ext",
    process="WHcc",
    path=(
        "/pnfs/iihe/cms/store/user/daocampo/PFNano_Run3/"
        "mc_summer22EE_MINIAODv4/WminusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/"
        "Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2_BTV_Run3_2022_Comm_MINIAODv4/240601_140200/0000/"
    ),
    key="Events",
    year="2022EE",
    era="MC",
    xsec=None,
    partitions=5,
    stepsize=50_000,
    filenames=(
        "MC_defaultAK4_73.root",
        "MC_defaultAK4_74.root",
        "MC_defaultAK4_62.root",
        "MC_defaultAK4_70.root",
        "MC_defaultAK4_26.root",
        "MC_defaultAK4_61.root",
        "MC_defaultAK4_14.root",
        "MC_defaultAK4_29.root",
        "MC_defaultAK4_63.root",
        "MC_defaultAK4_60.root",
        "MC_defaultAK4_65.root",
        "MC_defaultAK4_64.root",
        "MC_defaultAK4_15.root",
        "MC_defaultAK4_68.root",
        "MC_defaultAK4_20.root",
        "MC_defaultAK4_79.root",
        "MC_defaultAK4_10.root",
        "MC_defaultAK4_16.root",
        "MC_defaultAK4_21.root",
        "MC_defaultAK4_11.root",
        "MC_defaultAK4_66.root",
        "MC_defaultAK4_24.root",
        "MC_defaultAK4_75.root",
        "MC_defaultAK4_67.root",
        "MC_defaultAK4_17.root",
        "MC_defaultAK4_71.root",
        "MC_defaultAK4_18.root",
        "MC_defaultAK4_69.root",
        "MC_defaultAK4_19.root",
        "MC_defaultAK4_28.root",
        "MC_defaultAK4_72.root",
        "MC_defaultAK4_27.root",
        "MC_defaultAK4_22.root",
        "MC_defaultAK4_25.root",
        "MC_defaultAK4_77.root",
        "MC_defaultAK4_76.root",
        "MC_defaultAK4_23.root",
        "MC_defaultAK4_78.root",
        "MC_defaultAK4_12.root",
        "MC_defaultAK4_13.root",
        "MC_defaultAK4_1-122.root",
        "MC_defaultAK4_1-86.root",
        "MC_defaultAK4_1-2.root",
        "MC_defaultAK4_1-28.root",
        "MC_defaultAK4_1-29.root",
        "MC_defaultAK4_1-70.root",
        "MC_defaultAK4_1-175.root",
        "MC_defaultAK4_1-140.root",
        "MC_defaultAK4_1-31.root",
        "MC_defaultAK4_1-9.root",
        "MC_defaultAK4_1-8.root",
        "MC_defaultAK4_1-124.root",
        "MC_defaultAK4_1-3.root",
        "MC_defaultAK4_1-6.root",
        "MC_defaultAK4_1-74.root",
        "MC_defaultAK4_1-176.root",
        "MC_defaultAK4_1-141.root",
        "MC_defaultAK4_1-177.root",
        "MC_defaultAK4_1-191.root",
        "MC_defaultAK4_1-85.root",
        "MC_defaultAK4_1-187.root",
        "MC_defaultAK4_1-171.root",
        "MC_defaultAK4_1-172.root",
        "MC_defaultAK4_1-188.root",
        "MC_defaultAK4_1-120.root",
        "MC_defaultAK4_1-146.root",
        "MC_defaultAK4_1-36.root",
        "MC_defaultAK4_1-182.root",
        "MC_defaultAK4_1-43.root",
        "MC_defaultAK4_1-183.root",
        "MC_defaultAK4_1-121.root",
        "MC_defaultAK4_1-194.root",
        "MC_defaultAK4_1-200.root",
        "MC_defaultAK4_1-192.root",
        "MC_defaultAK4_1-83.root",
        "MC_defaultAK4_1-138.root",
        "MC_defaultAK4_1-125.root",
        "MC_defaultAK4_1-76.root",
        "MC_defaultAK4_1-1.root",
        "MC_defaultAK4_1-38.root",
        "MC_defaultAK4_1-80.root",
        "MC_defaultAK4_1-132.root",
        "MC_defaultAK4_1-126.root",
        "MC_defaultAK4_1-129.root",
        "MC_defaultAK4_1-189.root",
        "MC_defaultAK4_1-174.root",
        "MC_defaultAK4_1-75.root",
        "MC_defaultAK4_1-89.root",
        "MC_defaultAK4_1-143.root",
        "MC_defaultAK4_1-137.root",
        "MC_defaultAK4_1-33.root",
        "MC_defaultAK4_1-5.root",
        "MC_defaultAK4_1-35.root",
        "MC_defaultAK4_1-123.root",
        "MC_defaultAK4_1-39.root",
        "MC_defaultAK4_1-135.root",
        "MC_defaultAK4_1-148.root",
        "MC_defaultAK4_1-87.root",
        "MC_defaultAK4_1-88.root",
        "MC_defaultAK4_1-72.root",
        "MC_defaultAK4_1-37.root",
        "MC_defaultAK4_1-144.root",
        "MC_defaultAK4_1-82.root",
        "MC_defaultAK4_1-7.root",
        "MC_defaultAK4_1-42.root",
        "MC_defaultAK4_1-178.root",
        "MC_defaultAK4_1-170.root",
        "MC_defaultAK4_1-127.root",
        "MC_defaultAK4_1-30.root",
        "MC_defaultAK4_1-184.root",
        "MC_defaultAK4_1-131.root",
        "MC_defaultAK4_1-84.root",
        "MC_defaultAK4_1-79.root",
        "MC_defaultAK4_1-77.root",
        "MC_defaultAK4_1-136.root",
        "MC_defaultAK4_1-179.root",
        "MC_defaultAK4_1-139.root",
        "MC_defaultAK4_1-78.root",
        "MC_defaultAK4_1-142.root",
        "MC_defaultAK4_1-133.root",
        "MC_defaultAK4_1-149.root",
        "MC_defaultAK4_1-190.root",
        "MC_defaultAK4_1-185.root",
        "MC_defaultAK4_1-4.root",
        "MC_defaultAK4_1-193.root",
        "MC_defaultAK4_1-181.root",
        "MC_defaultAK4_1-180.root",
        "MC_defaultAK4_1-81.root",
        "MC_defaultAK4_1-134.root",
        "MC_defaultAK4_1-145.root",
        "MC_defaultAK4_1-41.root",
        "MC_defaultAK4_1-128.root",
        "MC_defaultAK4_1-73.root",
        "MC_defaultAK4_1-130.root",
        "MC_defaultAK4_1-186.root",
        "MC_defaultAK4_1-71.root",
        "MC_defaultAK4_1-173.root",
        "MC_defaultAK4_1-40.root",
        "MC_defaultAK4_1-32.root",
        "MC_defaultAK4_1-34.root",
        "MC_defaultAK4_1-147.root",
        "MC_defaultAK4_1-21.root",
        "MC_defaultAK4_1-25.root",
        "MC_defaultAK4_1-27.root",
        "MC_defaultAK4_1-20.root",
        "MC_defaultAK4_1-24.root",
        "MC_defaultAK4_1-23.root",
        "MC_defaultAK4_1-26.root",
        "MC_defaultAK4_1-22.root",
        "MC_defaultAK4_1-195.root",
        "MC_defaultAK4_1-44.root",
        "MC_defaultAK4_1-196.root",
        "MC_defaultAK4_30.root",
        "MC_defaultAK4_1-90.root",
        "MC_defaultAK4_1-45.root",
        "MC_defaultAK4_1-197.root",
        "MC_defaultAK4_31.root",
        "MC_defaultAK4_1-91.root",
        "MC_defaultAK4_1-46.root",
        "MC_defaultAK4_1-198.root",
        "MC_defaultAK4_32.root",
        "MC_defaultAK4_1-92.root",
        "MC_defaultAK4_1-47.root",
        "MC_defaultAK4_1-199.root",
        "MC_defaultAK4_33.root",
        "MC_defaultAK4_1-93.root",
        "MC_defaultAK4_1-48.root",
        "MC_defaultAK4_34.root",
        "MC_defaultAK4_1-94.root",
        "MC_defaultAK4_1-49.root",
        "MC_defaultAK4_35.root",
        "MC_defaultAK4_1-95.root",
        "MC_defaultAK4_36.root",
        "MC_defaultAK4_1-96.root",
        "MC_defaultAK4_37.root",
        "MC_defaultAK4_1-97.root",
        "MC_defaultAK4_38.root",
        "MC_defaultAK4_1-98.root",
        "MC_defaultAK4_39.root",
        "MC_defaultAK4_1-99.root",
        "MC_defaultAK4_1.root",
        "MC_defaultAK4_2.root",
        "MC_defaultAK4_3.root",
        "MC_defaultAK4_4.root",
        "MC_defaultAK4_1-100.root",
        "MC_defaultAK4_5.root",
        "MC_defaultAK4_1-101.root",
        "MC_defaultAK4_6.root",
        "MC_defaultAK4_1-102.root",
        "MC_defaultAK4_7.root",
        "MC_defaultAK4_1-103.root",
        "MC_defaultAK4_8.root",
        "MC_defaultAK4_1-104.root",
        "MC_defaultAK4_9.root",
        "MC_defaultAK4_1-150.root",
        "MC_defaultAK4_1-105.root",
        "MC_defaultAK4_1-151.root",
        "MC_defaultAK4_1-106.root",
        "MC_defaultAK4_1-152.root",
        "MC_defaultAK4_1-107.root",
        "MC_defaultAK4_1-153.root",
        "MC_defaultAK4_1-108.root",
        "MC_defaultAK4_1-154.root",
        "MC_defaultAK4_1-109.root",
        "MC_defaultAK4_1-155.root",
        "MC_defaultAK4_1-156.root",
        "MC_defaultAK4_1-50.root",
        "MC_defaultAK4_1-157.root",
        "MC_defaultAK4_1-51.root",
        "MC_defaultAK4_1-158.root",
        "MC_defaultAK4_1-52.root",
        "MC_defaultAK4_1-159.root",
        "MC_defaultAK4_1-53.root",
        "MC_defaultAK4_1-54.root",
        "MC_defaultAK4_40.root",
        "MC_defaultAK4_1-55.root",
        "MC_defaultAK4_41.root",
        "MC_defaultAK4_1-56.root",
        "MC_defaultAK4_42.root",
        "MC_defaultAK4_1-57.root",
        "MC_defaultAK4_43.root",
        "MC_defaultAK4_1-58.root",
        "MC_defaultAK4_44.root",
        "MC_defaultAK4_1-59.root",
        "MC_defaultAK4_45.root",
        "MC_defaultAK4_46.root",
        "MC_defaultAK4_47.root",
        "MC_defaultAK4_48.root",
        "MC_defaultAK4_49.root",
        "MC_defaultAK4_1-110.root",
        "MC_defaultAK4_1-111.root",
        "MC_defaultAK4_1-112.root",
        "MC_defaultAK4_1-113.root",
        "MC_defaultAK4_1-114.root",
        "MC_defaultAK4_1-160.root",
        "MC_defaultAK4_1-115.root",
        "MC_defaultAK4_1-161.root",
        "MC_defaultAK4_1-116.root",
        "MC_defaultAK4_1-10.root",
        "MC_defaultAK4_1-162.root",
        "MC_defaultAK4_1-117.root",
        "MC_defaultAK4_1-11.root",
        "MC_defaultAK4_1-163.root",
        "MC_defaultAK4_1-118.root",
        "MC_defaultAK4_1-12.root",
        "MC_defaultAK4_1-164.root",
        "MC_defaultAK4_1-119.root",
        "MC_defaultAK4_1-13.root",
        "MC_defaultAK4_1-165.root",
        "MC_defaultAK4_1-14.root",
        "MC_defaultAK4_1-166.root",
        "MC_defaultAK4_1-60.root",
        "MC_defaultAK4_1-15.root",
        "MC_defaultAK4_1-167.root",
        "MC_defaultAK4_1-61.root",
        "MC_defaultAK4_1-16.root",
        "MC_defaultAK4_1-168.root",
        "MC_defaultAK4_1-62.root",
        "MC_defaultAK4_1-17.root",
        "MC_defaultAK4_1-169.root",
        "MC_defaultAK4_1-63.root",
        "MC_defaultAK4_1-18.root",
        "MC_defaultAK4_1-64.root",
        "MC_defaultAK4_1-19.root",
        "MC_defaultAK4_50.root",
        "MC_defaultAK4_1-65.root",
        "MC_defaultAK4_51.root",
        "MC_defaultAK4_1-66.root",
        "MC_defaultAK4_52.root",
        "MC_defaultAK4_1-67.root",
        "MC_defaultAK4_53.root",
        "MC_defaultAK4_1-68.root",
        "MC_defaultAK4_54.root",
        "MC_defaultAK4_1-69.root",
        "MC_defaultAK4_55.root",
        "MC_defaultAK4_56.root",
        "MC_defaultAK4_57.root",
        "MC_defaultAK4_58.root",
        "MC_defaultAK4_59.root",
    ),
)