#!flask/bin/python
from flask import Flask
from flask import jsonify
from cloudmesh_data.data.Provider import Provider
from cloudmesh_data.data.Config import Config
from cloudmesh_data.database.mongo import Mongo

app = Flask(__name__)


@app.route("/files", methods=["GET"])
def get_files(service):
    config = Config()
    kind = config.data[service]['kind']
    provider = Provider(kind)
    provider = provider.get_provider(kind)
    files_list = provider.list(kind, config.data[service]['location'])
    i = 1
    filelist = []
    for value in files_list:
        list = [{'SNo': i, 'Filename': value}]
        i = i + 1
        filelist.append(list)
    return jsonify(results=filelist)


@app.route("/file", methods=["GET"])
def get_file_by_name(service, filename, user_uuid):
    config = Config()
    kind = config.data[service]['kind']
    provider = Provider(kind)
    provider = provider.get_provider(kind)
    file_path = provider.download(kind, config.data[service]['location'], filename)
    mongo = Mongo()
    mongo.save_file_to_db(service, file_path, filename, user_uuid)


@app.route("/file", methods=["POST"])
def upload_file_by_name(service, filename):
    config = Config()
    kind = config.data[service]['kind']
    provider = Provider(kind)
    provider = provider.get_provider(kind)
    provider.upload(kind, config.data[service]['location'], filename)


@app.route("/file/copy", methods=["POST"])
def copy_file(filename, service, dest):
    if service == dest:
        print("Target cloud needs to different than the source cloud")
        exit
    else:
        config = Config()
        kind = config.data[service]['kind']
        provider = Provider(kind)
        provider = provider.get_provider(kind)
        destination = provider.get_provider(dest)
        file_path = provider.download(kind, config.data[service]['location'], filename)
        mongo = Mongo()
        mongo.save_file_to_db(service, file_path, filename)
        destination.upload(kind, config.data[service]['location'], filename)


@app.route("/file/rsync", methods=["POST"])
def rsync_file(filename, source, dest):
    print('')


@app.route("/file/delete", methods=["DELETE"])
def delete_file(service, filename):
    config = Config()
    kind = config.data[service]['kind']
    provider = Provider(kind)
    provider = provider.get_provider(kind)
    provider.delete(kind, config.data[service]['location'], filename)


def update_user_for_file(user_uuid, filename):
    mongo = Mongo()
    mongo.update_user_for_file(user_uuid, filename)


if __name__ == '__main__':
    app.run()
