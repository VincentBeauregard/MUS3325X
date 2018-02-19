import wx

class MyFrame(wx.Frame):
	def __init__(self,parent,title,pos,size):
		wx.Frame.__init__(self,parent,id=-1,title=title,pos=pos,size=size)
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour("#000000")

app = wx.App()

mainFrame = MyFrame(None, title='test', pos=(100,100), size = (500,300))
mainFrame.Show()

app.MainLoop()
