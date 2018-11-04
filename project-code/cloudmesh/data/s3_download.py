import boto3

import yaml

from cloudmesh.data import aws_setup

with open('setup.yaml', 'r') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)


def download_file(filename):
    session = boto3.Session(aws_access_key_id=aws_setup.dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                            aws_secret_access_key=aws_setup.dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
    s3 = session.resource('s3')
    bucket_name = s3.Bucket(aws_setup.dataMap['cloud']['aws']['bucket_name'])
    bucket_name.download_file(filename, dataMap['local_directory']+filename)


#download_file('xyz2.txt')