from abc import ABC, abstractmethod

class DataProvider(ABC):

    provider = "TBD"

    @abstractmethod
    def __init__(self, cloud):
        pass

    @abstractmethod
    def authenticate(self, config):
        pass

    @abstractmethod
    def delete(self,filename):
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
    def authenticate(self, credentials):
        pass

