# Scheduled task that goes through EC2 volumes everyday
# and creates Snapshots for those volumes.

import boto3

ec2_client = boto3.client('ec2', region_name='eu-west-3')

volumes = ec2_client.describe_volumes()
for volume in volumes['Volumes']:
    new_snapshot = ec2_client.create_snapshot(
        VolumeId=volume['VolumeId']
    )
    print(new_snapshot)


