# Manage Files Across Cloud Providers :hand: fa18-516-18

| Richa Rastogi
| rirastog@iu.edu
| Indiana University
| hid: fa18-516-18
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-516-18/blob/master/project-paper/report.md)

---

Keywords: Multi-cloud data service, Cloud Computing, Python, Open API, Cloud Providers, MongoDB, Swagger

---

## Abstract

The goal of this project is to manage files across different cloud providers. There are many cloud providers where we can store data in form of files like Amazon AWS, Microsoft Azure, Google cloud, etc. Here we are going to build an OpenAPI to manage these files, operations like copy, upload or download from one provider to another. 


## Introduction

The objective of this project is to manage data across different cloud providers. We are going to build an Open API for managing the data between all the cloud storages. We will analyse how these different clouds work and then build python methods to handle data across them. Final step will be to expose these functionalities as an API. This way we can also take advantage of cloud providers for cheaper solutions for storage by dividing the data across them.

## Requirements

We require accounts in various cloud providers(atleast 2) to test this functionality. I have used Amazon AWS and Google cloud as two cloud providers here and use their storage functionality. 

## Design

This project is designed to copy files from a cloud provider to another by downloading from one place and uploading to another. 

* The very first thing for that is to create accounts in AWS and Google. 
* Then use their API Keys to connect to these providers through Python code. 
* After we have a connection, we use their APIs to access the bucket by providing the name through Yaml file.
* Now since we have the bucket, we can list, download or upload the files.
* There is Command console from where we can execute these functions directly using console or script file.
* On top of that there is an open API built to perform these functions using REST.
* We also have MongoDB storing the downloaded files.


## Dataset

## Implementation

This project is using following technologies for implementation:
* Swagger 2.0 for writing API specification. This specification describes REST endpoints for managing files across providers.
* Python flask framework which consumes the OpenAPI specification and directs the endpoints to Python functions by building a RESTful app.
* MongoEngine as a Document-Object Mapper for working with MongoDB from Python.

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

## Benchmark

## Conclusion

## Acknowledgement

## References
