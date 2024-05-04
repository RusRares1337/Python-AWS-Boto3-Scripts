# Script that will recover the latest working state
# and attach a new volume to EC2 Instance

import boto3

ec2_client = boto3.client('ec2', region_name="eu-west-3")
ec2_resource = boto3.resource('ec2', region_name="eu-west-3")

instance_id = 'i-0bc53c17e7a0c29b3'

# Filter the volumes that belong to that specific instance id
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume = volumes['Volumes'][0]
print(instance_volume)