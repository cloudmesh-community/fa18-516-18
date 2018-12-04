import boto3
from cloudmesh.deprecated import aws_setup


class S3(object):

    #
    # bug datamap is not done right it should be config
    #

    def __init__(self, cloud):
        self.session = boto3.Session(
            aws_access_key_id=aws_setup.dataMap['cloud'][cloud]['credentials']['S3_ACCESS_ID'],
            aws_secret_access_key=aws_setup.dataMap['cloud'][cloud]['credentials']['S3_SECRET_KEY'])
        self.s3 = self.session.resource('s3')
        #
        # BUG: where is bucketname comming from
        #
        bucketname = "ERROR"  # BUG BUG BUG
        self.bucket_name = self.s3.Bucket(bucketname)


    def delete_file(self, bucketname, filename):
        self.bucket_name.delete_key(filename)

    def list_objects(self, bucketname):
        your_bucket = self.s3.Bucket(bucketname)
        keys = []
        for s3_file in your_bucket.objects.all():
            keys.append(s3_file.key)

        return keys

    def download_file(self, bucketname, filename):
        bucket_name = self.s3.Bucket(bucketname)
        file_path = aws_setup.dataMap['local_directory'] + filename
        bucket_name.download_file(filename, file_path)
        return file_path

    def upload_file(self, bucketname, filename):
        with open(aws_setup.dataMap['local_directory'] + filename, 'rb') as iterator:
            obj = aws_setup.driver.upload_object_via_stream(
                iterator=iterator,
                container=aws_setup.driver.get_container(container_name=bucketname),
                object_name=filename)
            print('File {} uploaded to {}.'.format(
                aws_setup.dataMap['local_directory'] + filename,
                filename))

#
# BUG: Create proper example for testing
#
# upload_file('xyz2.txt')
# path = download_file('richa-516', 'MapReduce.docx')
# print(path)
