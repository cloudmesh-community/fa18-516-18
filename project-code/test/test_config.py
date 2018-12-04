from cloudmesh_data.data.Config import Config

def test_config():
    config = Config()

    print(config.data)

    print(config.credentials('local'))

    assert config is not None
    assert 'cloud' in config.data