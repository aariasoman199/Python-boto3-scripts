import boto3
import sys

action = sys.argv[1] #ec2 or vpc

vpc_details = []
subnet_by_vpc = {}
ins = []

aws_access_key = ################
aws_secret_key = ################
aws_region = "ap-south-1"

def instance_info():
    ec2_client = boto3.client('ec2',aws_access_key_id=aws_access_key,aws_secret_access_key=aws_secret_key,region_name= aws_region)

    response = ec2_client.describe_instances()

    for Reservation in response['Reservations']:
        for Instance in Reservation['Instances']:
            ins_dict = {}
            for Tag in Instance['Tags']:
                if Tag['Key'] == 'Name':
                    ins_dict['Name'] = Tag['Value']
                ins_dict['Instanceid'] = Instance['InstanceId']
                ins_dict['Imageid'] = Instance['ImageId']
                ins_dict['InstanceType'] = Instance['InstanceType']
                ins_dict['InstanceState'] = Instance['State']['Name']
                ins_dict['PrivateIpAddress'] = Instance['PrivateIpAddress']
                if 'PublicIpAddress' in Instance:
                    ins_dict['PublicIpAddress'] = Instance['PublicIpAddress']
                else:
                    ins_dict['PublicIpAddress'] = 'null'
                ins_dict['VpcId'] = Instance['VpcId']
                ins_dict['SubnetId'] =Instance['SubnetId']
                ins_dict['AvailabilityZone'] = Instance['Placement']['AvailabilityZone']
                ins.append(ins_dict)
            
            
    
        return ins


def vpc_info():
    ec2_client = boto3.client('ec2',aws_access_key_id=aws_access_key,aws_secret_access_key=aws_secret_key,region_name= aws_region)

    response = ec2_client.describe_vpcs()

    response_subnet = ec2_client.describe_subnets()


    for subnet in response_subnet['Subnets']:
        subnet_details = {}
        subnet_details['SubnetId'] = subnet['SubnetId']
        subnet_details['CidrBlock'] = subnet['CidrBlock']
        subnet_details['AvailabilityZone'] = subnet['AvailabilityZone']
        vpc_id = subnet['VpcId']

        if vpc_id not in subnet_by_vpc:
            subnet_by_vpc[vpc_id] = []

        subnet_by_vpc[vpc_id].append(subnet_details)


    for vpc in response['Vpcs']:
        vpc_dict = {}
        for Tag in vpc['Tags']:
            if Tag['Key'] == 'Name':
                vpc_dict['Name'] = Tag['Value']
                vpc_dict['VpcId'] =vpc['VpcId']
                vpc_dict['CidrBlock'] = vpc['CidrBlock']
                vpc_details.append(vpc_dict)

            if vpc_dict['VpcId'] in subnet_by_vpc:
                vpc_dict['Subnet'] = subnet_by_vpc[vpc_dict['VpcId']]
                    
                    
                

    return(vpc_details)


if action.lower() == 'ec2':
    result1 = instance_info()
    print(result1)

if action.lower() == 'vpc':
    result2 = vpc_info()
    print(result2)
