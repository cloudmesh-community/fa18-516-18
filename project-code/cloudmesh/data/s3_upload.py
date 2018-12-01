from cloudmesh.data import aws_setup


def upload_file(bucketname, filename):
    with open(aws_setup.dataMap['local_directory']+filename, 'rb') as iterator:
        obj = aws_setup.driver.upload_object_via_stream(
            iterator=iterator,
            container=aws_setup.driver.get_container(container_name=bucketname),
            object_name=filename)
        print('File {} uploaded to {}.'.format(
            aws_setup.dataMap['local_directory'] + filename,
            filename))

#upload_file('xyz2.txt')
