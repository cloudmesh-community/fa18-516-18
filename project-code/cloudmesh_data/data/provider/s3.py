import boto3
from cloudmesh_data.data.Config import Config
from cloudmesh_data.data.provider.DataProviderABC import DataProviderABC
import os

from cloudmesh_data.data.provider.local import LocalProvider


class S3(DataProviderABC):

    #
    # bug datamap is not done right it should be config
    #

    def __init__(self, cloud):
        if cloud is None:
            self.cloud = "aws"
        else:
            self.cloud = cloud
        config = Config()
        credentials = config.credentials(cloud)
        self.session = boto3.Session(
            aws_access_key_id=credentials['S3_ACCESS_ID'],
            aws_secret_access_key=credentials['S3_SECRET_KEY'])
        self.s3 = self.session.resource('s3')
        localprovider = LocalProvider()
        self.dir = LocalProvider.create(localprovider, str(os.getcwd()), self.cloud + 'dump')

    def authenticate(self, config):
        pass

    def delete(self, bucketname, filename):
        bucket = self.s3.Bucket(bucketname)
        bucket.delete_key(filename)

    def list(self, bucketname):
        bucket = self.s3.Bucket(bucketname)
        keys = []
        for s3_file in bucket.objects.all():
            keys.append(s3_file.key)

        return keys

    def download(self, bucketname, filename):
        bucket = self.s3.Bucket(bucketname)
        file_path = self.dir + filename
        bucket.download_file(filename, file_path)
        return file_path

    def upload(self, bucketname, filename):
        self.s3.upload_file(filename, bucketname, filename)

    def create(self, dir):
        self.s3.create_bucket(Bucket=dir)

    def move(self, source, destination):
        pass

    def copy(self, source, destination):
        pass


