from cloudmesh_data.deprecated import google_cloud_setup


def list_object(bucketname):
    bucket = google_cloud_setup.storage_client.get_bucket(bucketname)
    blobs = bucket.list_blobs()
    keys = []
    for blob in blobs:
        keys.append(blob.name)

    return keys

# print(list_object('richa-cloud-516'))
