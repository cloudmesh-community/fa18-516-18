import uuid

from cloudmesh import Profile
from cloudmesh import mongo


def get_profile():
    """
    :return: list all the profiles as a list
    """

    return mongo.get_profiles()


def add_profile(username, group, role, resource, context, description, firstname, lastname, publickey, email):
    uid = str(uuid.uuid4())
    profile = Profile(uid, username, group, role, resource, context, description, firstname, lastname, publickey, email)
    mongo.save_user_to_db(profile)
    return profile


def get_profile_by_uuid(uuid):
    """get_profile_by_uuid
    Returns a general description of a user  # noqa: E501
    :param uuid: uuid of user
    :type id: str
    :rtype: PROFILE
    """
    profile = mongo.get_profile_by_uuid(uuid)
    return profile



