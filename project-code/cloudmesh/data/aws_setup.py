import yaml
#import os
from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver


with open('cloudmesh-data.yaml', 'r') as f:
    dataMap = yaml.safe_load(f)

cls = get_driver(Provider.S3_US_EAST2)
driver = cls(dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                    dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
container = driver.get_container(container_name=dataMap['cloud']['aws']['bucket_name'])



