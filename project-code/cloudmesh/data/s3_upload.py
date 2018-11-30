
import yaml

from cloudmesh.data import aws_setup
import os

prefix_path = "/home/richa/fa18-516-18/project-code/cloudmesh/"
target_path = open('cloudmesh-data.yaml', 'w')
file_array = [f for f in os.listdir(prefix_path) if f.endswith('.yaml')]
file_array.sort()  # file is sorted list

file_array = [os.path.join(prefix_path, name) for name in file_array]
for filename in file_array:
    with open(filename, 'r') as f:
        dataMap = yaml.safe_load(f)


def upload_file(bucketname, filename):
    with open(dataMap['local_directory']+filename, 'rb') as iterator:
        obj = aws_setup.driver.upload_object_via_stream(
            iterator=iterator,
            container=aws_setup.driver.get_container(container_name=bucketname),
            object_name=filename)
        print('File {} uploaded to {}.'.format(
            dataMap['local_directory'] + filename,
            filename))

#upload_file('xyz2.txt')