from cloudmesh_data.data.Config import Config
from cloudmesh_data.data.util.debug import myself, HEADING
from pprint import pprint

def test_config():
    HEADING(myself())
    config = Config()

    print(config)

    #pprint(config.credentials('local'))

    assert config is not None
    #assert 'cloud' in config.cloud