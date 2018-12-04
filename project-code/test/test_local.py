from cloudmesh_data.data.provider.local import LocalProvider
from cloudmesh_data.data.Config import Config
from cloudmesh_data.data.util.debug import myself, HEADING
from pprint import pprint


def test_local_provider_list():
    HEADING(myself())
    provider = LocalProvider()
    result = provider.list(".")
    print(result)
    assert 'setup.py' in result


def test_local_list():
    HEADING(myself())
    config = Config()
    print(config)

    source = config.data['local_a']
    pprint(source)
    destination = config.data['local_b']
    pprint(destination)

    pprint(source["location"])
    pprint(destination["location"])


def test_local_exists():
    HEADING(myself())

    config = Config()
    print(config)

    source = config.data['local_a']
    pprint(source)
    destination = config.data['local_b']
    pprint(destination)

    pprint(source["location"])
    pprint(destination["location"])

    provider = LocalProvider()

    #
    # CREATE DIR
    #

    provider.create(source["location"])
    provider.create(destination["location"])


    #
    # EXISTS
    #

    assert provider.exists(source["location"])
    assert provider.exists(destination["location"])


    #
    # CREATE FILE
    #

    path = source["location"] + "/a.txt"
    print (path)
    provider.create(path, dir=False)
    assert provider.exists(path)

    #
    # COPY FILE
    #

    s_path = source["location"] + "/a.txt"
    d_path = destination["location"] + "/a.txt"
    print (s_path, d_path)
    provider.copy(s_path, d_path)
    assert provider.exists(d_path)
    assert provider.exists(s_path)




#    assert provider.exists(path)


