"""Data Manager.

Usage:
  cmdata data list [--format=FORMAT]
  cmdata set provider=PROVIDER
  cmdata set dir=BUCKET
  cmdata data add PROVIDER FILENAME
  cmdata data get PROVIDER FILENAME USER_UUID
  cmdata data ls PROVIDER
  cmdata data copy FILENAME PROVIDER DEST
  cmdata data rsync FILENAME SOURCE DEST
  cmdata data del PROVIDER FILENAME
  cmdata update user USER file FILENAME
  cmdata (-h | --help)
  cmdata --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --config      Location of a cmdata.yaml file

Description:

    cmdata data ls PROVIDER

        Description: CM command to list all the files in a Provider's bucket

    cmdata data add PROVIDER FILENAME

        Description: CM command to upload a file from local directory to the Provider's bucket

    cmdata data get PROVIDER FILENAME USER_UUID

        Description: CM command to download a file from the Provider's bucket to a local directory
        and then save that file to MongoDB with the username assigned

    cmdata data copy FILENAME PROVIDER DEST

        Description: CM command to copy a file from one Provider's bucket to another

    cmdata data del PROVIDER FILENAME

        Description: CM command to delete a file from a Provider's bucket

Example:
   cmdata data ls google_cloud
   cmdata data add google_cloud abc.txt
   cmdata data get google_cloud abc.txt richa
   cmdata data copy xyz.txt AWS GOOGLE
   cmdata data del google_cloud abc.txt
"""
from docopt import docopt

from cloudmesh_data.data.file import get_files
# from cloudmesh_data.data.file import rsync_file
from cloudmesh_data.data.file import delete_file
from cloudmesh_data.data.file import copy_file
from cloudmesh_data.data.file import upload_file_by_name
from cloudmesh_data.data.file import get_file_by_name
# from cloudmesh_data.data.file import update_user_for_file
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
        user_uuid = arguments['USER_UUID']
        file = arguments['FILENAME']
        get_file_by_name(provider, file, user_uuid)

    elif arguments['data'] and arguments['ls']:
        provider = arguments['PROVIDER']
        files = get_files(provider)
        config = Config()
        config.print(files)

    elif arguments['data'] and arguments['copy']:
        file = arguments['FILENAME']
        source = arguments['PROVIDER']
        dest = arguments['DEST']
        copy_file(file, source, dest)

    elif arguments['data'] and arguments['rsync']:
        source = arguments['SOURCE']
        dest = arguments['DEST']
        filename = arguments['FILENAME']
        # rsync_file(filename, source, dest)

    elif arguments['data'] and arguments['del']:
        provider = arguments['PROVIDER']
        filename = arguments['FILENAME']
        delete_file(provider, filename)

    elif arguments['update'] and arguments['user'] and arguments['file']:
        username = arguments['USER']
        filename = arguments['FILENAME']
        # update_user_for_file(username, filename)


if __name__ == "__main__":
    main()
