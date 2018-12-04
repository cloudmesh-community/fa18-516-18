class DataProvider(object):

    def __init__(self, kind):
        if kind == "local":
            import cloudmesh_data.data.provider.local
            provider = cloudmesh_data.data.provider.local.LocalProvider

    def list(self, path):
        return self.provider.list(path)
