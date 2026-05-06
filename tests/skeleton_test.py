import DirectStiffness as DS

def test_config_device():
    cfg = DS.Config()
    assert cfg.device is not None

def test_structure_creation():
    s = DS.Structure()
    assert s is not None