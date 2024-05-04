# Script that will list and go through snapshots 
# and check creation date, find the latest 2 and delete the rest.

import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-west-3")

# Fetch our snapshots
snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self']
)

# Sort the snapshot lists by StartTime, with reverse=True we sort them in DESC order
sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

# Delete all snapshots starting from 3rd item
for snap in sorted_by_date[2:]:
    ec2_client.delete_snapshot(
        SnapShotId=snap['Snapshot']
    )
    