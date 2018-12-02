import yaml
from pprint import pprint

with open('file.yml', 'r') as f:
    # use safe_load instead load
    file = yaml.safe_load(f)

with open('user.yml', 'r') as f:
    # use safe_load instead load
    user = yaml.safe_load(f)

propertyname = []

def generate(type):
    if type == "File":
        for fileproperty in file['definitions']['File']['properties']:
            propertyname.append(fileproperty)

        return propertyname
    elif type == "User":
        for userproperty in user['definitions']['User']['properties']:
            propertyname.append(userproperty)

        return propertyname


#property = generate("User")

