import oyaml as yaml
import os


class Config(object):

    def __init__(self, filename=None):

        #
        # BUG: add if there is a cloudmesh-data.yaml in the current dir use that
        #

        if filename is None:
            filename = os.path.expanduser("~/.cloudmesh/cloudmesh-data.yaml")


        with open(filename, 'r') as f:
            try:
                self.data = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)
                pm = exc.problem_mark
                print("ERROR: {name} has an issue on line {line} at position {column}".format(**pm))

    def credentials(self, cloud):
        return self.data['cloud'][cloud]['credentials']
