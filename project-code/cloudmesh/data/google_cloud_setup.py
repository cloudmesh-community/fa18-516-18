from google.cloud import storage
import os
import yaml
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

prefix_path = "/home/richa/fa18-516-18/project-code/cloudmesh/"
target_path = open('cloudmesh-data.yaml', 'w')
file_array = [f for f in os.listdir(prefix_path) if f.endswith('.yaml')]
file_array.sort()  # file is sorted list

file_array = [os.path.join(prefix_path, name) for name in file_array]

for filename in file_array:
    with open(filename, 'r') as f:
        dataMap = yaml.safe_load(f)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = dataMap['cloud']['google_cloud']['credentials']['GOOGLE_CLOUD_CREDENTIALS_JSON']
storage_client = storage.Client()
# The name for the bucket
bucket_name = dataMap['cloud']['google_cloud']['bucket_name']
