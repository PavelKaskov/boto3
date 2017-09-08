import boto3

ec2 = boto3.resource('ec2')

# Use the filter() method of the instances collection to retrieve
# all running EC2 instances.
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name':
            name_inst = tag['Value']
    print name_inst, instance.id, instance.instance_type
