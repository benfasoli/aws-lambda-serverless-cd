# AWS Lambda Deployment Pipeline

This repository contains a minimal (3 short files) example of how to use [GitHub Actions](https://github.com/features/actions) and [Serverless Framework](https://serverless.com/) to automate the deployment pipeline for an API backed with [AWS Lambda](https://aws.amazon.com/lambda/) and [AWS API Gateway](https://aws.amazon.com/api-gateway/).

## Why

AWS includes powerful tools for production deployments but the learning curve to spin up a new service can be steep. This is intended to be used as a starter for other serverless projects, along with the great examples provided in the [serverless/examples](https://github.com/serverless/examples) repo.

AWS Lambda is the current leader in serverless computing and provides the execution environment for user defined functions. 

AWS API Gateway can be used to map Lambda function execution to public facing HTTP endpoints and can be configured to perform JWT authentication/authorization, abstracting the auth logic away from application code.

## Files

- [serverless.yml](serverless.yml) configures the application to receive events at a given URL.  
- [handler.py](handler.py) receives the event and returns a response.  
- [.github/workflows/main.yml](.github/workflows/main.yml) configures GitHub Actions to build and deploy the application.  

## Setup

Clone or copy these files and the corresponding directory structure. None of these files need to be edited to get a working example, since the only configuration necessary is supplying the credentials (instructions below) to allow the GitHub Actions runner to configure the necessary AWS resources.

You'll need an AWS account to deploy the application.

1. Go to the [Users](https://console.aws.amazon.com/iam/home#/users) page in the AWS Identity and Access Management (IAM) console.  
1. Create a new Admin user that will be used by the deployment pipeline.
1. Select this user, then **Security credentials > Access keys** and **Create access key**.  
1. Add the key credentials to the Secrets settings of your GitHub repository, found at **Settings > Secrets** using the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.

Done! Each new push to `master` will now build and redeploy the service.
