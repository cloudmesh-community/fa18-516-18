# Introduction

The objective of this project is to manage data across different cloud providers. We are going to build an RESTFUL OpenAPI for managing the data between all the cloud storages. We will analyse how these different clouds work and then build python methods to handle data across them. Final step will be to expose these functionalities as a RESTFUL API. This way we can also take advantage of cloud providers for cheaper solutions for storage by dividing the data across them. Since this project has its own MongoDB and User profiling so it can be used a file storage and manager in itself.

Complete report with sample output is at [Report.md](https://github.com/cloudmesh-community/fa18-516-18/blob/master/project-report/report.md)


## Steps to be followed for setup:

1. Install requirements.txt by following command
```
  pip install -r requirements.txt
```

2. Make accounts in AWS and Google Cloud
3. Follow steps below to access these Cloud Providers [AWS](https://github.com/cloudmesh-community/fa18-516-18/blob/master/project-code/README.md#aws-access-from-python) and [Google Cloud](https://github.com/cloudmesh-community/fa18-516-18/blob/master/project-code/README.md#google-cloud-platform) from Python.
4. Now run following command to access our code and running "cmdata" commands
```
  pip install -e .
```
5. Then run following cmdata commands to test the flow
```
  cmdata data ls google_cloud
  cmdata data get google_cloud Test.txt richa
  cmdata data del google_cloud Test.txt
  cmdata data add google_cloud Test.txt
```

6. There are REST APIs as well for these functionalities. Run below commands to start the server and then run curl commands for APIs
```
   make server
   make file
```


### AWS access from Python:

1. Follow instructions to create an AWS account - https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md
2. Select S3 from Services and create a bucket
3. To access this bucket, go to IAM and create a user and then create a new Access Key in "Security Credentials"
4. While creating this key, system will promt to download pem file. Save that pem file onto your working machine.


### Google Cloud Platform:

1. Create an account on Google Cloud by going to https://cloud.google.com/
2. Create a new Project from the top of the page.
3. Create a new storage bucket in google cloud, select Storage -> Storage -> Browser
4. To access this bucket now, follow https://cloud.google.com/storage/docs/reference/libraries
5. This will download a JSON file in your working VM and use that file for authentication to access Google Cloud Storage.
