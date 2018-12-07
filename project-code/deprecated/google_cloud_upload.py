from deprecated import google_cloud_setup


def upload_blob(bucketname, filename):
    """Uploads a file to the bucket."""
    #bucket = google_cloud_setup.storage_client.get_bucket(bucketname)
    bucket = google_cloud_setup.gcs_client.get_bucket(bucketname)
    blob = bucket.blob(filename)
    print(blob)
    blob.upload_from_filename(filename)
    #blob.upload_from_filename('/home/richa/fa18-516-18/project-code/googleDump/'+ filename)
    #print('File {} uploaded to {}.'.format('/home/richa/Documents/' + filename, filename))


def upload_blob1(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    #storage_client = storage.Client()
    bucket = google_cloud_setup.gcs_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

upload_blob1('richa-cloud-516', '/home/richa/Documents/MapReduce.docx', 'MapReduce.docx')
