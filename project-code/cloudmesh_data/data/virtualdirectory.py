import os
import cloudmesh_data
from cloudmesh_data.database.mongo import Mongo


def add_virtualdirectory(virtualdirname):
    # Create target Directory if don't exist
    if not os.path.exists(virtualdirname):
        os.mkdir(virtualdirname)
        print("Directory ", virtualdirname, " Created ")
    else:
        print("Directory ", virtualdirname, " already exists")

    prefix_path = os.path.dirname(cloudmesh_data.__file__)

    dir_path = os.path.join(os.getcwd(), virtualdirname)
    print(dir_path)
    mongo = Mongo()
    mongo.save_vdir_to_db(virtualdirname, '', str(os.path), str(dir_path))
    return dir_path


def get_virtualdirectory():
    """
    :return: list all the virtualdirectorys as a list
    """
    mongo = Mongo()
    return mongo.get_all_virtualdirectory()


def get_virtualdirectory_by_name(name):
    mongo = Mongo()
    return mongo.get_virtualdirectory_by_name(name)

# print(add_virtualdirectory('testDir'))
