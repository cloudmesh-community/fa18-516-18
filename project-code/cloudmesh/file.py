from cloudmesh import mongo
from cloudmesh.data import s3
from cloudmesh.deprecated import google_cloud_delete, google_cloud_download, google_cloud_list, google_cloud_upload, \
    s3_delete, s3_download, s3_upload


def get_files(provider, bucketname):
    if provider == 'aws':
        list = s3.list_objects(bucketname)
    elif provider == 'google':
        list = google_cloud_list.list_object(bucketname)

    return list


def get_file_by_name(provider, bucketname, filename, user_uuid):
    if provider == 'aws':
        file_path = s3_download.download_file(bucketname, filename)
        mongo.save_file_to_db('AWS', file_path, filename, user_uuid)
    elif provider == 'google':
        file_path = google_cloud_download.download_blob(bucketname, filename)
        mongo.save_file_to_db('GOOGLE', file_path, filename, user_uuid)


def upload_file_by_name(provider, bucketname, filename):
    if provider == 'aws':
        s3_upload.upload_file(bucketname, filename)
    elif provider == 'google':
        google_cloud_upload.upload_blob(bucketname, filename)


def copy_file(filename, provider, provider_bucket, dest, dest_bucket):
    if provider == dest:
        print("Target cloud needs to different than the source cloud")
        exit
    else:
        get_file_by_name(provider, provider_bucket, filename)
        upload_file_by_name(dest, dest_bucket, filename)


def rsync_file(filename, source, dest):
    print('')


def delete_file(provider, bucketname, filename):
    if provider == 'aws':
        s3_delete.delete_file(bucketname, filename)
    elif provider == 'google':
        google_cloud_delete.delete_blob(bucketname, filename)


def update_user_for_file(user_uuid, filename):
    mongo.update_user_for_file(user_uuid, filename)









