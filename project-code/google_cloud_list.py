import google_cloud_setup

def list_object():
    bucket = google_cloud_setup.storage_client.get_bucket(google_cloud_setup.bucket_name)
    blobs = bucket.list_blobs()
    for blob in blobs:
        print(blob.name)


list_object()
