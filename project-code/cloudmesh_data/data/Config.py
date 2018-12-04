import oyaml as yaml
import os


class Config(object):

    def __init__(self, filename=None):
        if filename is None:
            filename = os.path.expanduser("~/.cloudmesh_data/cloudmesh_data-data.yaml")

        #
        # BUG: add if there is a cloudmesh_data-data.yaml in the current dir use that
        #

        with open(filename, 'r') as f:
            self.config = yaml.safe_load(f)

    def credentials(self, cloud):
        return self.config['cloud'][cloud]['credentials']

