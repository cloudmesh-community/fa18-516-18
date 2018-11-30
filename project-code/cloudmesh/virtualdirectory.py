
import connexion
import six


#from virtualdirectory_controller import *
#from swagger_server.models.virtualdirectory import Virtualdirectory  # noqa: E501
#from swagger_server import util
#from swagger_server.conf import basic_auth, apikey_auth
from pymongo import MongoClient


client = MongoClient()

db = client['cm']
virtualdirectorys = db['virtualdirectory']


