from cloudmesh_data.deprecated import google_cloud_list


def listFiles():
    """

    :return:
    """
    # aws_files = s3List.list_objects()
    google_files = google_cloud_list.list_object()
    # combined_files = aws_files.copy()
    # combined_files.extend(google_files)
    # print(aws_files)
    # print(google_files)
    for file in google_files:
        print(file)
