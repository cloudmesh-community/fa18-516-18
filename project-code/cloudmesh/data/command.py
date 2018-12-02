"""Data Manager.

Usage:
  cmdata test
  cmdata set provider=PROVIDER
  cmdata set dir=BUCKET
  cmdata data add PROVIDER BUCKETNAME FILENAME
  cmdata data get PROVIDER BUCKETNAME FILENAME USER_UUID
  cmdata data ls PROVIDER BUCKETNAME
  cmdata data copy FILENAME PROVIDER PROVIDER_BUCKET DEST DEST_BUCKET
  cmdata data rsync FILENAME SOURCE DEST
  cmdata data del PROVIDER BUCKETNAME FILENAME
  cmdata update user USER file FILENAME
  cmdata (-h | --help)
  cmdata --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --config      Location of a cmdata.yaml file
  
Description:
   put a description here

Example:
   put an example here
"""
from docopt import docopt

from cloudmesh.file import get_files
from cloudmesh.file import rsync_file
from cloudmesh.file import delete_file
from cloudmesh.file import copy_file
from cloudmesh.file import upload_file_by_name
from cloudmesh.file import get_file_by_name
from cloudmesh.file import update_user_for_file
from pprint import pprint
from prettytable import PrettyTable


def main():
    """
    Main function for the Data Manager. Processes the input arguments.
    """
    version = 1.0
    arguments = docopt(__doc__, version=version)
    if arguments['data'] and arguments['add']:
        provider = arguments['PROVIDER']
        bucketname = arguments['BUCKETNAME']
        file = arguments['FILENAME']
        upload_file_by_name(provider, bucketname, file)

    elif arguments['data'] and arguments['get']:
        provider = arguments['PROVIDER']
        bucketname = arguments['BUCKETNAME']
        user_uuid = arguments['USER_UUID']
        file = arguments['FILENAME']
        get_file_by_name(provider, bucketname, file, user_uuid)

    elif arguments['data'] and arguments['ls']:
        provider = arguments['PROVIDER']
        bucket = arguments['BUCKETNAME']
        files = get_files(provider, bucket)
        x = PrettyTable(["SNo", "Filename"])
        i=1
        for file in files:
            x.add_row([i, file])
            i = i+1
        print(x)

    elif arguments['data'] and arguments['copy']:
        file = arguments['FILENAME']
        source = arguments['PROVIDER']
        sourcebucket = arguments['PROVIDER_BUCKET']
        dest = arguments['DEST']
        destbucket = arguments['DEST_BUCKET']
        copy_file(file, source, sourcebucket, dest, destbucket)

    elif arguments['data'] and arguments['rsync']:
        source = arguments['SOURCE']
        dest = arguments['DEST']
        filename = arguments['FILENAME']
        rsync_file(filename, source, dest)

    elif arguments['data'] and arguments['del']:
        provider = arguments['PROVIDER']
        bucketname = arguments['BUCKETNAME']
        filename = arguments['FILENAME']
        delete_file(provider, bucketname, filename)

    elif arguments['update'] and arguments['user'] and arguments['file']:
        username = arguments['USER']
        filename = arguments['FILENAME']
        update_user_for_file(username, filename)

    elif arguments['test']:
        pprint("Hello!!!!")


if __name__ == "__main__":
    main()