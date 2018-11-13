"""Data Manager.

Usage:
  cmdata test
  cmdata data add FILE
  cmdata data add SERVICE FILE
  cmdata data get FILE
  cmdata data get FILE DEST_FOLDER
  cmdata data del FILE
  cmdata data move FILE SOURCE DEST
  cmdata data (ls | dir)
  cmdata set cloud=CLOUD
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

from cloudmesh.data import google_cloud_upload, google_cloud_download, listFiles


def main():
    """
    Main function for the Data Manager. Processes the input arguments.
    """
    version = 1.0
    arguments = docopt(__doc__, version=version)
    if arguments['data'] and arguments['add']:
        file = arguments['FILE']
        google_cloud_upload.upload_blob(file)
        print('Hello', file)

    elif arguments['data'] and arguments['get']:
        file = arguments['FILE']
        google_cloud_download.download_blob(file)
        print('File Downloaded')

    elif arguments['data'] and arguments['ls']:
        listFiles.listFiles()

    elif arguments['data'] and arguments['move']:
        file = arguments['FILE']
        source = arguments['SOURCE']
        dest = arguments['DEST']
        print(file, source, dest)

    elif arguments['test']:
        print('Hello Test')


if __name__ == "__main__":
    main()