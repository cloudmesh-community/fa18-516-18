import oyaml as yaml
import os
from pprint import pprint
from prettytable  import PrettyTable

class Config(object):

    def __init__(self, filename=None):

        #
        # BUG: add if there is a cloudmesh-data.yaml in the current dir use that
        #

        if filename is None:
            filename = os.path.expanduser("~/.cloudmesh/cloudmesh-data.yaml")

        with open(filename, 'r') as f:
            try:
                self.cloud = yaml.safe_load(f)
                self.data = self.cloud['cloud']['data']
            except yaml.YAMLError as exc:
                print(exc)
                pm = exc.problem_mark
                print("ERROR: {name} has an issue on line {line} at position {column}".format(**pm))

    def credentials(self, cloud):
        return self.data[cloud]['credentials']

    def __str__(self):
        return yaml.dump(self.cloud)

    def table(self):

        x = PrettyTable(["No", "Provider", "Kind", "Location"])
        x.align["No"] = "r"
        x.align["Provider"] = "l"
        x.align["Kind"] = "l"
        x.align["Location"] = "l"

        i = 1
        for provider in self.data:
            name = provider
            kind = self.data[provider]["kind"]
            location = self.data[provider]["location"]
            x.add_row([i, name, kind, location])
            i = i + 1

        return x