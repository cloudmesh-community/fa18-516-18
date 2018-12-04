from cloudmesh.deprecated import google_cloud_setup
import os


# Function to download a file from google cloud
def download_blob(bucketname, filename):
    """Downloads a blob from the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(bucketname)
    blob = bucket.blob(filename)
    file_path = google_cloud_setup.dataMap['local_directory'] + filename
    blob.download_to_filename(file_path)
    # print('Blob {} downloaded to {}.'.format(filename, google_cloud_setup.dataMap['local_directory']+filename))
    return file_path


# Function to download a full dir from google cloud
def download_dir(bucketname, prefix):
    os.mkdir(google_cloud_setup.dataMap['local_directory'] + prefix)
    dl_dir = google_cloud_setup.dataMap['local_directory'] + prefix
    print(dl_dir)
    bucket = google_cloud_setup.storage_client.get_bucket(bucketname)
    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    for blob in blobs:
        filename = blob.name.replace('/', '_')
        print(filename)
        blob.download_to_filename(dl_dir + filename)  # Download
    return dl_dir

# path = download_dir('richa-cloud-516', 'MapReduce.docx')
