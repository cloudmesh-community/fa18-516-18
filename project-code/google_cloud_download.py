import google_cloud_setup

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

download_blob(google_cloud_setup.bucket_name,'MapReduce.docx','/home/richa/Documents/MapReduce.docx')

