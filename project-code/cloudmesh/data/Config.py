import oyaml as yaml
import os


class Config(object):

    def __init__(self, filename=None):
        if filename is None:
            filename = os.path.expanduser("~/.cloudmesh/cloudmesh-data.yaml")

        #
        # BUG: add if there is a cloudmesh-data.yaml in the current dir use that
        #

        with open(filename, 'r') as f:
            self.config = yaml.safe_load(f)

        return self.config
