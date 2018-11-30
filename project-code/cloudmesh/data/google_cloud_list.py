from cloudmesh.data import google_cloud_setup


def list_object(bucketname):
    #bucket = google_cloud_setup.storage_client.get_bucket(google_cloud_setup.bucket_name)
    bucket = google_cloud_setup.storage_client.get_bucket(bucketname)
    blobs = bucket.list_blobs()
    keys = []
    for blob in blobs:
        keys.append(blob.name)

    return keys

