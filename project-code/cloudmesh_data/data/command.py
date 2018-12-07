"""Data Manager.

Usage:
  cmdata data list [--format=FORMAT]
  cmdata set provider=PROVIDER
  cmdata set dir=BUCKET
  cmdata data add PROVIDER FILENAME
  cmdata data get PROVIDER FILENAME USER_UUID
  cmdata data ls PROVIDER
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

   cmdata data get PROVIDER FILENAME USER_UUID

        Description:

Example:
   cmdata test
   cmdata data add AWS richa-516 MapReduce.docx
   cmdata data get AWS richa-516 MapReduce.docx 1234
   cmdata data ls AWS richa-516
   cmdata data copy xyz.txt AWS richa-516 GOOGLE richa-google-516
"""
from docopt import docopt

from cloudmesh_data.data.file import get_files
# from cloudmesh_data.data.file import rsync_file
# from cloudmesh_data.data.file import delete_file
# from cloudmesh_data.data.file import copy_file
from cloudmesh_data.data.file import upload_file_by_name
# from cloudmesh_data.data.file import get_file_by_name
# from cloudmesh_data.data.file import update_user_for_file
from pprint import pprint
from prettytable import PrettyTable
from cloudmesh_data.data.Config import Config


def main():
    """
    Main function for the Data Manager. Processes the input arguments.
    """
    version = 1.0
    arguments = docopt(__doc__, version=version)
    if arguments['data'] and arguments['add']:
        provider = arguments['PROVIDER']
        file = arguments['FILENAME']
        upload_file_by_name(provider, file)

    elif arguments['data'] and arguments['list']:

        output_format = arguments["--format"] or 'table'
        if output_format == "table":
            config = Config()
            print(config.table())

        elif output_format == "yaml":
            config = Config()
            print(config)

    elif arguments['data'] and arguments['get']:
        provider = arguments['PROVIDER']
        bucketname = arguments['BUCKETNAME']
        user_uuid = arguments['USER_UUID']
        file = arguments['FILENAME']
        # get_file_by_name(provider, bucketname, file, user_uuid)

    elif arguments['data'] and arguments['ls']:
        provider = arguments['PROVIDER']
        files = get_files(provider)
        config = Config()
        config.print(files)


    elif arguments['data'] and arguments['copy']:
        file = arguments['FILENAME']
        source = arguments['PROVIDER']
        sourcebucket = arguments['PROVIDER_BUCKET']
        dest = arguments['DEST']
        destbucket = arguments['DEST_BUCKET']
        # copy_file(file, source, sourcebucket, dest, destbucket)

    elif arguments['data'] and arguments['rsync']:
        source = arguments['SOURCE']
        dest = arguments['DEST']
        filename = arguments['FILENAME']
        # rsync_file(filename, source, dest)

    elif arguments['data'] and arguments['del']:
        provider = arguments['PROVIDER']
        bucketname = arguments['BUCKETNAME']
        filename = arguments['FILENAME']
        # delete_file(provider, bucketname, filename)

    elif arguments['update'] and arguments['user'] and arguments['file']:
        username = arguments['USER']
        filename = arguments['FILENAME']
        # update_user_for_file(username, filename)


if __name__ == "__main__":
    main()
