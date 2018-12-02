# Manage Files Across Cloud Providers :hand: fa18-516-18

| Richa Rastogi
| rirastog@iu.edu
| Indiana University
| hid: fa18-516-18
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-516-18/blob/master/project-report/report.md)

---

Keywords: Multi-cloud data service, Cloud Computing, Python, Open API, Cloud Providers, MongoDB, Swagger

---

## Abstract

The goal of this project is to manage files across different cloud providers. There are many cloud providers where we can store data in form of files like Amazon AWS, Microsoft Azure, Google cloud, etc. Here we are going to build an OpenAPI to manage these files, operations like copy, upload, download or delete from any provider. This system is self sufficient to work as a file manager.


## Introduction

The objective of this project is to manage data across different cloud providers. We are going to build an RESTFUL OpenAPI for managing the data between all the cloud storages. We will analyse how these different clouds work and then build python methods to handle data across them. Final step will be to expose these functionalities as a RESTFUL API. This way we can also take advantage of cloud providers for cheaper solutions for storage by dividing the data across them. Since this project has its own MongoDB and User profiling so it can be used a file manager in itself.

## Requirements

This project requires knowledge about Cloud Providers like AWS, Azure, Google Cloud, etc. 
* This project is using Amazon AWS and Google cloud as two cloud providers and their storage functionality. We can expand this 
* This also needs a database so we are using MongoDB through MongoEngine and store the files and User data in it.
* Overall functionality can be accesses through console or RESTFUL OpenAPI which is built using Flask and Swagger.

## Design

This project involves developing a RESTFUL API to manage files. We can perform following operations like upload, download, list, copy, rsync and delete. We can also this project to store files in MongoDB and assign specific User Role permissions to access the files. 

* The very first thing required for that is to create accounts in AWS and Google(Since those are the two providers we are using). 
* Then use their API Keys to connect to these providers through Python code. 
* After we have a connection, we use their APIs to access the bucket by providing the name through Yaml file/API input.
* Now since we have the bucket, we can list, download or upload the files.
* There is Command console from where we can execute these functions directly using console or script file.
* On top of that there is an open API built to perform these functions using REST.
* We also have MongoDB storing the downloaded files.

## Implementation

This project is using following technologies for implementation:
* Python 3.7.0 for python code development
* Swagger 2.0 for writing API specification. This specification describes REST endpoints for managing files across providers.
* Python flask framework which consumes the OpenAPI specification and directs the endpoints to Python functions by building a RESTful app.
* MongoEngine as a Document-Object Mapper for working with MongoDB from Python.

Enable a virtual environment so that all installations can be done specifically in that env.
```
python3 -m virtualenv /home/richa/venv/    //to install venv
source /home/richa/venv/bin/activate		//to activate venv

Now my console looks like:

(venv) (3.7.0) richa@richa-VirtualBox:~$
```

### AWS access from Python:
* Install apache-libcloud by "pip install apache-libcloud"
* Follow instructions to create an AWS account - https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md
* Select S3 from Services and create a bucket
* To access this bucket, go to IAM and create a user and then create a new Access Key in "Security Credentials"
* While creating this key, system will promt to download pem file. Save that pem file onto your working machine.

### Google Cloud Platform:
* Install "pip install google-cloud-storage"
* pip install google-auth google-auth-httplib2
* pip install --upgrade google-api-python-client
* Create an account on Google Cloud by going to https://cloud.google.com/
* Create a new Project from the top of the page.
* Create a new storage bucket in google cloud, select Storage -> Storage -> Browser
* To access this bucket now, follow https://cloud.google.com/storage/docs/reference/libraries
* This will download a JSON file in your working VM and use that file for authentication to access Google Cloud Storage.

All the dependencies can be installed easily by running requirements.txt inside project-code so no need to do any pip install.

```bash
 pip install -r requirements.txt
```

AWS and Google Cloud specific functionality python files are under directory structure project-code/cloudmesh/data. cloudmesh-data.yaml is the yaml file holding all the information about these cloud setup. Aws_setup.py and google_cloud_setup.py uses this yaml file to authenticate the cloud providers and setup the connection to the cloud services.

It also has command.py under here to run the functionality from console passing in relevant input.

```
cmdata test
  cmdata set provider=PROVIDER
  cmdata set dir=BUCKET
  cmdata data add PROVIDER BUCKETNAME FILENAME
  cmdata data get PROVIDER BUCKETNAME FILENAME USER_UUID
  cmdata data ls PROVIDER BUCKETNAME
  cmdata data copy FILENAME PROVIDER PROVIDER_BUCKET DEST DEST_BUCKET
  cmdata data rsync FILENAME SOURCE DEST
  cmdata data del PROVIDER BUCKETNAME FILENAME
  cmdata update user USER file FILENAME
  cmdata (-h | --help)
  cmdata --version
Options:
  -h --help     Show this screen.
  --version     Show version.
  --config      Location of a cmdata.yaml file
Description:
   put a description here
Example:
   cmdata test
   cmdata data add AWS richa-516 MapReduce.docx
   cmdata data get AWS richa-516 MapReduce.docx 1234
   cmdata data ls AWS richa-516
   cmdata data copy xyz.txt AWS richa-516 GOOGLE richa-google-516
```

This project also has RESTFUL APIs to perform all the above operations and their Swagger UI looks like below. For File APIs, please refer to Figure
## Benchmark

## Conclusion

## Acknowledgement

## References
