import wx
import os
from pyo import *
sndPath = "../sounds/"
s = Server().boot()
table = SndTable(sndPath+'snd_1.aif')
osc = Osc(table, freq=table.getRate(),mul = 0.5)
mix = osc.mix(2).out()
class MyFrame(wx.Frame):
    def __init__(self, parent, title, pos, size):
        wx.Frame.__init__(self, parent, id=-1, title=title, pos=pos, size=size)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("#DDDDDD")
        self.onOffText = wx.StaticText(self.panel,id=-1,label="Audio",pos = (28,10), size = wx.DefaultSize)
        self.onOff = wx.ToggleButton(self.panel,id=-1,label="on / off",pos = (10,28), size = wx.DefaultSize)
        list = os.listdir('../sounds')
        self.popupText=wx.StaticText(self.panel,id=-1, label = "choisi",pos=(10,60),size=wx.DefaultSize)
        self.popup = wx.Choice(self.panel,id=-1,pos=(8,78),size=wx.DefaultSize,choices = list)
        
        
        self.onOff.Bind(wx.EVT_TOGGLEBUTTON, self.handleAudio)
        
        self.popup.Bind(wx.EVT_CHOICE,self.setSound)
    def handleAudio(self,evt):
        if( evt.GetInt() ==1):
            s.start()
        else:
            s.stop()
        
    def setSound(self,evt):
        table.sound = sndPath+evt.GetString()
        osc.freq=table.getRate()
        
        
app = wx.App()
mainFrame = MyFrame(None, title = 'simple App', pos = (100,100), size = (500,300))

mainFrame.Show()
app.MainLoop()
