from mongoengine import *
import datetime
from pymongo import MongoClient

from cloudmesh.retrieve_yaml_definition_properties import generate
from cloudmesh import get_file_size_and_checksum

connect('mongoengine_test', host='localhost', port=27017)


client = MongoClient('localhost', 27017)
db = client['mongoengine_test']
filecollection = db.get_collection("file")
usercollection = db.get_collection("user")

#To print all records for file table
#for file in filecollection.find():
 #   print(file)
#To delete all records
#myquery = {}
#filecollection.delete_many(myquery)


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
    name = StringField(primary_key=True)
    endpoint = StringField()
    checksum = StringField()
    size = StringField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    last_modified = DateTimeField(default=datetime.datetime.now)
    user_uuid = StringField()


class User(Document):
    uuid = StringField(primary_key=True)
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


def save_file_to_db(provider, file_path, filename, user_uuid):
    checksum_value = get_file_size_and_checksum.md5(file_path)
    file_size = get_file_size_and_checksum.file_size(file_path)
    file = File(
        name=filename,
        endpoint=provider,
        checksum=checksum_value,
        size=file_size,
        timestamp=datetime.datetime.now,
        last_modified=datetime.datetime.now,
        user_uuid=user_uuid
    )

    file.save()


def update_user_for_file(user_uuid, filename):
    myquery = {"name": filename}
    newvalues = {"$set": {"user_uuid": user_uuid}}
    filecollection.update_one(myquery, newvalues)

    # print "customers" after the update:
    #for x in filecollection.find():
    #   print(x)



#save_file_to_db('AWS', '/home/richa/Downloads/aws_lambda_10.png', 'aws_lambda_10.png', 'richa')

#add_user_for_file('richa', 'test123')

