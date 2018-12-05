#from google.cloud import bigquery
from google.cloud import storage
import yaml


def get_gcs_client():
    with open('cloudmesh-data.yaml', 'r') as f:
        dataMap = yaml.safe_load(f)


    return storage.Client.from_service_account_json(dataMap['cloud']['data']['google_cloud']['credentials']['GOOGLE_CLOUD_CREDENTIALS_JSON']    )


def list_object(bucketname):
    gcs_client = get_gcs_client()

    bucket = gcs_client.get_bucket(bucketname)
    blobs = bucket.list_blobs()
    keys = []
    for blob in blobs:
        keys.append(blob.name)
        print(blob.name)
    return keys


print(list_object('richa-cloud-516'))
