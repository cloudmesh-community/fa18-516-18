from abc import ABC, abstractmethod


class DataProviderABC(ABC):
    name = "TBD"

    @abstractmethod
    def __init__(self, cloud):
        if cloud is None:
            self.cloud = "local"
        else:
            self.cloud = cloud

    @abstractmethod
    def authenticate(self, config):
        pass

    @abstractmethod
    def delete(self, filename):
        pass

    @abstractmethod
    def copy(self, source, destination):
        pass

    @abstractmethod
    def move(self, source, destination):
        pass

    @abstractmethod
    def download(self, source):
        pass

    @abstractmethod
    def upload(self, source):
        pass

    @abstractmethod
    def list(self, dir):
        pass

    @abstractmethod
    def create(self, dir):
        pass
