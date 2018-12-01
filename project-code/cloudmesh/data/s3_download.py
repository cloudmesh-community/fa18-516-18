import boto3

from cloudmesh.data import aws_setup


def download_file(bucketname, filename):
    session = boto3.Session(aws_access_key_id=aws_setup.dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                            aws_secret_access_key=aws_setup.dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
    s3 = session.resource('s3')
    bucket_name = s3.Bucket(bucketname)
    bucket_name.download_file(filename, aws_setup.dataMap['local_directory']+filename)


#download_file('xyz2.txt')