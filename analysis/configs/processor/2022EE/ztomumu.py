from analysis.configs.processor_config import ProcessorConfig

processor_config = ProcessorConfig(
    lumimask="analysis/data/Cert_Collisions2022_355100_362760_Golden.txt",
    hlt_paths=["IsoMu24", "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8"],
    selection={
        "muon": {
            "pt": 10,
            "abs_eta": 2.4,
            "dxy": 0.5,
            "dz": 1,
            "sip3d": 4,
            "id_wp": "tight",
            "iso_wp": "tight",
        },
        "jet": {
            "pt": 20,
            "abs_eta": 2.5,
            "id": 6,
            "delta_r_lepton": True,
            "veto_maps": True,
        },
    },
)
