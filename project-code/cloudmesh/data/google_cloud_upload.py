import google_cloud_setup
import yaml

with open('setup.yaml', 'r') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)

def upload_blob(filename):
    """Uploads a file to the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(google_cloud_setup.bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_filename(dataMap['local_directory']+filename)
    print('File {} uploaded to {}.'.format(
        dataMap['local_directory']+filename,
        filename))
