# -*- coding: UTF-8 -*-
import boto3
import botocore
import paramiko
import os
import threading
import subprocess
import time

def runRDP(func):
    a = subprocess.getstatusoutput('python2 rdp.py')

def runGame(func):
    os.system("./GAbin/ga-client GAbin/config/client.rel.conf rtsp://18.163.151.101:8554/desktop")

instance_id = 'i-0aba734d414f3aefa'
ec2 = boto3.client('ec2', region_name='ap-east-1', aws_access_key_id='AKIAJCOQ4OUTBMDONM2Q', aws_secret_access_key='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')

# Do a dryrun first to verify permissions
try:
    ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
except:
    print("")
try:
    response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
    print(response)
except:
    print("")

time.sleep(25)

ssm_client = boto3.client('ssm', region_name='ap-east-1',
    aws_access_key_id='AKIAJCOQ4OUTBMDONM2Q',
    aws_secret_access_key='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')

threads = []
t1 = threading.Thread(target=runRDP,args=(1,))
threads.append(t1)
t1.setDaemon(True)
t1.start()

time.sleep(5)

params2 = {"commands":["cd ../../Users/Administrator/gaminganywhere-0.8.0/bin","tasklist",r"PsExec.exe -s -i 2 'C:\Users\Administrator\gaminganywhere-0.8.0\bin\ga-server-event-driven.exe' 'C:\Users\Administrator\gaminganywhere-0.8.0\bin\config\server.assaultcube.win32.conf'"],"executionTimeout":["3600"]}
response2 = ssm_client.send_command(DocumentName="AWS-RunPowerShellScript", InstanceIds=[instance_id],Comment='Execute Limbo', TimeoutSeconds=600, Parameters=params2)
print(response2)

time.sleep(10)

t2 = threading.Thread(target=runGame,args=(1,))
threads.append(t2)
t2.setDaemon(True)
t2.start()

while True:
    time.sleep(10)

# # Dry run succeeded, run start_instances without dryrun
# try:
#     response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
#     print(response)
# except ClientError as e:
#     print(e)
# else:
#     # Do a dryrun first to verify permissions
#     try:
#         ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
#     except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise

#     # Dry run succeeded, call stop_instances without dryrun
#     try:
#         response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
#         print(response)
#     except ClientError as e:
#         print(e)