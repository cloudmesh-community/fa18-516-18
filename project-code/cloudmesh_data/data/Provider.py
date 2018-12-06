from cloudmesh_data.data.provider.DataProvider import DataProvider


class Provider(object):

    def __init__(self, provider=None):
        self.provider = DataProvider(provider)

    def get_provider(self, provider):
        if provider == 'local':
            self.provider = DataProvider(provider)
        elif provider == 'aws':
            self.provider = DataProvider(provider)
        elif provider == 'google':
            pass
        return self.provider
    