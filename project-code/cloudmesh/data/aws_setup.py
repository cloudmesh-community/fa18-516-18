import yaml
import os
from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver

prefix_path = "/home/richa/fa18-516-18/project-code/cloudmesh/"
target_path = open('cloudmesh-data.yaml', 'w')
file_array = [f for f in os.listdir(prefix_path) if f.endswith('.yaml')]
file_array.sort()  # file is sorted list

file_array = [os.path.join(prefix_path, name) for name in file_array]

for filename in file_array:
    with open(filename, 'r') as f:
        dataMap = yaml.safe_load(f)

cls = get_driver(Provider.S3_US_EAST2)
driver = cls(dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                    dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
container = driver.get_container(container_name=dataMap['cloud']['aws']['bucket_name'])



