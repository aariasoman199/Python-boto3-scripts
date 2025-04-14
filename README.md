# Describe EC2 and VPCs using Boto3

This Python script connects to AWS using Boto3 and retrieves detailed information about either EC2 instances or VPCs, based on the command-line argument provided.

## Requirements

1. Python 3.x
2. Boto3 library (pip install boto3)
3. AWS credentials configured

## How It Works

The script takes a single command-line argument:

1. ec2 – Retrieves details of EC2 instances
2. vpc – Retrieves details of VPCs and their associated subnets

Example:
```sh
python3 describe_ec2_vpc.py ec2
```
