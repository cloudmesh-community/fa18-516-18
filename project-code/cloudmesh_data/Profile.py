class Profile(object):

    def __init__(self,
                 uuid,
                 username,
                 group,
                 role,
                 resource,
                 context,
                 description,
                 firstname,
                 lastname,
                 publickey,
                 email):
        self._uuid = uuid
        self._username = username
        self._group = group
        self._role = role
        self._resource = resource
        self._context = context
        self._description = description
        self._firstname = firstname
        self._lastname = lastname
        self._publickey = publickey
        self._email = email

    def get_uuid(self):
        return self._uuid

    def set_uuid(self, uuid):
        self._uuid = uuid

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = username

    def get_group(self):
        return self._group

    def set_group(self, group):
        self._group = group

    def get_role(self):
        return self._role

    def set_role(self, role):
        self._role = role

    def get_resource(self):
        return self._resource

    def set_resource(self, resource):
        self._resource = resource

    def get_context(self):
        return self._context

    def set_context(self, context):
        self._context = context

    def get_description(self):
        return self._description

    def set_description(self, desciption):
        self._description = desciption

    def get_firstname(self):
        return self._firstname

    def set_firstname(self, firstname):
        self._firstname = firstname

    def get_lastname(self):
        return self._lastname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def get_publickey(self):
        return self._publickey

    def set_publickey(self, publickey):
        self._publickey = publickey

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email



