# -*- coding: UTF-8 -*-
import wx
import boto
# from init_game import CloudGame


def OnQuit(e):
    main_frame.Close()

def ConnectToGame(e):
    return 0
    # game = CloudGame()
    # game.startInstance()
    # game.startGame()
    
def ChangeGameSelection(e):
    section = game_list_box.GetSelections()[0]
    game_name = game_list_box.GetString(section)
    game_name_label.SetLabel('Game Name: '+game_name)
    game_genre_label.SetLabel('Game Genre: '+game_dict[game_name][0])
    game_area_label.SetLabel('Graphic Engine: '+game_dict[game_name][1])
    start_image = wx.Image(game_dict[game_name][2])
    start_image.Rescale(200, 100)
    game_logo_widget.SetBitmap(wx.BitmapFromImage(start_image))
    
app = wx.App(False)
main_frame = wx.Frame(None, 0, "Kudan Cloud Gaming Platform", size=(600, 600), pos=(20, 20))
main_frame.Show(True)

connect_button = wx.Button(main_frame, label='CONNECT', pos=(250, 500))
connect_button.SetBackgroundColour(wx.Colour(64, 64, 64))
connect_button.Bind(wx.EVT_BUTTON, ConnectToGame)

quit_button = wx.Button(main_frame, label='QUIT', pos=(0, 0))
quit_button.SetBackgroundColour(wx.Colour(64, 64, 64))
quit_button.Bind(wx.EVT_BUTTON, OnQuit)

# 服务器列表栏
server_list = ['i-0aba734d414f3aefa']
server_list_box = wx.ListBox(main_frame, -1, (100, 70), (200, 150), server_list, wx.LB_SINGLE)
server_list_box.SetSelection(0)
main_frame.Bind(wx.EVT_LISTBOX, ChangeGameSelection, server_list_box)

# 服务器信息栏
server_dict = {'i-0aba734d414f3aefa':['g4dn.xlarge','ap-east-1b', '18.163.151.101']}
instance_data1 = server_dict[server_list[0]]
server_id_label = wx.StaticText(parent=main_frame, label='Instance ID: '+server_list[0], pos=(350, 70))
server_type_label = wx.StaticText(parent=main_frame, label='Instance Type: '+instance_data1[0], pos=(350, 100))
server_area_label = wx.StaticText(parent=main_frame, label='Instance Area: '+instance_data1[1], pos=(350, 130))
server_ip_lable = wx.StaticText(parent=main_frame, label='Instance IP: '+instance_data1[2], pos=(350, 160))

# 游戏列表栏
game_list = ['AssaultCube', 'LIMBO', 'Cube2: Sauerbraten']
game_list_box = wx.ListBox(main_frame, -1, (100, 250), (200, 200), game_list, wx.LB_SINGLE)
game_list_box.SetSelection(0)
main_frame.Bind(wx.EVT_LISTBOX, ChangeGameSelection, game_list_box)

game_dict = {'AssaultCube':['FPS', 'SDL', 'gameLogo/AssaultCube.png'], 
             'LIMBO':['ACT', 'DirectX9', 'gameLogo/LIMBO.png'], 
             'Cube2: Sauerbraten':['FPS', 'SDL', 'gameLogo/Cube2: Sauerbraten.png']}

# 游戏信息栏
game_data1 = game_dict[game_list[0]]
game_name_label = wx.StaticText(parent=main_frame, label='Game Name: '+game_list[0], pos=(350, 250))
game_genre_label = wx.StaticText(parent=main_frame, label='Game Genre: '+game_data1[0], pos=(350, 280))
game_area_label = wx.StaticText(parent=main_frame, label='Graphic Engine: '+game_data1[1], pos=(350, 310))
start_image = wx.Image(game_data1[2])
start_image.Rescale(200, 100)
bitmap = wx.BitmapFromImage(start_image)
game_logo_widget = wx.StaticBitmap(main_frame, -1, bitmap)
game_logo_widget.SetPosition((350, 340))

app.MainLoop()


    