from cloudmesh.data import s3List, google_cloud_list, s3_download, google_cloud_upload, google_cloud_download, s3_upload


def get_files(provider):
    if provider == 'aws':
        s3List.list_objects()
    if provider == 'gc':
        google_cloud_list.list_object()


def get_file_by_name(provider, filename):
    if provider == 'aws':
        s3_download.download_file(filename)
    if provider == 'gc':
        google_cloud_download.download_blob(filename)


def upload_file_by_name(provider, filename):
    if provider == 'aws':
        s3_upload.upload_file(filename)
    if provider == 'gc':
        google_cloud_upload.upload_blob(filename)

