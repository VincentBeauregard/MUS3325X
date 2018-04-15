#!/usr/bin/env python
# encoding: utf-8
import wx
from pyo import *

s = Server().boot()
s.amp = 0.5

class FxSwitch:
    def __init__(self, fx='Delay'):
        self.fx = fx
        self.table = SndTable([SNDS_PATH+"/transparent.aif"]*2)
        self.input = Osc(self.table, freq=self.table.getRate())
        self.p1 = SigTo(value=0.5, time=0.05, init=0.5)
        self.p2 = SigTo(value=0.5, time=0.05, init=0.5)
        self.delay = Delay(self.input, delay=self.p1, feedback=self.p2).stop()
        self.disto = Disto(self.input, drive=self.p1, slope=self.p2, 
                           mul=.5).stop()
        self.degrade = Degrade(self.input, bitdepth=Sig(self.p1,mul=20,add=2),
                               srscale=Sig(self.p2,mul=.99,add=.01),
                               mul=1.5).stop()
        self.reverb = WGVerb(self.input, feedback=self.p1, 
                             cutoff=Sig(self.p2,mul=10000,add=250)).stop()
        self.harmo = Harmonizer(self.input, 
                                transpo=Sig(self.p1,mul=24,add=-12),
                                feedback=self.p2).stop()
        self.fx_dict = {'Delay': self.delay, 'Disto': self.disto, 
                        'Degrade': self.degrade, 'Reverb': self.reverb, 
                        'Harmonizer': self.harmo}
        self.fx_dict[fx].out()
        
    def changeFx(self, fx):
        self.fx_dict[self.fx].stop()
        self.fx_dict[fx].out()
        self.fx = fx

    def changeTable(self, snd):
        self.table.sound = snd
        self.input.freq = self.table.getRate()
        
    def changeP1(self, x):
        self.p1.value = x

    def changeP2(self, x):
        self.p2.value = x

# Surface de controle des parametres
# La classe est un derive de wx.Panel puisque qu'il 
# faut dessiner sur une surface quelconque!
class Surface(wx.Panel):
    def __init__(self, parent, pos, size, callback):
        wx.Panel.__init__(self, parent, pos=pos, size=size)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

        # reference a l'argument "callback" qui est la fonction a appeler 
        # quand on deplace le pointeur sur la surface
        self.callback = callback
        # Si la souris n'est pas enfoncee, la position est None (facile a filtrer)
        self.pos = None
        # Position du cercle representant la position courante
        self.circlePos = (200,200)

        ### assignation de methodes a certains evenements ###
        # wx.EVT_PAINT est envoye par la methode self.Refresh()
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        # bouton gauche de la souris enfonce
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        # bouton gauche de la souris relsche
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        # deplacement de la souris sur la surface
        self.Bind(wx.EVT_MOTION, self.OnMotion)

    def OnMouseDown(self, evt):
        # CaptureMouse soumet la souris a l'objet tant que 
        # ReleaseMouse() n'est pas appelee
        self.CaptureMouse()
        # evt.GetPosition() retourne la position du pointeur en pixel (x,y)
        self.pos = evt.GetPosition()
        # self.Refresh() envoie un evenement wx.EVT_PAINT pour rafraichir l'ecran
        self.Refresh()

    def OnMouseUp(self, evt):
        # self.HasCapture() retourne True si la souris est soumise a l'objet
        if self.HasCapture():
            # relache la souris
            self.ReleaseMouse()
            # reinitialise la position
            self.pos = None
            # rafraichit l'ecran
            self.Refresh()

    def OnMotion(self, evt):
        "OnMotion est appelee chaque fois que la souris se deplace sur le panneau"
        if self.HasCapture():
            # taille du panneau, tuple (X, Y)
            w,h = self.GetSize()
            # position courante de la souris, tuple (X, Y)
            self.pos = evt.GetPosition()
            # limite les valeur de position entre 0 et la taille en X ou en Y
            if self.pos[0] < 0:
                self.pos[0] = 0
            elif self.pos[0] > w:
                self.pos[0] = w
            if self.pos[1] < 0:
                self.pos[1] = 0
            elif self.pos[1] > h:
                self.pos[1] = h
            # rafraichit l'ecran
            self.Refresh()

    def OnPaint(self, evt):
        w,h = self.GetSize()
        # on dessine sur un objet wx.PaintDC
        dc = wx.AutoBufferedPaintDC(self)
        # specifie la couleur de la brosse courante (interieur des formes)
        dc.SetBrush(wx.Brush("#444444"))
        # dessine un rectangle aux dimensions du panneau
        dc.DrawRectangle(0, 0, w, h)
        # specifie la couleur du crayon pour le cadrillage
        dc.SetPen(wx.Pen("#666666", 1))
        # on dessine un quadrillage aux 50 pixels...
        for i in range(0, 400, 50):
            dc.DrawLine(0, i, w, i)
            dc.DrawLine(i, 0, i, h)
        # specifie la couleur du crayon pour la croix
        dc.SetPen(wx.Pen("#AAAAAA", 1))
        # si self.pos n'est pas None, on dessine une croix a la position courante
        if self.pos != None:
            # ajuste la position du cercle
            self.circlePos = self.pos
            # dessine une ligne horizontal a la hauteur Y
            dc.DrawLine(0, self.pos[1], w, self.pos[1])
            # dessine une ligne vertical a la largeur X
            dc.DrawLine(self.pos[0], 0, self.pos[0], h)
            # conversion des positions X et Y entre 0 et 1
            x = self.pos[0] / float(w)
            y = 1. - self.pos[1] / float(h)
            # affiche la position normalisee du pointeur
            dc.DrawText("%.3f, %.3f" % (x,y), 10, 10)
            # appel du callback pour acheminer les valeurs vers le processus audio
            self.callback(x, y)
        # nouvelle couleur de brosse pour le cercle
        dc.SetBrush(wx.Brush("#AA0000"))
        # dessine un cercle centre sur la position courante
        dc.DrawCircle(self.circlePos[0], self.circlePos[1], 5)

class MyFrame(wx.Frame):
    def __init__(self, parent=None, title="Fx Switcher", pos=(100,100),
                 size=(600,500), switcher=None):
        wx.Frame.__init__(self, parent, id=-1, title=title, pos=pos, size=size)
        self.switcher = switcher
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("#DDDDDD")

        self.onOffText = wx.StaticText(self.panel, id=-1, label="Audio",
                                       pos=(28,10))
        self.onOff = wx.ToggleButton(self.panel, id=-1, label="on / off", 
                                     pos=(10,28))
        self.onOff.Bind(wx.EVT_TOGGLEBUTTON, self.handleAudio)

        self.chooseButton = wx.Button(self.panel, id=-1, label="Load snd...", 
                                      pos=(10,65))
        self.chooseButton.Bind(wx.EVT_BUTTON, self.loadSnd)

        fxs = ['Delay', 'Disto', 'Degrade', 'Reverb', 'Harmonizer']
        self.popupText = wx.StaticText(self.panel, id=-1, 
                                       label="Choose FX", pos=(10,100))
        self.popup = wx.Choice(self.panel, id=-1, pos=(8,118), choices=fxs)
        self.popup.SetSelection(0)
        self.popup.Bind(wx.EVT_CHOICE, self.changeFx)

        # cree un objet Surface pour le controle des parametres
        self.surface = Surface(self.panel, pos=(150,28), size=(400,400), 
                               callback=self.changeParams)

    def handleAudio(self, evt):
        if evt.GetInt() == 1:
            s.start()
        else:
            s.stop()    

    def loadSnd(self, evt):
        wildcard = "All files|*.*|" \
               "AIFF file|*.aif;*.aiff;*.aifc;*.AIF;*.AIFF;*.Aif;*.Aiff|" \
               "Wave file|*.wav;*.wave;*.WAV;*.WAVE;*.Wav;*.Wave"
        dlg = wx.FileDialog(self, message="Choose a new soundfile...", 
                            wildcard=wildcard, style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if path != "":
                self.switcher.changeTable(path)
        dlg.Destroy()        

    def changeFx(self, evt):
        self.switcher.changeFx(evt.GetString()) 

    def changeParams(self, x, y):
        # fonction appelee par le "callback" de la surface de controle
        self.switcher.changeP1(x)
        self.switcher.changeP2(y)

app = wx.App()

fxswitch = FxSwitch()

mainFrame = MyFrame(switcher=fxswitch)
mainFrame.Show()

app.MainLoop()