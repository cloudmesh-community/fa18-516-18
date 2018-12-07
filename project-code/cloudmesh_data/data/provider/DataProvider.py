from cloudmesh_data.data.provider.google import Google


class DataProvider(object):

    def __init__(self, kind):
        if kind == '':
            import cloudmesh_data.data.provider.local
            self.provider = cloudmesh_data.data.Provider.local.LocalProvider

    def list(self, provider, location):
        if provider == "local":
            import cloudmesh_data.data.provider.local
            self.provider = cloudmesh_data.data.Provider.local.LocalProvider
            print(self.provider)
            return self.provider.list(location)
        elif provider == "aws":
            import cloudmesh_data.data.provider.s3
            self.provider = cloudmesh_data.data.Provider.s3.S3
            print(self.provider)
            return self.provider.list(location)
        elif provider == "google":
            import cloudmesh_data.data.provider.google
            self.provider = cloudmesh_data.data.provider.google.Google
            google = Google()
            return self.provider.list(google, location)

