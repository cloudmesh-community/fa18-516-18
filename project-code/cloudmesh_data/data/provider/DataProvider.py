class DataProvider(object):

    def __init__(self, provider):
        if provider == "local":
            import cloudmesh_data.data.provider.local
            self.provider = cloudmesh_data.data.Provider.local.LocalProvider
        elif provider == "aws":
            import cloudmesh_data.data.provider.s3
            self.provider = cloudmesh_data.data.Provider.s3.S3
        elif provider == "google":
            import cloudmesh_data.data.provider.google
            self.provider = cloudmesh_data.data.Provider.google.Google

    def list(self, path):
        return self.provider.list(path)
