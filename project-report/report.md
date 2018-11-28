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

## Architecture



## Dataset

## Implementation

## Benchmark

## Conclusion

## Acknowledgement

## References
