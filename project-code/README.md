This document instructs the setup for various cloud providers.

Here we will be using mainly 2 Cloud Providers for this project - Amazon AWS and Google Cloud Platform

### AWS Setup:

1. Install apache-libcloud by "pip install apache-libcloud"
2. Follow instructions to create an AWS account - https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md
3. Select S3 from Services and create a bucket
4. To access this bucket, go to IAM and create a user and then create a new Access Key in "Security Credentials"
5. While creating this key, system will promt to download pem file. Save that pem file onto your working machine.

### Google Cloud Platform:

1. Install "pip install google-cloud-storage"
2. pip install google-auth google-auth-httplib2
3. pip install --upgrade google-api-python-client
4. Create an account on Google Cloud by going to https://cloud.google.com/
5. Create a new Project from the top of the page.
6. Create a new storage bucket in google cloud, select Storage -> Storage -> Browser
7. To access this bucket now, follow https://cloud.google.com/storage/docs/reference/libraries 
8. This will download a JSON file in your working VM and use that file for authentication to access Google Cloud Storage.
