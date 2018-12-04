from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from googleapiclient import discovery

from cloudmesh.data import google_cloud_setup


def create_service(bucket_name):
    bucket = google_cloud_setup.storage_client.create_bucket(bucket_name)
    print('Bucket {} created.'.format(bucket.name))
    scopes = ['https://www.googleapis.com/auth/devstorage.read_write']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        google_cloud_setup.dataMap['cloud']['google_cloud']['credentials']['GOOGLE_CLOUD_CREDENTIALS_JSON'], scopes)
    http_auth = credentials.authorize(Http())
    return discovery.build('storage', 'v1', http=http_auth)

# create_service('test_richa')
