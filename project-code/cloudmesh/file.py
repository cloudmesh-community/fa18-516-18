from cloudmesh.data import s3List
from cloudmesh.data import google_cloud_list
from cloudmesh.data import s3_download
from cloudmesh.data import google_cloud_upload
from cloudmesh.data import google_cloud_download
from cloudmesh.data import s3_upload


def get_files(provider, bucketname):
    if provider == 'aws':
        s3List.list_objects(bucketname)
    elif provider == 'google':
        google_cloud_list.list_object(bucketname)


def get_file_by_name(provider, bucketname, filename):
    if provider == 'aws':
        s3_download.download_file(bucketname, filename)
    elif provider == 'google':
        google_cloud_download.download_blob(bucketname, filename)


def upload_file_by_name(provider, bucketname, filename):
    if provider == 'aws':
        s3_upload.upload_file(bucketname, filename)
    elif provider == 'google':
        google_cloud_upload.upload_blob(bucketname, filename)

