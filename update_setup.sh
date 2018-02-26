#!/bin/bash

aws s3 cp setup/setup.cf.yaml s3://theartofgin-codebuild-artifacts/cloudformation/setup.cf.yaml
aws cloudformation update-stack \
    --stack-name theartofgin-setup \
    --template-url https://s3.eu-central-1.amazonaws.com/theartofgin-codebuild-artifacts/cloudformation/setup.cf.yaml \
    --capabilities CAPABILITY_NAMED_IAM
