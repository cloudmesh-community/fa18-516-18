from cloudmesh_data.data.Config import Config
from cloudmesh_data.data.util.debug import myself, HEADING
from pprint import pprint

# nosetests -v --nocapture tests/test_config.py


def test_config():
    HEADING(myself())
    config = Config()

    print(config)

    print(config.dict())

    #pprint(config.credentials('local'))

    assert config is not None

    #assert 'cloud' in config.cloud

