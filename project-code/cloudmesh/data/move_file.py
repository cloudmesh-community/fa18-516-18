import re

from cloudmesh.deprecated import google_cloud_download, google_cloud_upload, s3_download, s3_upload


def moveFile(filepath, targetcloud):
    """

    :param filepath:
    :param targetcloud:
    :return:
    """
    # match format
    if re.compile("^(s3://|gc://)").match(filepath) is None:
        print("Incorrect filename...")
        return
    filepathparsed = re.search(r"^(s3|gc)://(.*)/(.*)", filepath)
    sourcecloud = filepathparsed.group(1)
    bucket = filepathparsed.group(2)
    filename = filepathparsed.group(3)
    print("sourceCloud=" + sourcecloud + "\nbucket=" + bucket + "\nfilename=" + filename)
    if sourcecloud == targetcloud:
        print("Target cloud needs to different than the source cloud")
        exit
    if filepath.startswith("s3"):
        s3_download.download_file(filename)
        if targetcloud == 'gc':
            google_cloud_upload.upload_blob(filename)

    elif filepath.startswith("gc"):
        google_cloud_download.download_blob(filename)
        if targetcloud == 's3':
            s3_upload.upload_file(filename)
    return
