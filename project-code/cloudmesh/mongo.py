from mongoengine import *
import datetime

from cloudmesh.retrieve_yaml_definition_properties import generate
from cloudmesh import get_file_size_and_checksum

connect('mongoengine_test', host='localhost', port=27017)

fileproperty = generate("File")
i = 0
while i < len(fileproperty):
    #print(fileproperty[i])
    i += 1

userproperty = generate("User")
j = 0
while j < len(userproperty):
    #print(userproperty[j])
    j += 1


class File(Document):
    name = StringField()
    endpoint = StringField()
    checksum = StringField()
    size = StringField()
    timestamp = DateTimeField(default=datetime.datetime.now)


class User(Document):
    uuid = StringField()
    username = StringField()
    group = StringField()
    role = StringField()
    resource = StringField()
    context = StringField()
    description = StringField()
    firstname = StringField()
    lastname = StringField()
    publickey = StringField()
    email = StringField()


def save_file_to_db(provider, file_path, filename):
    checksum_value = get_file_size_and_checksum.md5(file_path)
    file_size = get_file_size_and_checksum.file_size(file_path)
    file = File(
        name=filename,
        endpoint=provider,
        checksum=checksum_value,
        size=file_size
    )

    file.save()


#save_file_to_db('AWS', '/home/richa/Downloads/aws_lambda_10.png', 'aws_lambda_10.png')

