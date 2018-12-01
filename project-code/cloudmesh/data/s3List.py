import boto3

from cloudmesh.data import aws_setup


def list_objects(bucketname):
    session = boto3.Session(aws_access_key_id=aws_setup.dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                            aws_secret_access_key=aws_setup.dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
    s3 = session.resource('s3')
    your_bucket = s3.Bucket(bucketname)
    keys = []
    for s3_file in your_bucket.objects.all():
        keys.append(s3_file.key)

    return keys

