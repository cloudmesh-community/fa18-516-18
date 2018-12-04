import boto3

from cloudmesh.data import aws_setup

def delete_file(bucketname, filename):
    session = boto3.Session(aws_access_key_id=aws_setup.dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                            aws_secret_access_key=aws_setup.dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
    s3 = session.resource('s3')
    bucket_name = s3.Bucket(bucketname)
    bucket_name.delete_key(filename)

def list_objects(bucketname):
    session = boto3.Session(aws_access_key_id=aws_setup.dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                            aws_secret_access_key=aws_setup.dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
    s3 = session.resource('s3')
    your_bucket = s3.Bucket(bucketname)
    keys = []
    for s3_file in your_bucket.objects.all():
        keys.append(s3_file.key)

    return keys

def download_file(bucketname, filename):
    session = boto3.Session(aws_access_key_id=aws_setup.dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                            aws_secret_access_key=aws_setup.dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
    s3 = session.resource('s3')
    bucket_name = s3.Bucket(bucketname)
    file_path = aws_setup.dataMap['local_directory'] + filename
    bucket_name.download_file(filename, file_path)
    return file_path

def upload_file(bucketname, filename):
    with open(aws_setup.dataMap['local_directory'] + filename, 'rb') as iterator:
        obj = aws_setup.driver.upload_object_via_stream(
            iterator=iterator,
            container=aws_setup.driver.get_container(container_name=bucketname),
            object_name=filename)
        print('File {} uploaded to {}.'.format(
            aws_setup.dataMap['local_directory'] + filename,
            filename))

# upload_file('xyz2.txt')
# path = download_file('richa-516', 'MapReduce.docx')
# print(path)
