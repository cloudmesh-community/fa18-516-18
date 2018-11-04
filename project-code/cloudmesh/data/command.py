"""Data Manager.

Usage:
  cm4 data add FILE
  cm4 data add SERVICE FILE
  cm4 data get FILE
  cm4 data get FILE DEST_FOLDER
  cm4 data del FILE
  cm4 data move source dest FILE
  cm4 data (ls | dir)
  cm4 set cloud=CLOUD
  cm4 set group=GROUP
  cm4 set role=ROLE
  cm4 set host=HOSTNAME
  cm4 set cluster=CLUSTERNAME
  cm4 set experiment=EXPERIMENT
  cm4 (-h | --help)
  cm4 --version

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

from cloudmesh.data import google_cloud_upload, google_cloud_download


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

    if arguments['data'] and arguments['get']:
        file = arguments['FILE']
        google_cloud_download.download_blob(file)

    if arguments['data'] and arguments['move'] and arguments['source'] and arguments['dest']:
        file = arguments['FILE']
        




if __name__ == "__main__":
    main()