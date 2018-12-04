from cloudmesh_data.deprecated import google_cloud_setup


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    bucket = google_cloud_setup.storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()
    print('Blob {} deleted.'.format(blob_name))

# delete_blob('richa-cloud-516','MapReduce.docx')
