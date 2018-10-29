import google_cloud_setup

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

upload_blob(google_cloud_setup.bucket_name,'/home/richa/Documents/abc.txt','abc.txt')