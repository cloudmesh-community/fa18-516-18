import yaml
import os
from pprint import pprint

prefix_path = "../"
file_array = [f for f in os.listdir(prefix_path) if f.endswith('file.yml')]
file_array.sort()  # file is sorted list

file_array = [os.path.join(prefix_path, name) for name in file_array]

for filename in file_array:
    with open(filename, 'r') as f:
        # use safe_load instead load
        file = yaml.safe_load(f)


user_array = [f for f in os.listdir(prefix_path) if f.endswith('user.yml')]
user_array.sort()

user_array = [os.path.join(prefix_path, name) for name in user_array]

for filename in user_array:
    with open(filename, 'r') as f:
        # use safe_load instead load
        user = yaml.safe_load(f)


propertyname = []


def generate(type):
    if type == 'File':
        for fileproperty in file['definitions']['File']['properties']:
            propertyname.append(fileproperty)

        return propertyname
    elif type == "User":
        for userproperty in user['definitions']['User']['properties']:
            propertyname.append(userproperty)

        return propertyname



#property = generate("User")
#print(property)

