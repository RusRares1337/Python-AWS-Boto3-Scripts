# Scheduled task that goes through EC2 volumes everyday
# and creates Snapshots for those volumes.

import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='eu-west-3')

def create_voume_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Environment',
                'Values': ['Prod']
            }
        ]
    )
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)


schedule.every().day.do(create_voume_snapshots)

while True:
    schedule.run_pending()

