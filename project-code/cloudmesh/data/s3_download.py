import boto3

import yaml
import os

from cloudmesh.data import aws_setup

prefix_path = "/home/richa/fa18-516-18/project-code/cloudmesh/"
target_path = open('cloudmesh-data.yaml', 'w')
file_array = [f for f in os.listdir(prefix_path) if f.endswith('.yaml')]
file_array.sort()  # file is sorted list

file_array = [os.path.join(prefix_path, name) for name in file_array]
for filename in file_array:
    with open(filename, 'r') as f:
        dataMap = yaml.safe_load(f)


def download_file(bucketname, filename):
    session = boto3.Session(aws_access_key_id=aws_setup.dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                            aws_secret_access_key=aws_setup.dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
    s3 = session.resource('s3')
    bucket_name = s3.Bucket(bucketname)
    bucket_name.download_file(filename, dataMap['local_directory']+filename)


#download_file('xyz2.txt')