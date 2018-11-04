import re
from cloudmesh.data.listFiles import listFiles
from cloudmesh.data.move_file import moveFile

print("########### Cross Platform File Strorage System")
while 1:
    print("0. Exit")
    print("1. List Files")
    print("2. Move File")
    choice = int(input("Enter Choice "))
    #print(choice)
    if (choice == 1):
        #print("hello world")
        print("################################")
        listFiles()
        print("################################")
    elif (choice == 2):
        print ("###############################")
        filePath=""
        while (re.compile("^(s3|gc)").match(filePath) is None):
            print("Incorrect filename...")
            filePath = input("Enter Filename: ")
        targetCloud = ""
        while (targetCloud!="s3" and targetCloud!="gc"):
            targetCloud = input("Enter Target Cloud(s3/gc) ")
        moveFile(filePath, targetCloud)
        print("###############################")
    elif (choice == 0):
        exit(0)