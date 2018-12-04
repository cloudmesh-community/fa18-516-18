from cloudmesh_data.data.provider.local import LocalProvider

def test_local_provider_list():
    provider = LocalProvider()
    result = provider.list(".")
    print(result)
    assert 'setup.py' in result