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
        for property in file['definitions']['File']['properties']:
            propertyname.append(property)

        return propertyname
    elif type == "User":
        for property in user['definitions']['User']['properties']:
            propertyname.append(property)

        return property


property = generate("File")
i = 0
while i < len(property):
    print(property[i])
    i += 1