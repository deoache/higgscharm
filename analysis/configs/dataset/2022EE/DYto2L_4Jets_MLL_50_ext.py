from analysis.configs.dataset_config import DatasetConfig

dataset_config = DatasetConfig(
    name="DYto2L_4Jets_MLL_50_ext",
    process="DY+Jets",
    path=(
        "/pnfs/iihe/cms/store/user/tvanlaer/PFNano_Run3/"
        "mc_summer22EE_MINIAODv4/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/"
        "Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2_BTV_Run3_2022_Comm_MINIAODv4/240827_213219/0000/"
    ),
    key="Events",
    year="2022EE",
    era="MC",
    xsec=None,
    partitions=30,
    stepsize=50_000,
    filenames=(
        'MC_defaultAK4_1-100.root',
        'MC_defaultAK4_1-101.root',
        'MC_defaultAK4_1-102.root',
        'MC_defaultAK4_1-103.root',
        'MC_defaultAK4_1-104.root',
        'MC_defaultAK4_1-105.root',
        'MC_defaultAK4_1-106.root',
        'MC_defaultAK4_1-107.root',
        'MC_defaultAK4_1-108.root',
        'MC_defaultAK4_1-109.root',
        'MC_defaultAK4_1-110.root',
        'MC_defaultAK4_1-111.root',
        'MC_defaultAK4_1-112.root',
        'MC_defaultAK4_1-113.root',
        'MC_defaultAK4_1-114.root',
        'MC_defaultAK4_1-115.root',
        'MC_defaultAK4_1-116.root',
        'MC_defaultAK4_1-117.root',
        'MC_defaultAK4_1-118.root',
        'MC_defaultAK4_1-119.root',
        'MC_defaultAK4_1-12.root',
        'MC_defaultAK4_1-120.root',
        'MC_defaultAK4_1-121.root',
        'MC_defaultAK4_1-122.root',
        'MC_defaultAK4_1-123.root',
        'MC_defaultAK4_1-124.root',
        'MC_defaultAK4_1-125.root',
        'MC_defaultAK4_1-126.root',
        'MC_defaultAK4_1-127.root',
        'MC_defaultAK4_1-128.root',
        'MC_defaultAK4_1-129.root',
        'MC_defaultAK4_1-130.root',
        'MC_defaultAK4_1-131.root',
        'MC_defaultAK4_1-132.root',
        'MC_defaultAK4_1-133.root',
        'MC_defaultAK4_1-134.root',
        'MC_defaultAK4_1-135.root',
        'MC_defaultAK4_1-136.root',
        'MC_defaultAK4_1-137.root',
        'MC_defaultAK4_1-138.root',
        'MC_defaultAK4_1-139.root',
        'MC_defaultAK4_1-140.root',
        'MC_defaultAK4_1-141.root',
        'MC_defaultAK4_1-142.root',
        'MC_defaultAK4_1-143.root',
        'MC_defaultAK4_1-144.root',
        'MC_defaultAK4_1-145.root',
        'MC_defaultAK4_1-146.root',
        'MC_defaultAK4_1-147.root',
        'MC_defaultAK4_1-148.root',
        'MC_defaultAK4_1-149.root',
        'MC_defaultAK4_1-150.root',
        'MC_defaultAK4_1-151.root',
        'MC_defaultAK4_1-152.root',
        'MC_defaultAK4_1-153.root',
        'MC_defaultAK4_1-154.root',
        'MC_defaultAK4_1-155.root',
        'MC_defaultAK4_1-156.root',
        'MC_defaultAK4_1-157.root',
        'MC_defaultAK4_1-158.root',
        'MC_defaultAK4_1-159.root',
        'MC_defaultAK4_1-160.root',
        'MC_defaultAK4_1-161.root',
        'MC_defaultAK4_1-162.root',
        'MC_defaultAK4_1-163.root',
        'MC_defaultAK4_1-164.root',
        'MC_defaultAK4_1-165.root',
        'MC_defaultAK4_1-166.root',
        'MC_defaultAK4_1-167.root',
        'MC_defaultAK4_1-168.root',
        'MC_defaultAK4_1-169.root',
        'MC_defaultAK4_1-170.root',
        'MC_defaultAK4_1-171.root',
        'MC_defaultAK4_1-172.root',
        'MC_defaultAK4_1-173.root',
        'MC_defaultAK4_1-174.root',
        'MC_defaultAK4_1-175.root',
        'MC_defaultAK4_1-176.root',
        'MC_defaultAK4_1-177.root',
        'MC_defaultAK4_1-178.root',
        'MC_defaultAK4_1-179.root',
        'MC_defaultAK4_1-18.root',
        'MC_defaultAK4_1-180.root',
        'MC_defaultAK4_1-181.root',
        'MC_defaultAK4_1-182.root',
        'MC_defaultAK4_1-183.root',
        'MC_defaultAK4_1-184.root',
        'MC_defaultAK4_1-185.root',
        'MC_defaultAK4_1-186.root',
        'MC_defaultAK4_1-187.root',
        'MC_defaultAK4_1-188.root',
        'MC_defaultAK4_1-189.root',
        'MC_defaultAK4_1-190.root',
        'MC_defaultAK4_1-191.root',
        'MC_defaultAK4_1-192.root',
        'MC_defaultAK4_1-193.root',
        'MC_defaultAK4_1-194.root',
        'MC_defaultAK4_1-195.root',
        'MC_defaultAK4_1-196.root',
        'MC_defaultAK4_1-197.root',
        'MC_defaultAK4_1-198.root',
        'MC_defaultAK4_1-199.root',
        'MC_defaultAK4_1-2.root',
        'MC_defaultAK4_1-200.root',
        'MC_defaultAK4_1-201.root',
        'MC_defaultAK4_1-202.root',
        'MC_defaultAK4_1-203.root',
        'MC_defaultAK4_1-204.root',
        'MC_defaultAK4_1-205.root',
        'MC_defaultAK4_1-206.root',
        'MC_defaultAK4_1-207.root',
        'MC_defaultAK4_1-208.root',
        'MC_defaultAK4_1-209.root',
        'MC_defaultAK4_1-210.root',
        'MC_defaultAK4_1-211.root',
        'MC_defaultAK4_1-212.root',
        'MC_defaultAK4_1-213.root',
        'MC_defaultAK4_1-37.root',
        'MC_defaultAK4_1-38.root',
        'MC_defaultAK4_1-39.root',
        'MC_defaultAK4_1-40.root',
        'MC_defaultAK4_1-41.root',
        'MC_defaultAK4_1-42.root',
        'MC_defaultAK4_1-43.root',
        'MC_defaultAK4_1-44.root',
        'MC_defaultAK4_1-45.root',
        'MC_defaultAK4_1-46.root',
        'MC_defaultAK4_1-47.root',
        'MC_defaultAK4_1-48.root',
        'MC_defaultAK4_1-49.root',
        'MC_defaultAK4_1-50.root',
        'MC_defaultAK4_1-51.root',
        'MC_defaultAK4_1-52.root',
        'MC_defaultAK4_1-53.root',
        'MC_defaultAK4_1-54.root',
        'MC_defaultAK4_1-55.root',
        'MC_defaultAK4_1-56.root',
        'MC_defaultAK4_1-57.root',
        'MC_defaultAK4_1-58.root',
        'MC_defaultAK4_1-59.root',
        'MC_defaultAK4_1-60.root',
        'MC_defaultAK4_1-61.root',
        'MC_defaultAK4_1-62.root',
        'MC_defaultAK4_1-63.root',
        'MC_defaultAK4_1-64.root',
        'MC_defaultAK4_1-65.root',
        'MC_defaultAK4_1-66.root',
        'MC_defaultAK4_1-67.root',
        'MC_defaultAK4_1-68.root',
        'MC_defaultAK4_1-69.root',
        'MC_defaultAK4_1-70.root',
        'MC_defaultAK4_1-71.root',
        'MC_defaultAK4_1-72.root',
        'MC_defaultAK4_1-73.root',
        'MC_defaultAK4_1-74.root',
        'MC_defaultAK4_1-75.root',
        'MC_defaultAK4_1-76.root',
        'MC_defaultAK4_1-77.root',
        'MC_defaultAK4_1-78.root',
        'MC_defaultAK4_1-79.root',
        'MC_defaultAK4_1-80.root',
        'MC_defaultAK4_1-81.root',
        'MC_defaultAK4_1-82.root',
        'MC_defaultAK4_1-83.root',
        'MC_defaultAK4_1-84.root',
        'MC_defaultAK4_1-85.root',
        'MC_defaultAK4_1-86.root',
        'MC_defaultAK4_1-87.root',
        'MC_defaultAK4_1-88.root',
        'MC_defaultAK4_1-89.root',
        'MC_defaultAK4_1-90.root',
        'MC_defaultAK4_1-91.root',
        'MC_defaultAK4_1-92.root',
        'MC_defaultAK4_1-93.root',
        'MC_defaultAK4_1-94.root',
        'MC_defaultAK4_1-95.root',
        'MC_defaultAK4_1-96.root',
        'MC_defaultAK4_1-97.root',
        'MC_defaultAK4_1-98.root',
        'MC_defaultAK4_1-99.root',
        'MC_defaultAK4_1.root',
        'MC_defaultAK4_10.root',
        'MC_defaultAK4_100.root',
        'MC_defaultAK4_101.root',
        'MC_defaultAK4_102.root',
        'MC_defaultAK4_103.root',
        'MC_defaultAK4_104.root',
        'MC_defaultAK4_105.root',
        'MC_defaultAK4_106.root',
        'MC_defaultAK4_107.root',
        'MC_defaultAK4_108.root',
        'MC_defaultAK4_109.root',
        'MC_defaultAK4_11.root',
        'MC_defaultAK4_110.root',
        'MC_defaultAK4_111.root',
        'MC_defaultAK4_112.root',
        'MC_defaultAK4_113.root',
        'MC_defaultAK4_114.root',
        'MC_defaultAK4_115.root',
        'MC_defaultAK4_116.root',
        'MC_defaultAK4_117.root',
        'MC_defaultAK4_118.root',
        'MC_defaultAK4_119.root',
        'MC_defaultAK4_12.root',
        'MC_defaultAK4_120.root',
        'MC_defaultAK4_121.root',
        'MC_defaultAK4_122.root',
        'MC_defaultAK4_123.root',
        'MC_defaultAK4_124.root',
        'MC_defaultAK4_125.root',
        'MC_defaultAK4_126.root',
        'MC_defaultAK4_127.root',
        'MC_defaultAK4_128.root',
        'MC_defaultAK4_129.root',
        'MC_defaultAK4_13.root',
        'MC_defaultAK4_130.root',
        'MC_defaultAK4_131.root',
        'MC_defaultAK4_132.root',
        'MC_defaultAK4_133.root',
        'MC_defaultAK4_134.root',
        'MC_defaultAK4_135.root',
        'MC_defaultAK4_136.root',
        'MC_defaultAK4_137.root',
        'MC_defaultAK4_138.root',
        'MC_defaultAK4_139.root',
        'MC_defaultAK4_14.root',
        'MC_defaultAK4_140.root',
        'MC_defaultAK4_141.root',
        'MC_defaultAK4_149.root',
        'MC_defaultAK4_15.root',
        'MC_defaultAK4_150.root',
        'MC_defaultAK4_151.root',
        'MC_defaultAK4_156.root',
        'MC_defaultAK4_158.root',
        'MC_defaultAK4_159.root',
        'MC_defaultAK4_16.root',
        'MC_defaultAK4_160.root',
        'MC_defaultAK4_161.root',
        'MC_defaultAK4_162.root',
        'MC_defaultAK4_165.root',
        'MC_defaultAK4_17.root',
        'MC_defaultAK4_177.root',
        'MC_defaultAK4_18.root',
        'MC_defaultAK4_184.root',
        'MC_defaultAK4_185.root',
        'MC_defaultAK4_186.root',
        'MC_defaultAK4_187.root',
        'MC_defaultAK4_188.root',
        'MC_defaultAK4_189.root',
        'MC_defaultAK4_19.root',
        'MC_defaultAK4_190.root',
        'MC_defaultAK4_191.root',
        'MC_defaultAK4_192.root',
        'MC_defaultAK4_193.root',
        'MC_defaultAK4_194.root',
        'MC_defaultAK4_195.root',
        'MC_defaultAK4_196.root',
        'MC_defaultAK4_197.root',
        'MC_defaultAK4_198.root',
        'MC_defaultAK4_199.root',
        'MC_defaultAK4_2-1.root',
        'MC_defaultAK4_2-10.root',
        'MC_defaultAK4_2-100.root',
        'MC_defaultAK4_2-101.root',
        'MC_defaultAK4_2-102.root',
        'MC_defaultAK4_2-103.root',
        'MC_defaultAK4_2-104.root',
        'MC_defaultAK4_2-105.root',
        'MC_defaultAK4_2-106.root',
        'MC_defaultAK4_2-107.root',
        'MC_defaultAK4_2-108.root',
        'MC_defaultAK4_2-109.root',
        'MC_defaultAK4_2-11.root',
        'MC_defaultAK4_2-110.root',
        'MC_defaultAK4_2-111.root',
        'MC_defaultAK4_2-112.root',
        'MC_defaultAK4_2-113.root',
        'MC_defaultAK4_2-114.root',
        'MC_defaultAK4_2-115.root',
        'MC_defaultAK4_2-116.root',
        'MC_defaultAK4_2-117.root',
        'MC_defaultAK4_2-118.root',
        'MC_defaultAK4_2-119.root',
        'MC_defaultAK4_2-12.root',
        'MC_defaultAK4_2-120.root',
        'MC_defaultAK4_2-121.root',
        'MC_defaultAK4_2-122.root',
        'MC_defaultAK4_2-123.root',
        'MC_defaultAK4_2-124.root',
        'MC_defaultAK4_2-125.root',
        'MC_defaultAK4_2-126.root',
        'MC_defaultAK4_2-127.root',
        'MC_defaultAK4_2-128.root',
        'MC_defaultAK4_2-129.root',
        'MC_defaultAK4_2-13.root',
        'MC_defaultAK4_2-130.root',
        'MC_defaultAK4_2-14.root',
        'MC_defaultAK4_2-15.root',
        'MC_defaultAK4_2-16.root',
        'MC_defaultAK4_2-17.root',
        'MC_defaultAK4_2-18.root',
        'MC_defaultAK4_2-19.root',
        'MC_defaultAK4_2-2.root',
        'MC_defaultAK4_2-20.root',
        'MC_defaultAK4_2-21.root',
        'MC_defaultAK4_2-22.root',
        'MC_defaultAK4_2-23.root',
        'MC_defaultAK4_2-24.root',
        'MC_defaultAK4_2-25.root',
        'MC_defaultAK4_2-26.root',
        'MC_defaultAK4_2-27.root',
        'MC_defaultAK4_2-28.root',
        'MC_defaultAK4_2-29.root',
        'MC_defaultAK4_2-3.root',
        'MC_defaultAK4_2-30.root',
        'MC_defaultAK4_2-31.root',
        'MC_defaultAK4_2-32.root',
        'MC_defaultAK4_2-33.root',
        'MC_defaultAK4_2-34.root',
        'MC_defaultAK4_2-35.root',
        'MC_defaultAK4_2-36.root',
        'MC_defaultAK4_2-37.root',
        'MC_defaultAK4_2-38.root',
        'MC_defaultAK4_2-39.root',
        'MC_defaultAK4_2-4.root',
        'MC_defaultAK4_2-40.root',
        'MC_defaultAK4_2-41.root',
        'MC_defaultAK4_2-42.root',
        'MC_defaultAK4_2-43.root',
        'MC_defaultAK4_2-44.root',
        'MC_defaultAK4_2-45.root',
        'MC_defaultAK4_2-46.root',
        'MC_defaultAK4_2-47.root',
        'MC_defaultAK4_2-48.root',
        'MC_defaultAK4_2-49.root',
        'MC_defaultAK4_2-5.root',
        'MC_defaultAK4_2-50.root',
        'MC_defaultAK4_2-51.root',
        'MC_defaultAK4_2-52.root',
        'MC_defaultAK4_2-53.root',
        'MC_defaultAK4_2-54.root',
        'MC_defaultAK4_2-55.root',
        'MC_defaultAK4_2-56.root',
        'MC_defaultAK4_2-57.root',
        'MC_defaultAK4_2-58.root',
        'MC_defaultAK4_2-59.root',
        'MC_defaultAK4_2-6.root',
        'MC_defaultAK4_2-60.root',
        'MC_defaultAK4_2-61.root',
        'MC_defaultAK4_2-62.root',
        'MC_defaultAK4_2-63.root',
        'MC_defaultAK4_2-64.root',
        'MC_defaultAK4_2-65.root',
        'MC_defaultAK4_2-66.root',
        'MC_defaultAK4_2-67.root',
        'MC_defaultAK4_2-68.root',
        'MC_defaultAK4_2-69.root',
        'MC_defaultAK4_2-7.root',
        'MC_defaultAK4_2-70.root',
        'MC_defaultAK4_2-71.root',
        'MC_defaultAK4_2-72.root',
        'MC_defaultAK4_2-73.root',
        'MC_defaultAK4_2-74.root',
        'MC_defaultAK4_2-75.root',
        'MC_defaultAK4_2-76.root',
        'MC_defaultAK4_2-77.root',
        'MC_defaultAK4_2-78.root',
        'MC_defaultAK4_2-79.root',
        'MC_defaultAK4_2-8.root',
        'MC_defaultAK4_2-80.root',
        'MC_defaultAK4_2-81.root',
        'MC_defaultAK4_2-82.root',
        'MC_defaultAK4_2-83.root',
        'MC_defaultAK4_2-84.root',
        'MC_defaultAK4_2-85.root',
        'MC_defaultAK4_2-86.root',
        'MC_defaultAK4_2-87.root',
        'MC_defaultAK4_2-88.root',
        'MC_defaultAK4_2-89.root',
        'MC_defaultAK4_2-9.root',
        'MC_defaultAK4_2-90.root',
        'MC_defaultAK4_2-91.root',
        'MC_defaultAK4_2-92.root',
        'MC_defaultAK4_2-93.root',
        'MC_defaultAK4_2-94.root',
        'MC_defaultAK4_2-95.root',
        'MC_defaultAK4_2-96.root',
        'MC_defaultAK4_2-97.root',
        'MC_defaultAK4_2-98.root',
        'MC_defaultAK4_2-99.root',
        'MC_defaultAK4_2.root',
        'MC_defaultAK4_20.root',
        'MC_defaultAK4_200.root',
        'MC_defaultAK4_201.root',
        'MC_defaultAK4_202.root',
        'MC_defaultAK4_203.root',
        'MC_defaultAK4_204.root',
        'MC_defaultAK4_205.root',
        'MC_defaultAK4_207.root',
        'MC_defaultAK4_209.root',
        'MC_defaultAK4_21.root',
        'MC_defaultAK4_210.root',
        'MC_defaultAK4_211.root',
        'MC_defaultAK4_212.root',
        'MC_defaultAK4_213.root',
        'MC_defaultAK4_215.root',
        'MC_defaultAK4_216.root',
        'MC_defaultAK4_217.root',
        'MC_defaultAK4_218.root',
        'MC_defaultAK4_219.root',
        'MC_defaultAK4_22.root',
        'MC_defaultAK4_220.root',
        'MC_defaultAK4_221.root',
        'MC_defaultAK4_222.root',
        'MC_defaultAK4_223.root',
        'MC_defaultAK4_224.root',
        'MC_defaultAK4_225.root',
        'MC_defaultAK4_226.root',
        'MC_defaultAK4_227.root',
        'MC_defaultAK4_228.root',
        'MC_defaultAK4_229.root',
        'MC_defaultAK4_23.root',
        'MC_defaultAK4_230.root',
        'MC_defaultAK4_231.root',
        'MC_defaultAK4_232.root',
        'MC_defaultAK4_233.root',
        'MC_defaultAK4_234.root',
        'MC_defaultAK4_235.root',
        'MC_defaultAK4_236.root',
        'MC_defaultAK4_237.root',
        'MC_defaultAK4_238.root',
        'MC_defaultAK4_239.root',
        'MC_defaultAK4_24.root',
        'MC_defaultAK4_240.root',
        'MC_defaultAK4_241.root',
        'MC_defaultAK4_242.root',
        'MC_defaultAK4_243.root',
        'MC_defaultAK4_244.root',
        'MC_defaultAK4_245.root',
        'MC_defaultAK4_246.root',
        'MC_defaultAK4_247.root',
        'MC_defaultAK4_248.root',
        'MC_defaultAK4_249.root',
        'MC_defaultAK4_25.root',
        'MC_defaultAK4_250.root',
        'MC_defaultAK4_251.root',
        'MC_defaultAK4_252.root',
        'MC_defaultAK4_253.root',
        'MC_defaultAK4_254.root',
        'MC_defaultAK4_255.root',
        'MC_defaultAK4_256.root',
        'MC_defaultAK4_257.root',
        'MC_defaultAK4_258.root',
        'MC_defaultAK4_259.root',
        'MC_defaultAK4_26.root',
        'MC_defaultAK4_260.root',
        'MC_defaultAK4_261.root',
        'MC_defaultAK4_262.root',
        'MC_defaultAK4_263.root',
        'MC_defaultAK4_268.root',
        'MC_defaultAK4_269.root',
        'MC_defaultAK4_27.root',
        'MC_defaultAK4_270.root',
        'MC_defaultAK4_271.root',
        'MC_defaultAK4_272.root',
        'MC_defaultAK4_273.root',
        'MC_defaultAK4_274.root',
        'MC_defaultAK4_275.root',
        'MC_defaultAK4_276.root',
        'MC_defaultAK4_277.root',
        'MC_defaultAK4_278.root',
        'MC_defaultAK4_279.root',
        'MC_defaultAK4_28.root',
        'MC_defaultAK4_280.root',
        'MC_defaultAK4_281.root',
        'MC_defaultAK4_282.root',
        'MC_defaultAK4_283.root',
        'MC_defaultAK4_284.root',
        'MC_defaultAK4_285.root',
        'MC_defaultAK4_286.root',
        'MC_defaultAK4_287.root',
        'MC_defaultAK4_288.root',
        'MC_defaultAK4_289.root',
        'MC_defaultAK4_29.root',
        'MC_defaultAK4_290.root',
        'MC_defaultAK4_291.root',
        'MC_defaultAK4_292.root',
        'MC_defaultAK4_293.root',
        'MC_defaultAK4_294.root',
        'MC_defaultAK4_295.root',
        'MC_defaultAK4_296.root',
        'MC_defaultAK4_297.root',
        'MC_defaultAK4_298.root',
        'MC_defaultAK4_299.root',
        'MC_defaultAK4_3-1.root',
        'MC_defaultAK4_3-10.root',
        'MC_defaultAK4_3-100.root',
        'MC_defaultAK4_3-101.root',
        'MC_defaultAK4_3-102.root',
        'MC_defaultAK4_3-103.root',
        'MC_defaultAK4_3-104.root',
        'MC_defaultAK4_3-105.root',
        'MC_defaultAK4_3-106.root',
        'MC_defaultAK4_3-107.root',
        'MC_defaultAK4_3-108.root',
        'MC_defaultAK4_3-109.root',
        'MC_defaultAK4_3-11.root',
        'MC_defaultAK4_3-110.root',
        'MC_defaultAK4_3-111.root',
        'MC_defaultAK4_3-112.root',
        'MC_defaultAK4_3-113.root',
        'MC_defaultAK4_3-114.root',
        'MC_defaultAK4_3-115.root',
        'MC_defaultAK4_3-116.root',
        'MC_defaultAK4_3-117.root',
        'MC_defaultAK4_3-118.root',
        'MC_defaultAK4_3-119.root',
        'MC_defaultAK4_3-12.root',
        'MC_defaultAK4_3-120.root',
        'MC_defaultAK4_3-121.root',
        'MC_defaultAK4_3-122.root',
        'MC_defaultAK4_3-123.root',
        'MC_defaultAK4_3-124.root',
        'MC_defaultAK4_3-125.root',
        'MC_defaultAK4_3-126.root',
        'MC_defaultAK4_3-127.root',
        'MC_defaultAK4_3-128.root',
        'MC_defaultAK4_3-129.root',
        'MC_defaultAK4_3-13.root',
        'MC_defaultAK4_3-130.root',
        'MC_defaultAK4_3-131.root',
        'MC_defaultAK4_3-132.root',
        'MC_defaultAK4_3-133.root',
        'MC_defaultAK4_3-134.root',
        'MC_defaultAK4_3-135.root',
        'MC_defaultAK4_3-136.root',
        'MC_defaultAK4_3-137.root',
        'MC_defaultAK4_3-138.root',
        'MC_defaultAK4_3-139.root',
        'MC_defaultAK4_3-14.root',
        'MC_defaultAK4_3-140.root',
        'MC_defaultAK4_3-141.root',
        'MC_defaultAK4_3-142.root',
        'MC_defaultAK4_3-143.root',
        'MC_defaultAK4_3-144.root',
        'MC_defaultAK4_3-145.root',
        'MC_defaultAK4_3-146.root',
        'MC_defaultAK4_3-147.root',
        'MC_defaultAK4_3-148.root',
        'MC_defaultAK4_3-149.root',
        'MC_defaultAK4_3-15.root',
        'MC_defaultAK4_3-150.root',
        'MC_defaultAK4_3-151.root',
        'MC_defaultAK4_3-152.root',
        'MC_defaultAK4_3-153.root',
        'MC_defaultAK4_3-154.root',
        'MC_defaultAK4_3-155.root',
        'MC_defaultAK4_3-156.root',
        'MC_defaultAK4_3-157.root',
        'MC_defaultAK4_3-158.root',
        'MC_defaultAK4_3-159.root',
        'MC_defaultAK4_3-16.root',
        'MC_defaultAK4_3-160.root',
        'MC_defaultAK4_3-161.root',
        'MC_defaultAK4_3-162.root',
        'MC_defaultAK4_3-163.root',
        'MC_defaultAK4_3-164.root',
        'MC_defaultAK4_3-165.root',
        'MC_defaultAK4_3-166.root',
        'MC_defaultAK4_3-167.root',
        'MC_defaultAK4_3-168.root',
        'MC_defaultAK4_3-169.root',
        'MC_defaultAK4_3-17.root',
        'MC_defaultAK4_3-170.root',
        'MC_defaultAK4_3-171.root',
        'MC_defaultAK4_3-172.root',
        'MC_defaultAK4_3-173.root',
        'MC_defaultAK4_3-174.root',
        'MC_defaultAK4_3-175.root',
        'MC_defaultAK4_3-176.root',
        'MC_defaultAK4_3-177.root',
        'MC_defaultAK4_3-178.root',
        'MC_defaultAK4_3-179.root',
        'MC_defaultAK4_3-18.root',
        'MC_defaultAK4_3-180.root',
        'MC_defaultAK4_3-181.root',
        'MC_defaultAK4_3-182.root',
        'MC_defaultAK4_3-183.root',
        'MC_defaultAK4_3-184.root',
        'MC_defaultAK4_3-185.root',
        'MC_defaultAK4_3-186.root',
        'MC_defaultAK4_3-187.root',
        'MC_defaultAK4_3-188.root',
        'MC_defaultAK4_3-189.root',
        'MC_defaultAK4_3-19.root',
        'MC_defaultAK4_3-190.root',
        'MC_defaultAK4_3-191.root',
        'MC_defaultAK4_3-192.root',
        'MC_defaultAK4_3-193.root',
        'MC_defaultAK4_3-194.root',
        'MC_defaultAK4_3-195.root',
        'MC_defaultAK4_3-2.root',
        'MC_defaultAK4_3-20.root',
        'MC_defaultAK4_3-21.root',
        'MC_defaultAK4_3-22.root',
        'MC_defaultAK4_3-23.root',
        'MC_defaultAK4_3-24.root',
        'MC_defaultAK4_3-25.root',
        'MC_defaultAK4_3-26.root',
        'MC_defaultAK4_3-27.root',
        'MC_defaultAK4_3-28.root',
        'MC_defaultAK4_3-29.root',
        'MC_defaultAK4_3-3.root',
        'MC_defaultAK4_3-30.root',
        'MC_defaultAK4_3-31.root',
        'MC_defaultAK4_3-32.root',
        'MC_defaultAK4_3-33.root',
        'MC_defaultAK4_3-34.root',
        'MC_defaultAK4_3-35.root',
        'MC_defaultAK4_3-36.root',
        'MC_defaultAK4_3-37.root',
        'MC_defaultAK4_3-38.root',
        'MC_defaultAK4_3-39.root',
        'MC_defaultAK4_3-4.root',
        'MC_defaultAK4_3-40.root',
        'MC_defaultAK4_3-41.root',
        'MC_defaultAK4_3-42.root',
        'MC_defaultAK4_3-43.root',
        'MC_defaultAK4_3-44.root',
        'MC_defaultAK4_3-45.root',
        'MC_defaultAK4_3-46.root',
        'MC_defaultAK4_3-47.root',
        'MC_defaultAK4_3-48.root',
        'MC_defaultAK4_3-49.root',
        'MC_defaultAK4_3-5.root',
        'MC_defaultAK4_3-50.root',
        'MC_defaultAK4_3-51.root',
        'MC_defaultAK4_3-52.root',
        'MC_defaultAK4_3-53.root',
        'MC_defaultAK4_3-54.root',
        'MC_defaultAK4_3-55.root',
        'MC_defaultAK4_3-56.root',
        'MC_defaultAK4_3-57.root',
        'MC_defaultAK4_3-58.root',
        'MC_defaultAK4_3-59.root',
        'MC_defaultAK4_3-6.root',
        'MC_defaultAK4_3-60.root',
        'MC_defaultAK4_3-61.root',
        'MC_defaultAK4_3-62.root',
        'MC_defaultAK4_3-63.root',
        'MC_defaultAK4_3-64.root',
        'MC_defaultAK4_3-65.root',
        'MC_defaultAK4_3-66.root',
        'MC_defaultAK4_3-67.root',
        'MC_defaultAK4_3-68.root',
        'MC_defaultAK4_3-69.root',
        'MC_defaultAK4_3-7.root',
        'MC_defaultAK4_3-70.root',
        'MC_defaultAK4_3-71.root',
        'MC_defaultAK4_3-72.root',
        'MC_defaultAK4_3-73.root',
        'MC_defaultAK4_3-74.root',
        'MC_defaultAK4_3-75.root',
        'MC_defaultAK4_3-76.root',
        'MC_defaultAK4_3-77.root',
        'MC_defaultAK4_3-78.root',
        'MC_defaultAK4_3-79.root',
        'MC_defaultAK4_3-8.root',
        'MC_defaultAK4_3-80.root',
        'MC_defaultAK4_3-81.root',
        'MC_defaultAK4_3-82.root',
        'MC_defaultAK4_3-83.root',
        'MC_defaultAK4_3-84.root',
        'MC_defaultAK4_3-85.root',
        'MC_defaultAK4_3-86.root',
        'MC_defaultAK4_3-87.root',
        'MC_defaultAK4_3-88.root',
        'MC_defaultAK4_3-89.root',
        'MC_defaultAK4_3-9.root',
        'MC_defaultAK4_3-90.root',
        'MC_defaultAK4_3-91.root',
        'MC_defaultAK4_3-92.root',
        'MC_defaultAK4_3-93.root',
        'MC_defaultAK4_3-94.root',
        'MC_defaultAK4_3-95.root',
        'MC_defaultAK4_3-96.root',
        'MC_defaultAK4_3-97.root',
        'MC_defaultAK4_3-98.root',
        'MC_defaultAK4_3-99.root',
        'MC_defaultAK4_3.root',
        'MC_defaultAK4_30.root',
        'MC_defaultAK4_300.root',
        'MC_defaultAK4_301.root',
        'MC_defaultAK4_305.root',
        'MC_defaultAK4_307.root',
        'MC_defaultAK4_309.root',
        'MC_defaultAK4_31.root',
        'MC_defaultAK4_310.root',
        'MC_defaultAK4_311.root',
        'MC_defaultAK4_312.root',
        'MC_defaultAK4_313.root',
        'MC_defaultAK4_314.root',
        'MC_defaultAK4_315.root',
        'MC_defaultAK4_32.root',
        'MC_defaultAK4_33.root',
        'MC_defaultAK4_38.root',
        'MC_defaultAK4_4.root',
        'MC_defaultAK4_42.root',
        'MC_defaultAK4_43.root',
        'MC_defaultAK4_44.root',
        'MC_defaultAK4_45.root',
        'MC_defaultAK4_46.root',
        'MC_defaultAK4_47.root',
        'MC_defaultAK4_48.root',
        'MC_defaultAK4_49.root',
        'MC_defaultAK4_5.root',
        'MC_defaultAK4_50.root',
        'MC_defaultAK4_51.root',
        'MC_defaultAK4_52.root',
        'MC_defaultAK4_53.root',
        'MC_defaultAK4_54.root',
        'MC_defaultAK4_55.root',
        'MC_defaultAK4_56.root',
        'MC_defaultAK4_57.root',
        'MC_defaultAK4_58.root',
        'MC_defaultAK4_59.root',
        'MC_defaultAK4_6.root',
        'MC_defaultAK4_60.root',
        'MC_defaultAK4_61.root',
        'MC_defaultAK4_62.root',
        'MC_defaultAK4_63.root',
        'MC_defaultAK4_64.root',
        'MC_defaultAK4_65.root',
        'MC_defaultAK4_66.root',
        'MC_defaultAK4_67.root',
        'MC_defaultAK4_68.root',
        'MC_defaultAK4_69.root',
        'MC_defaultAK4_7.root',
        'MC_defaultAK4_8.root',
        'MC_defaultAK4_9.root',
        'MC_defaultAK4_95.root',
        'MC_defaultAK4_96.root',
        'MC_defaultAK4_97.root',
        'MC_defaultAK4_98.root',
        'MC_defaultAK4_99.root',
    ),
)