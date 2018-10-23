import yaml
import os.path
from gevent import monkey
from libcloud.storage.providers import get_driver
from libcloud.storage.types import Provider
from gevent.pool import Pool
monkey.patch_all()

with open('setup.yaml', 'r') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)

cls = get_driver(Provider.S3_US_EAST2)
driver = cls(dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                    dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
container = driver.get_container(container_name=dataMap['cloud']['aws']['bucket_name'])

def download_obj(container, obj):
    obj = driver.get_object(container_name=container.name,
                            object_name=obj.name)
    filename = os.path.basename(obj.name)
    path = os.path.join(os.path.expanduser('~/Downloads'), filename)
    print('Downloading: %s to %s' % (obj.name, path))
    obj.download(destination_path=path)

containers = driver.list_containers()

jobs = []
pool = Pool(20)

for index, container in enumerate(containers):
    objects = container.list_objects()

    for obj in objects:
        pool.spawn(download_obj, container, obj)

pool.join()
print('Done')


