import boto3

from cloudmesh.data import aws_setup


def download_file(bucketname, filename):
    session = boto3.Session(aws_access_key_id=aws_setup.dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                            aws_secret_access_key=aws_setup.dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
    s3 = session.resource('s3')
    bucket_name = s3.Bucket(bucketname)
    file_path = aws_setup.dataMap['local_directory'] + filename
    bucket_name.download_file(filename, file_path)
    return file_path

# path = download_file('richa-516', 'MapReduce.docx')
# print(path)
