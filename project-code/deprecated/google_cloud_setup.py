from google.cloud import storage
import os
import yaml
import logging

from cloudmesh_data.data.Config import Config

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

with open('cloudmesh-data.yaml', 'r') as f:
    dataMap = yaml.safe_load(f)

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = dataMap['cloud']['data'['google_cloud']['credentials']['GOOGLE_CLOUD_CREDENTIALS_JSON']
config = Config()
gcs_client = storage.Client.from_service_account_json(config.credentials('google_cloud')['GOOGLE_CLOUD_CREDENTIALS_JSON'])
#storage_client = storage.Client()
# The name for the bucket

# print(bucket_name)
