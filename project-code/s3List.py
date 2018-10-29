import aws_setup
import boto3

#aws_list = aws_setup.driver.list_container_objects(aws_setup.container)
#print(aws_list)

def list_objects():
    session = boto3.Session(aws_access_key_id=aws_setup.dataMap['cloud']['aws']['credentials']['S3_ACCESS_ID'],
                            aws_secret_access_key=aws_setup.dataMap['cloud']['aws']['credentials']['S3_SECRET_KEY'])
    s3 = session.resource('s3')
    your_bucket = s3.Bucket(aws_setup.dataMap['cloud']['aws']['bucket_name'])
    keys = []
    for s3_file in your_bucket.objects.all():
        # print(s3_file.key)
        keys.append("s3://"+aws_setup.dataMap['cloud']['aws']['bucket_name']+"/"+s3_file.key);

    return keys

