#!/usr/bin/python3

import ffmpeg, wx

class mainWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(mainWindow, self).__init__(*args, **kwargs)

        self.InitUI()

    def changeInputFiles(self, event):
        print('test')

    def InitUI(self):
        '''
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        '''

        #self.SetSize((400, 500))
        self.SetTitle('Lapser')
        self.SetWindowStyle(wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        #self.Centre()

        
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)

        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox_input_files = wx.BoxSizer(wx.HORIZONTAL)

        st_input_files = wx.StaticText(panel, label='Input files:')
        st_input_files.SetFont(font)
        hbox_input_files.Add(st_input_files, flag=wx.RIGHT | wx.CENTER, border=8)

        tc_input_files = wx.TextCtrl(panel, value='No files selected', style=wx.TE_READONLY)
        hbox_input_files.Add(tc_input_files, proportion=1)

        vbox.Add(hbox_input_files, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox_change_input_files = wx.BoxSizer(wx.HORIZONTAL)
        button_input_files = wx.Button(panel, label='Choose Input Files')
        button_input_files.Bind(wx.EVT_BUTTON, self.changeInputFiles)
        hbox_change_input_files.Add(button_input_files, proportion=1)

        vbox.Add(hbox_change_input_files, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        #vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Matching Classes')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)

        vbox.Add((-1, 25))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(panel, label='Case Sensitive')
        cb1.SetFont(font)
        hbox4.Add(cb1)
        cb2 = wx.CheckBox(panel, label='Nested Classes')
        cb2.SetFont(font)
        hbox4.Add(cb2, flag=wx.LEFT, border=10)
        cb3 = wx.CheckBox(panel, label='Non-Project classes')
        cb3.SetFont(font)
        hbox4.Add(cb3, flag=wx.LEFT, border=10)
        vbox.Add(hbox4, flag=wx.LEFT, border=10)

        vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)

    '''
    def OnQuit(self, e):
        self.Close()
    '''


def main():

    app = wx.App()
    root = mainWindow(None)
    root.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()

'''
input_files = input("Input files: ")
output_file = input("Output file: ")
#width = input("Width: ")
#height = input("Height: ")
display_framerate = input("Timelapse framerate: ")
file_framerate = input("File framerate: ")
overwrite = input("Overwrite? [y/n] ")
stream = ffmpeg.input(input_files, r=int(display_framerate), pattern_type='glob')
stream = ffmpeg.filter_(stream, 'format', 'yuv420p')
#stream = ffmpeg.filter_(stream, 'scale', '{}x{}'.format(width, height))
stream = ffmpeg.output(stream, output_file, r=int(file_framerate))
if overwrite.lower() in ['y', 'yes']:
    ffmpeg.overwrite_output(stream)
ffmpeg.run(stream)
'''
