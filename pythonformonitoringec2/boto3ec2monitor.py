import boto3
ec2 = boto3.client('ec2')
details = ec2.describe_instances()
print(details)
monitor = ec2.monitor_instances(InstanceIds = ['i-0a365b04c11c16930'])
print(monitor) 
