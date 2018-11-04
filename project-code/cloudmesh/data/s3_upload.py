
import yaml

from cloudmesh.data import aws_setup

with open('setup.yaml', 'r') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)


def upload_file(filename):
    with open(dataMap['local_directory']+filename, 'rb') as iterator:
        obj = aws_setup.driver.upload_object_via_stream(
            iterator=iterator,
            container=aws_setup.container,
            object_name=filename)
        print('File {} uploaded to {}.'.format(
            dataMap['local_directory'] + filename,
            filename))

#upload_file('xyz2.txt')