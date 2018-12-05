from cloudmesh_data.data.provider.DataProviderABC import DataProviderABC
import os
import shutil
from os import listdir
from os.path import isfile, join
import pathlib


class LocalProvider(DataProviderABC):
    name = "local"

    def __init__(self, cloud=None):
        if cloud is None:
            self.cloud = "local"
        else:
            self.cloud = cloud

    def authenticate(self, config):
        pass

    def delete(self, filename):
        os.remove(filename)

    def copy(self, source, destination):
        s = os.path.expanduser(source)
        d = os.path.expanduser(destination)
        shutil.copyfile(s, d)

    def move(self, source, destination):
        os.rename(source, destination)

    def download(self, source):
        pass

    def upload(self, source):
        pass

    def list(self, path):
        files = [f for f in listdir(path) if isfile(join(path, f))]
        return files

    def create(self, path, dir=True):
        _path = os.path.expanduser(path)
        if dir:
            pathlib.Path(_path).mkdir(parents=True, exist_ok=True)
        else:
            try:
                file = open(_path, 'r')
                file.close()
            except FileNotFoundError:
                file = open(_path, 'w')
                file.close()

        return _path

    def exists(self, path):
        _path = os.path.expanduser(path)
        return os.path.exists(_path)
