#from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from googleapiclient import discovery
from google.cloud import storage
import os
import logging
from cloudmesh_data.data.provider.DataProviderABC import DataProviderABC
from cloudmesh_data.data.Config import Config

# BUG: from pypi

# Note: oauth2client is now deprecated. No more features will be added to the
# libraries and the core team is turning down support. We recommend you use google-auth and oauthlib.

#
# this needs review due to bucket name also being returned.
#
from cloudmesh_data.data.provider.local import LocalProvider


class Google(DataProviderABC):

    def __init__(self, cloud=None):
        if cloud is None:
            self.cloud = "google"
        else:
            self.cloud = cloud

        localprovider = LocalProvider()
        self.dir = LocalProvider.create(localprovider, str(os.getcwd()), self.cloud+'dump')

    def authenticate(self):
        logging.basicConfig(filename='debug.log', level=logging.DEBUG)

        config = Config()
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.credentials('google_cloud')['GOOGLE_CLOUD_CREDENTIALS_JSON']

        #
        # Why setting the os environment we have this in config
        #
        self.storage_client = storage.Client()
        return self.storage_client

    def upload(self, bucketname, filename):
        """Uploads a file to the bucket."""
        bucket = self.storage_client.get_bucket(bucketname)
        blob = bucket.blob(filename)
        blob.upload_from_filename(self.config['local_directory'] + filename)
        print('File {} uploaded to {}.'.format(
            self.config['local_directory'] + filename,
            filename))

    def list(self, bucketname):
        bucket = self.storage_client.get_bucket(bucketname)
        blobs = bucket.list_blobs()
        keys = []
        for blob in blobs:
            keys.append(blob.name)

        return keys

    def create(self, bucket_name):
        bucket = self.storage_client.create_bucket(bucket_name)
        print('Bucket {} created.'.format(bucket.name))
        scopes = ['https://www.googleapis.com/auth/devstorage.read_write']
        #credentials = ServiceAccountCredentials.from_json_keyfile_name(
         #   self.config['cloud']['google_cloud']['credentials']['GOOGLE_CLOUD_CREDENTIALS_JSON'], scopes)
        #http_auth = credentials.authorize(Http())
        #return discovery.build('storage', 'v1', http=http_auth)

    def delete(self, bucket_name, blob_name):
        """Deletes a blob from the bucket."""
        bucket = self.storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()
        print('Blob {} deleted.'.format(blob_name))

    # Function to download a file from google cloud
    def download(self, bucketname, filename):
        """Downloads a blob from the bucket."""
        bucket = self.storage_client.get_bucket(bucketname)
        blob = bucket.blob(filename)
        file_path = self.dir + filename
        blob.download_to_filename(file_path)
        # print('Blob {} downloaded to {}.'.format(filename, self.config['local_directory']+filename))
        return file_path

    # Function to download a full dir from google cloud
    def download_dir(self, bucketname, prefix, filename):
        if prefix != '' and filename == '':
            os.mkdir(self.config['local_directory'] + prefix)
            dl_dir = self.config['local_directory'] + prefix

        bucket = self.storage_client.get_bucket(bucketname)
        blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
        for blob in blobs:
            filename = blob.name.replace('/', '_')
            print(filename)
            blob.download_to_filename(dl_dir + filename)  # Download
        return dl_dir

    def copy(self):
        pass

    def move(self):
        pass



