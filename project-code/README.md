# Openapi Virtual Directory

This document instructs the setup for various cloud providers.

Here we will be using mainly 2 Cloud Providers for this project - Amazon AWS and Google Cloud Platform


Gregor's development setup

```bash
$ pip install -r requirements.txt
$ python setup.py install -e .
```


:o: use proper verbatim in rest of readme.

:o: :hperlinks must be in  greater smaller brackets

## AWS Setup:

1. Install apache-libcloud by "pip install apache-libcloud"
2. Follow instructions to create an AWS account

    * <https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md>
	
3. Select S3 from Services and create a bucket
4. To access this bucket, go to IAM and create a user and then create a new Access Key in "Security Credentials"
5. While creating this key, system will promt to download pem file. Save that pem file onto your working machine.

## Google Cloud Platform:

1. Install "pip install google-cloud-storage"
2. pip install google-auth google-auth-httplib2
3. pip install --upgrade google-api-python-client
4. Create an account on Google Cloud by going to https://cloud.google.com/
5. Create a new Project from the top of the page.
6. Create a new storage bucket in google cloud, select Storage -> Storage -> Browser
7. To access this bucket now, follow https://cloud.google.com/storage/docs/reference/libraries 
8. This will download a JSON file in your working VM and use that file
   for authentication to access Google Cloud Storage.

## Example use from commandline

Usecs is to do this and that an the other

:o: please use the 3 quote syntax

	cmdata set cloud=AWS
	cmdata set dir=xyz
	cmdata data add file1.txt  [--label file1.txt]
	
	cmdata set cloud=GOOGLE
	cmdata set dir=xyz
	cmdata data add file1.txt [--label file1.txt]

	cmdata vdir create abc

	cmdata vdir abc add file1.txt
	cmdata vdir abc add file2.txt

    cmdata vdir list

    cmdata vdir abc get file1.txt
    cmdata get file1.txt


	cmdata add user gregor file file1.txt
	cmdata file1.txt permission gregor +rw

gregor:
  name:
  role:
  sshpubkey: ssh sdhjsdhkjh .....


chmod
chgrp

share files with users



  cmdata data add FILE



  cmdata data get FILE
  cmdata data get FILE DEST_FOLDER
  cmdata data del FILE
  cmdata data move FILE SOURCE DEST
  cmdata data (ls | dir)
  cmdata set group=GROUP
  cmdata set role=ROLE
  cmdata set host=HOSTNAME
  cmdata set cluster=CLUSTERNAME
  cmdata set experiment=EXPERIMENT
  cmdata (-h | --help)


file.yaml

d = yaml load (file.yaml)

generrate("File")

   """for property in properties:

   label = endpoint
   type
   description
   """
   return spec 


"""
class FIle(Document):
    endpoint = StringField()
    name = StringFIeld()
	....
"""

eval = spec








