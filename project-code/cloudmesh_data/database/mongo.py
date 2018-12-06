from mongoengine import *
import datetime
from pymongo import MongoClient
from cloudmesh_data.data.Config import Config
from cloudmesh_data.data.util.retrieve_yaml_definition_properties import generate
from cloudmesh_data.data.util import get_file_size_and_checksum
from cloudmesh_data.database.mongo_tables import File
from cloudmesh_data.database.mongo_tables import User
from cloudmesh_data.database.mongo_tables import Virtualdirectory


class Mongo(object):

    def __init__(self):
        config = Config()
        connect(config.database()['database'], host=config.database()['host'], port=config.database()['port'])

        self.client = MongoClient('localhost', 27017)
        self.db = self.client['mongoengine_test']

        self.filecollection = self.db.get_collection("file")
        self.usercollection = self.db.get_collection("user")
        self.vdircollection = self.db.get_collection("virtualdirectory")

        self.fileproperty = generate("File")
        self.userproperty = generate("User")
        self.vdirproperty = generate("Virtualdirectory")

    def save_file_to_db(self, provider, file_path, filename, user_uuid):
        checksum_value = get_file_size_and_checksum.md5(file_path)
        file_size = get_file_size_and_checksum.file_size(file_path)
        content = open(file_path, 'rb')

        file = File(
            name=filename,
            endpoint=provider,
            checksum=checksum_value,
            size=file_size,
            timestamp=datetime.datetime.now,
            last_modified=datetime.datetime.now,
            user_uuid=user_uuid
        )
        if filename.endswith('.png'):
            file.file_content.put(content, content_type='image/jpeg')
        elif filename.endswith('.txt') or filename.endswith('.docx'):
            file.file_content.put(content, content_type='text')

        file.save()

    def update_user_for_file(self, user_uuid, filename):
        myquery = {"name": filename}
        newvalues = {"$set": {"user_uuid": user_uuid}}
        self.filecollection.update_one(myquery, newvalues)

    def save_user_to_db(self, profile):
        user = User(
            uuid=profile.get_uuid(),
            username=profile.get_username(),
            group=profile.get_group(),
            role=profile.get_role(),
            resource=profile.get_resource(),
            context=profile.get_context(),
            description=profile.get_description(),
            firstname=profile.get_firstname(),
            lastname=profile.get_lastname(),
            publickey=profile.get_publickey(),
            email=profile.get_email()
        )

        user.save()

    def get_profiles(self):
        return list(self.usercollection.find({}, {'_id': False}))

    def get_profile_by_uuid(self, uuid):
        myquery = {"_id": uuid}

        user = self.usercollection.find(myquery)
        profile = []
        for x in user:
            profile.append(x)

        return profile

    def save_vdir_to_db(self, name, description, host, location):
        vdir = Virtualdirectory(
            name=name,
            description=description,
            host=host,
            location=location,
            protocol='',
            credential=''
        )
        vdir.save()

    def get_all_virtualdirectory(self):
        return list(self.vdircollection.find({}, {'_id': False}))

    def get_virtualdirectory_by_name(self, name):
        myquery = {"_id": name}

        vdir = self.vdircollection.find(myquery)
        profile = []
        for x in vdir:
            profile.append(x)

        return profile


