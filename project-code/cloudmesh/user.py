import connexion
import uuid
from pymongo import MongoClient


client = MongoClient()

db = client['cm']
profiles = db['profile']


def get_profile():
    """
    :return: list all the profiles as a list
    """
    # ok
    return list(profiles.find({}, {'_id': False}))


def get_profile_by_uuid(uuid):
    # BUG: does not gurantee more than one with same uuid
    """get_profile_by_uuid
    Returns a general description of a user  # noqa: E501
    :param uuid: uuid of user
    :type id: str
    :rtype: PROFILE
    """
    for element in profiles.find({'uuid': uuid}):
        return (element['uuid'],
                element['username'],
                element['context'],
                element['description'],
                element['firstname'],
                element['lastname'],
                element['publickey'],
                element['email'])


    return Profile(element[0],
                   element[1],
                   element[2],
                   element[3],
                   element[4],
                   element[5],
                   element[6],
                   element[7])

def profiles_get():  # noqa: E501
    """profiles_get
    Returns a list of general description of users  # noqa: E501
    :rtype: List[PROFILE]
    """
    listOfProfile = []
    items = get_profile()
    for element in items:
        listOfProfile.append(Profile(element[0],
                                     element[1],
                                     element[2],
                                     element[3],
                                     element[4],
                                     element[5],
                                     element[6],
                                     element[7]))
    return listOfProfile