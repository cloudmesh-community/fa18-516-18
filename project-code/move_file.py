import re
def moveFile(filePath, targetCloud):
    #match format
    if re.compile("^(s3://|gc://)").match(filePath) is None:
        print("Incorrect filename...")
        return
    filePathParsed = re.search(r"^(s3|gc)://(.*)/(.*)", filePath)
    sourceCloud = filePathParsed.group(1)
    bucket = filePathParsed.group(2)
    fileName = filePathParsed.group(3)
    print("sourceCloud="+sourceCloud+"\nbucket="+bucket+"\nfilename="+fileName)
    if sourceCloud == targetCloud:
        print("Target cloud needs to different than the source cloud")
        exit

#    if filePath.startswith("s3"):


 #   elif filePath.startswith("gc"):


    return
