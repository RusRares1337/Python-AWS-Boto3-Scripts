# Script that will list and go through snapshots 
# and check creation date, find the latest 2 and delete the rest.

import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-west-3")

# List all the volumes with tag name:Environment and value:Prod
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['Prod']
        }
    ]
)

for volume in volumes['Volumes']:
    # Fetch our snapshots
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume[VolumeId]]
            }
        ]
    )

    # Sort the snapshot lists by StartTime, with reverse=True we sort them in DESC order
    sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    # Delete all snapshots starting from 3rd item
    for snap in sorted_by_date[2:]:
        ec2_client.delete_snapshot(
            SnapShotId=snap['Snapshot']
        )

    # Fetch our snapshots
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self']
    )

