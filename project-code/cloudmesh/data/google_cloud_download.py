from cloudmesh.data import google_cloud_setup


def download_blob(bucketname, filename):
    """Downloads a blob from the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(bucketname)
    blob = bucket.blob(filename)
    blob.download_to_filename(google_cloud_setup.dataMap['local_directory']+filename)
    print('Blob {} downloaded to {}.'.format(filename, google_cloud_setup.dataMap['local_directory']+filename))

#download_blob('yosemite valley lodge stay.pdf')
