from deprecated import google_cloud_setup


def upload_blob(bucketname, filename):
    """Uploads a file to the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(bucketname)
    blob = bucket.blob(filename)
    blob.upload_from_filename(google_cloud_setup.dataMap['local_directory'] + filename)
    print('File {} uploaded to {}.'.format(
        google_cloud_setup.dataMap['local_directory'] + filename,
        filename))

# upload_blob('MapReduce.docx')
