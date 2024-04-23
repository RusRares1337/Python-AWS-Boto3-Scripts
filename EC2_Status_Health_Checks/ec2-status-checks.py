import boto3
import schedule

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

# Function to known which instances are in which state
def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses ['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instace {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")


# Scheduler that triggers the program automatically every 5 minutes
schedule.every(5).minutes.do(check_instance_status)

while True:
    schedule.run_pending()