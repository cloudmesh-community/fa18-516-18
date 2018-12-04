import os
import cloudmesh
from cloudmesh import mongo


def add_virtualdirectory(virtualdirname):
    # Create target Directory if don't exist
    if not os.path.exists(virtualdirname):
        os.mkdir(virtualdirname)
        print("Directory ", virtualdirname, " Created ")
    else:
        print("Directory ", virtualdirname, " already exists")

    prefix_path = os.path.dirname(cloudmesh.__file__)
    dir_path = os.path.join(prefix_path, virtualdirname)
    mongo.save_vdir_to_db(virtualdirname, '', str(os.path), str(dir_path))
    return dir_path


def get_virtualdirectory():
    """
    :return: list all the virtualdirectorys as a list
    """
    return mongo.get_all_virtualdirectory()


def get_virtualdirectory_by_name(name):
    return mongo.get_virtualdirectory_by_name(name)

# print(add_virtualdirectory('testDir'))
