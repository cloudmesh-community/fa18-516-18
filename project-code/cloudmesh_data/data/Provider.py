from cloudmesh_data.data.provider.DataProvider import DataProvider


class Provider(object):

    def get_provider(self, provider):
        if provider == 'local':
            provider = DataProvider(provider)
        elif provider == 'aws':
            provider = DataProvider(provider)
        elif provider == 'google':
            provider = DataProvider(provider)
        return provider