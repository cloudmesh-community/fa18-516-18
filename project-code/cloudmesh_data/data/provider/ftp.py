from cloudmesh_data.data.provider.DataProviderABC import DataProviderABC


class DataSSHProvider(DataProviderABC):
    name = "ftp"

    def __init__(self, cloud):
        if cloud is None:
            self.cloud = "local"
        else:
            self.cloud = cloud

    def authenticate(self, config):
        pass

    def delete(self, filename):
        pass

    def copy(self, source, destination):
        pass

    def move(self, source, destination):
        pass

    def download(self, source):
        pass

    def upload(self, source):
        pass

    def list(self, dir):
        pass

    def authenticate(self, credentials):
        pass
 
