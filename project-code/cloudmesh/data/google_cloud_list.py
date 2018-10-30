import google_cloud_setup

def list_object():
    bucket = google_cloud_setup.storage_client.get_bucket(google_cloud_setup.bucket_name)
    blobs = bucket.list_blobs()
    keys = []
    for blob in blobs:
        #print(blob.name)
        keys.append("gc://"+google_cloud_setup.bucket_name+"/"+blob.name)

    return keys

