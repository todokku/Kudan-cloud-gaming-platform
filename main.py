# -*- coding: UTF-8 -*-
import wx
import boto

def OnQuit(e):
    main_frame.Close()

def ConnectToEC2(e):
    ec2 = boto3.client('ec2', region_name='ap-east-1b',
    aws_access_key_id='AKIAJCOQ4OUTBMDONM2Q',
    aws_secret_access_key='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')
    response = ec2.describe_instances()
    print(response)
    
app = wx.App(False)
main_frame = wx.Frame(None, 0, "Kudan Cloud Gaming Platform", size=(600, 600), pos=(20, 20))
main_frame.Show(True)

connect_button = wx.Button(main_frame, label='CONNECT', size=(100, 70), pos=(250, 300))
connect_button.Bind(wx.EVT_BUTTON, ConnectToEC2)

quit_button = wx.Button(main_frame, label='QUIT', size=(96, 96), pos=(0, 0))
quit_button.SetBitmap(wx.Bitmap("quit.png"),wx.LEFT)
quit_button.Bind(wx.EVT_BUTTON, OnQuit)

app.MainLoop()


    