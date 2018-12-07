from cloudmesh_data.data.Provider import Provider
from cloudmesh_data.data.Config import Config
from cloudmesh_data.database.mongo import Mongo


def get_provider(service):
    config = Config()
    kind = config['cloud']['data'][service]
    #kind = config['cloud']['data'][service]['kind']
    provider = Provider()
    provider = provider.get_provider(kind)
    return provider


def get_files(service):
    provider = get_provider(service)
    files_list = provider.list(provider["location"])
    return files_list


def get_file_by_name(service, filename, user_uuid):
    provider = get_provider(service)
    file_path = provider.download(provider["location"], filename)
    mongo = Mongo()
    mongo.save_file_to_db(service, file_path, filename, user_uuid)


def upload_file_by_name(service, filename):
    provider = get_provider(service)
    provider.upload(provider["location"], filename)


def copy_file(filename, service, dest):
    if service == dest:
        print("Target cloud needs to different than the source cloud")
        exit
    else:
        provider = get_provider(service)
        destination = get_provider(dest)
        file_path = provider.download(provider["location"], filename)
        mongo = Mongo()
        mongo.save_file_to_db(service, file_path, filename)
        destination.upload(provider["location"], filename)


def rsync_file(filename, source, dest):
    print('')


def delete_file(service, filename):
    provider = get_provider(service)
    provider.delete(provider["location"], filename)


def update_user_for_file(user_uuid, filename):
    mongo = Mongo()
    mongo.update_user_for_file(user_uuid, filename)
