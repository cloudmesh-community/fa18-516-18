"""Data Manager.

Usage:
  cmdata test
  cmdata set provider=PROVIDER
  cmdata set dir=BUCKET
  cmdata data add PROVIDER BUCKETNAME FILE
  cmdata data get PROVIDER BUCKETNAME FILE
  cmdata data ls PROVIDER BUCKETNAME
  cmdata data copy FILE PROVIDER PROVIDER_BUCKET DEST DEST_BUCKET
  cmdata data del FILE
  cmdata set group=GROUP
  cmdata set role=ROLE
  cmdata set host=HOSTNAME
  cmdata set cluster=CLUSTERNAME
  cmdata set experiment=EXPERIMENT
  cmdata (-h | --help)
  cmdata --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --config      Location of a cmdata.yaml file
  --vm_list=<list_of_vms>  List of VMs separated by commas ex: node-1,node-2

Description:
   put a description here

Example:
   put an example here
"""
from docopt import docopt

from cloudmesh.file import get_files
from cloudmesh.file import upload_file_by_name
from cloudmesh.file import get_file_by_name
from pprint import pprint

def main():
    """
    Main function for the Data Manager. Processes the input arguments.
    """
    version = 1.0
    arguments = docopt(__doc__, version=version)
    if arguments['data'] and arguments['add']:
        provider = arguments['PROVIDER']
        bucketname = arguments['BUCKETNAME']
        file = arguments['FILE']
        upload_file_by_name(provider, bucketname, file)

    elif arguments['data'] and arguments['get']:
        provider = arguments['PROVIDER']
        bucketname = arguments['BUCKETNAME']
        file = arguments['FILE']
        get_file_by_name(provider, bucketname, file)

    elif arguments['data'] and arguments['ls']:
        provider = arguments['PROVIDER']
        bucket = arguments['BUCKETNAME']
        files = get_files(provider, bucket)
        pprint(files)

    elif arguments['data'] and arguments['copy']:
        file = arguments['FILE']
        source = arguments['PROVIDER']
        sourcebucket = arguments['PROVIDER_BUCKET']
        dest = arguments['DEST']
        destbucket = arguments['DEST_BUCKET']
        if source == dest:
            print("Target cloud needs to different than the source cloud")
            exit
        else:
            get_file_by_name(source, sourcebucket, file)
            upload_file_by_name(dest, destbucket, file)

    elif arguments['test']:
        pprint("Hello!!!!")


if __name__ == "__main__":
    main()