from mongoengine import *
import datetime

from cloudmesh.retrieve_yaml_definition_properties import generate

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


def save_file_to_db(file_path, filename):
    file = File(
        name='MapReduce2.docx',
        endpoint='Google',
        checksum='32jhgsfjahfkahf',
        size='32KB'
    )

    file.save()


#save_file_to_db()

