from google.cloud import storage
import os
import yaml
import logging

logging.basicConfig(filename='debug.log',level=logging.DEBUG)

with open('setup.yaml', 'r') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = dataMap['cloud']['google_cloud']['credentials']['GOOGLE_CLOUD_CREDENTIALS_JSON']
storage_client = storage.Client()
# The name for the bucket
bucket_name = dataMap['cloud']['google_cloud']['bucket_name']
