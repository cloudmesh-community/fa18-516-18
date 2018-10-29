import aws_setup


FILE_PATH = '/home/richa/Documents/abc.txt'


extra = {'meta_data': {
    'owner': 'Richa',
    'created': '2018-10-20'}}

with open(FILE_PATH, 'rb') as iterator:
    obj = aws_setup.driver.upload_object_via_stream(
        iterator=iterator,
        container=aws_setup.container,
        object_name='xyz2.txt',
        extra=extra)