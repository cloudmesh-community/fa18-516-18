from mongoengine import *
import datetime

from retrieve_yaml_definition_properties import generate

connect('mongoengine_test', host='localhost', port=27017)

fileproperty = generate("File")
fileproplen = len(fileproperty)


class File(Document):
    name = StringField()
    endpoint = StringField()
    checksum = StringField()
    size = StringField()
    timestamp = DateTimeField(default=datetime.datetime.now)


file = File(
    name='abc.txt',
    endpoint='AWS',
    checksum='32',
    size='32KB'
)
file.save()

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

user = User(
    uuid='adsdsdsdssad',
    username='test',
    email='abc@gmail.com'
)

user.save()