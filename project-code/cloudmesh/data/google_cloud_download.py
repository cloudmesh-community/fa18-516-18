from cloudmesh.data import google_cloud_setup


def download_blob(bucketname, filename):
    """Downloads a blob from the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(bucketname)
    blob = bucket.blob(filename)
    file_path = google_cloud_setup.dataMap['local_directory']+filename
    blob.download_to_filename(file_path)
    #print('Blob {} downloaded to {}.'.format(filename, google_cloud_setup.dataMap['local_directory']+filename))
    return file_path


#path = download_blob('richa-cloud-516', 'MapReduce.docx')
#print(path)
