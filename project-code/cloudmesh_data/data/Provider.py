from cloudmesh_data.data.provider.DataProvider import DataProvider


class Provider(object):

    def __init__(self, kind):
        if kind == '':
            self.provider = DataProvider('local')

    def get_provider(self, kind):
        if kind == 'local':
            self.provider = DataProvider(kind)
        elif kind == 'aws':
            self.provider = DataProvider(kind)
        elif kind == 'google':
            self.provider = DataProvider(kind)
        return self.provider
