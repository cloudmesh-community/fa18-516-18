from cloudmesh.data import google_cloud_setup


def upload_blob(filename):
    """Uploads a file to the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(google_cloud_setup.bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_filename(google_cloud_setup.dataMap['local_directory']+filename)
    print('File {} uploaded to {}.'.format(
        google_cloud_setup.dataMap['local_directory']+filename,
        filename))



#upload_blob('MapReduce.docx')