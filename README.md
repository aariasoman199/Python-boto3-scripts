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
## Algorithm Summary

1. Input: A command-line argument indicating whether to fetch ec2 or vpc info.

2. Initialize AWS Client: Using hardcoded credentials and Boto3.

3. If ec2 selected:

   - Call instance_info()
   - Loop through instances to extract:
   -  Name tag, instance ID, type, state, IPs, subnet, VPC, and AZ.
   - Format and print as a list of dictionaries.

4. If vpc selected:

   - Call vpc_info()
   - Group subnets under corresponding VPCs
   - Format and print as a list of VPC dictionaries with subnet details.

## Function Descriptions

### instance_info()
- Connects to EC2
- Retrieves all instances
- Extracts and structures details including:
- Name, ID, AMI, type, state, IPs, VPC, subnet, AZ
- Returns list of EC2 instance dictionaries

### vpc_info()
- Connects to EC2
- Retrieves all VPCs and subnets
- Maps subnets to corresponding VPCs
- Extracts: VPC name, ID, CIDR block,Subnet ID, CIDR block, and AZ
- Returns list of VPC dictionaries with embedded subnet list

## EC2 Example Output
```sh
[
{
'Name': 'shopping-Webserver-dev',
'Instanceid': 'i-06d263563c97aee50',
'Imageid': 'ami-05c179eced2eb9b5b',
'InstanceType': 't2.micro',
'InstanceState': 'stopped',
'PrivateIpAddress': '172.31.36.108',
'PublicIpAddress': 'null',
'VpcId': 'vpc-0a15b56e8bbd369cc',
'SubnetId': 'subnet-0ab12861f98052723',
'AvailabilityZone': 'ap-south-1a'}
}
]
```

## VPC Example Output
```sh
[
{
'Name': 'shopping',
'VpcId': 'vpc-00516b89656def807',
'CidrBlock': '172.16.0.0/16',
'Subnet':
         [
          {
            'SubnetId': 'subnet-02f7252a60332d556',
            'CidrBlock': '172.16.128.0/18',
             'AvailabilityZone': 'ap-south-1c'
          },
          {
            'SubnetId': 'subnet-0673b1a1338fa225b',
            'CidrBlock': '172.16.64.0/18',
            'AvailabilityZone': 'ap-south-1b'
          },
          {
            'SubnetId': 'subnet-0ac435a8fc87e625f',
            'CidrBlock': '172.16.0.0/18',
             'AvailabilityZone': 'ap-south-1a'
           }
         ]
}
]
```

## References

1. [describe_instances()](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html)

2. [ describe_vpcs()](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpcs.html)
3. [describe_subnets()](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_subnets.html)

