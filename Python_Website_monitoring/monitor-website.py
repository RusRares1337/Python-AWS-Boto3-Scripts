# Scheduled task to monitor application health
# Automated Email notification
# Restart application and reboot server

import requests
import smtplib
import os
import paramiko
import boto3
import time

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_notification(email_msg):
    print('Sending an email..')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = EMAIL_ADDRESS, EMAIL_PASSWORD, f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, message)

def restart_container():
    print('Restarting the application...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('15.237.181.14', username='ubuntu', key_filename='/Users/raresrus/.ssh/aws.pem')
    stdin, stdout, stderr = ssh.exec_command('docker start edcdc481487d')
    print(stdout.readlines())
    ssh.close()

try:
    response = requests.get('http://15.237.181.14:8080/')
    if response.status_code == 200:
        print("Application is running successfully")
    else:
        print('Application Down. Fix it!')
        msg = f'Application returned {response.status_code}'
        send_notification(msg)
        restart_container()
except Exception as ex:
    print(f'Connection error happened: {ex}')
    msg = 'Application not accesible at all.'
    send_notification(msg)

    # restart ec2 server
    print('Rebooting the server...')
    nginx_server = ec2.client.reboot_instances(InstanceIds=['i-0f10b0b7aed92bf0b'])
    nginx_server.reboot_instances()

    # restart the application
    while True:
        nginx_server = ec2.client.reboot_instances(InstanceIds=['i-0f10b0b7aed92bf0b'])
        if nginx_server.instancestatuses.instancestate == 'running':
            time.sleep(5)
            restart_container()
            break