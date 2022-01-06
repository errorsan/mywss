import boto3
ec2 = boto3.client('ec2')
details = ec2.describe_instances()
print(details)
