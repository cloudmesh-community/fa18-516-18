
import yaml

from cloudmesh.data import google_cloud_setup

with open('setup.yaml', 'r') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)


def download_blob(filename):
    """Downloads a blob from the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(google_cloud_setup.bucket_name)
    blob = bucket.blob(filename)
    blob.download_to_filename(dataMap['local_directory']+filename)
    print('Blob {} downloaded to {}.'.format(filename, dataMap['local_directory']+filename))
