# import boto3

# ec2 = boto3.client('ec2', region_name='ap-southeast-1',
#     aws_access_key_id='AKIA3BIB67JYB45OCKCY',
#     aws_secret_access_key='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')
# response = ec2.describe_instances()
# print(response)


# import botocore
# import paramiko

# action = 'OFF'
# instance_id = 'i-066050703e6640286'

# ec2 = boto3.client('ec2', region_name='ap-southeast-1',
#     aws_access_key_id='AKIA3BIB67JYB45OCKCY',
#     aws_secret_access_key='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')


# if action == 'ON':
#     # Do a dryrun first to verify permissions
#     try:
#         ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
#     except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise

#     # Dry run succeeded, run start_instances without dryrun
#     try:
#         response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
#         print(response)
#     except ClientError as e:
#         print(e)
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

# client = paramiko.SSHClient()
# client.load_system_host_keys()

# Connect/ssh to an instance
# try:
#     # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
#     print('no')
#     client.connect(hostname='ec2-18-163-151-170.ap-east-1.compute.amazonaws.com', port=3389, username='Administrator', password='DrScd83t6aHUpd)feDD3KT)TbgLT%ifm')
#     print('ok')
#     # # Execute a command(cmd) after connecting/ssh to an instance
#     stdin, stdout, stderr = client.exec_command('dir')
#     print(stdin.read())
#     print(stderr.read())
#     print(stdout.read())

#     # # close the client connection once the job is done
#     client.close()

# except Exception as e:
#     print (e)

# import spur
# shell = spur.SshShell(hostname='ec2-18-163-151-170.ap-east-1.compute.amazonaws.com', port=3389, username="Administrator", password="DrScd83t6aHUpd)feDD3KT)TbgLT%ifm")
# result = shell.run(["echo", "-n", "hello"])
# print(result.output) # prints hello

# import winrm

# wintest = winrm.Session('http://18.163.152.147:5985/wsman',auth=('Administrator','A(nI9;qULc;KKA@HJAtUp)5$dE8XntvG'), read_timeout_sec=60)
# ret = wintest.run_cmd('ipconfig')
# print(ret)
from rdpy.protocol.rdp import rdp
class MyRDPFactory(rdp.ClientFactory):

    def clientConnectionLost(self, connector, reason):
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

    def buildObserver(self, controller, addr):

        class MyObserver(rdp.RDPClientObserver):

            def onReady(self):
                """
                @summary: Call when stack is ready
                """
                #send 'r' key
                self._controller.sendKeyEventUnicode(ord(unicode("r".toUtf8(), encoding="UTF-8")), True)
                #mouse move and click at pixel 200x200
                self._controller.sendPointerEvent(200, 200, 1, true)

            def onUpdate(self, destLeft, destTop, destRight, destBottom, width, height, bitsPerPixel, isCompress, data):
                """
                @summary: Notify bitmap update
                @param destLeft: xmin position
                @param destTop: ymin position
                @param destRight: xmax position because RDP can send bitmap with padding
                @param destBottom: ymax position because RDP can send bitmap with padding
                @param width: width of bitmap
                @param height: height of bitmap
                @param bitsPerPixel: number of bit per pixel
                @param isCompress: use RLE compression
                @param data: bitmap data
                """
                
            # def onSessionReady(self):
		        # """
		        # @summary: Windows session is ready
		        # """

            # def onClose(self):
                # """
                # @summary: Call when stack is close
                # """

        return MyObserver(controller)

from twisted.internet import reactor
reactor.connectTCP("18.163.151.101", 3389, MyRDPFactory())
reactor.run()