from cloudmesh_data.data.provider.google import Google
from cloudmesh_data.data.provider.local import LocalProvider
from cloudmesh_data.data.provider.s3 import S3

#
# GVL I do not uderstand why when we identify a type of a provider that is also again a parameter to the declation, this seems not correct
#
class DataProvider(object):

    def __init__(self, kind):
        if kind == "local":
            import cloudmesh_data.data.provider.local
            self.provider = cloudmesh_data.data.Provider.local.LocalProvider
        elif kind == "aws":
            import cloudmesh_data.data.provider.s3
            self.provider = cloudmesh_data.data.Provider.s3.S3
        elif kind == "google":
            import cloudmesh_data.data.provider.google
            self.provider = cloudmesh_data.data.provider.google.Google

    def list(self, provider, location):
        #
        # why is sthis not just
        # return self.provider.list (location)
        # same question for all the other methods
        #
        if provider == "local":
            local = LocalProvider()
            return self.provider.list(local , location)
        elif provider == "aws":
            s3 = S3()
            return self.provider.list(s3, location)
        elif provider == "google":
            google = Google()
            return self.provider.list(google, location)

    def upload(self, provider, location, filename):
        if provider == "local":
            local = LocalProvider()
            return self.provider.upload(local , location, filename)
        elif provider == "aws":
            s3 = S3()
            return self.provider.upload(s3, location, filename)
        elif provider == "google":
            google = Google()
            return self.provider.upload(google, location, filename)

    def download(self, provider, location, filename):
        if provider == "local":
            local = LocalProvider()
            return self.provider.download(local , location, filename)
        elif provider == "aws":
            s3 = S3()
            return self.provider.download(s3, location, filename)
        elif provider == "google":
            google = Google()
            return self.provider.download(google, location, filename)

    def delete(self, provider, location, filename):
        if provider == "local":
            local = LocalProvider()
            return self.provider.delete(local , location, filename)
        elif provider == "aws":
            s3 = S3()
            return self.provider.delete(s3, location, filename)
        elif provider == "google":
            google = Google()
            return self.provider.delete(google, location, filename)

