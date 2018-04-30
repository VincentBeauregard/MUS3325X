#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

#Variable global des instruments et effet disponnible
effectList = [  ("Disto"),
                ("Delay"),
                ("SDelay"),
                ("Delay1"),
                ("Waveguide"),
                ("AllpassWG"),
                ("Freeverb"),
                ("WGVerb"),
                ("Chorus"),
                ("Harmonizer"),
                ("FreqShift"),
                ("STRev"),
                ("SmoothDelay")
            ]
instruList = [  ("defaut"),
                ("sinein"),
                ("auxin"),
                ("synthandy"),
                ("pyotoolsfatbass")
            ]

    
    
    
    
    
    
    
    
    
    
#class generer automatiquement en quasi totalite par wxGlade, contient l'affichage du gui wx 

class MyFrame(wx.Frame):
    def __init__(self,synth, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.start_stop = wx.Button(self, wx.ID_ANY, _("Start/Stop"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Play/Pause"))
        self.instru_box = wx.ComboBox(self, wx.ID_ANY, choices=instruList, style=wx.CB_DROPDOWN)
        self.instruSlider = []
        self.instruRadio = []
        self.instruInputBox = []
        self.effectSlider = []
        self.effectRadio = []
        self.effectInputBox = []
        self.instruSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127, style=wx.SL_INVERSE | wx.SL_VERTICAL))
        self.instruRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.instruInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.instruSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127, style=wx.SL_INVERSE | wx.SL_VERTICAL))
        self.instruRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.instruInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.instruSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127, style=wx.SL_INVERSE | wx.SL_VERTICAL))
        self.instruRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.instruInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.instruSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127, style=wx.SL_INVERSE | wx.SL_VERTICAL))
        self.instruRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.instruInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.instruSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127, style=wx.SL_INVERSE | wx.SL_VERTICAL))
        self.instruRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.instruInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.slider_pan = wx.Slider(self, wx.ID_ANY, 0, 0, 127)
        self.checkbox_pan = wx.CheckBox(self, wx.ID_ANY, _("input"))
        self.combo_box_pan = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.effectSelectBox = wx.ComboBox(self, wx.ID_ANY, choices=effectList, style=wx.CB_DROPDOWN)
        self.addEffectFirst_btn = wx.Button(self, wx.ID_ANY, _("AddFirst"))
        self.addEffectLast_btn = wx.Button(self, wx.ID_ANY, _("AddLast"))
        self.addEffectIndex_btn = wx.Button(self, wx.ID_ANY, _("AddAtIndex"))
        self.indexSpin = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=100)
        self.effectName = wx.TextCtrl(self, wx.ID_ANY, "")
        self.myEffectBox = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.effectSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127))
        self.effectRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.effectInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.effectSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127))
        self.effectRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.effectInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.effectSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127))
        self.effectRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.effectInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.effectSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127))
        self.effectRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.effectInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.effectSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127))
        self.effectRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.effectInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.effectSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127))
        self.effectRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.effectInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.effectSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127))
        self.effectRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.effectInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.effectSlider.append(wx.Slider(self, wx.ID_ANY, 0, 0, 127))
        self.effectRadio.append(wx.CheckBox(self, wx.ID_ANY, _("input")))
        self.effectInputBox.append(wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN))
        self.removeEffect_btn = wx.Button(self, wx.ID_ANY, _("Remove"))
        self.refresh_btn = wx.Button(self, wx.ID_ANY, _("Refresh Inputs"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.startstop, self.start_stop)
        self.Bind(wx.EVT_BUTTON, self.playpause, self.button_2)
        self.Bind(wx.EVT_COMBOBOX, self.selectInstru, self.instru_box)
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideInstru1, self.instruSlider[0])
        self.Bind(wx.EVT_CHECKBOX, self.radio_instru1, self.instruRadio[0])

        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideInstru2, self.instruSlider[1])
        self.Bind(wx.EVT_CHECKBOX, self.radio_instru2, self.instruRadio[1])

        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideInstru3, self.instruSlider[2])
        self.Bind(wx.EVT_CHECKBOX, self.radio_instru3, self.instruRadio[2])

        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideInstru4, self.instruSlider[3])
        self.Bind(wx.EVT_CHECKBOX, self.radio_instru4, self.instruRadio[3])

        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideInstru5, self.instruSlider[4])
        self.Bind(wx.EVT_CHECKBOX, self.radio_instru5, self.instruRadio[4])

        self.Bind(wx.EVT_BUTTON, self.addeffectfirst, self.addEffectFirst_btn)
        self.Bind(wx.EVT_BUTTON, self.addeffectlast, self.addEffectLast_btn)
        self.Bind(wx.EVT_BUTTON, self.addeffectAtIndex, self.addEffectIndex_btn)
        self.Bind(wx.EVT_COMBOBOX, self.selectedEffect, self.myEffectBox)
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideEffect1, self.effectSlider[0])
        self.Bind(wx.EVT_CHECKBOX, self.radio_effect1, self.effectRadio[0])
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideEffect2, self.effectSlider[1])
        self.Bind(wx.EVT_CHECKBOX, self.radio_effect2, self.effectRadio[1])
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideEffect3, self.effectSlider[2])
        self.Bind(wx.EVT_CHECKBOX, self.radio_effect3, self.effectRadio[2])
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideEffect4, self.effectSlider[3])
        self.Bind(wx.EVT_CHECKBOX, self.radio_effect4, self.effectRadio[3])
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideEffect5, self.effectSlider[4])
        self.Bind(wx.EVT_CHECKBOX, self.radio_effect5, self.effectRadio[4])
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideEffect6, self.effectSlider[5])
        self.Bind(wx.EVT_CHECKBOX, self.radio_effect6, self.effectRadio[5])
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideEffect7, self.effectSlider[6])
        self.Bind(wx.EVT_CHECKBOX, self.radio_effect7, self.effectRadio[6])
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideEffect8, self.effectSlider[7])
        self.Bind(wx.EVT_CHECKBOX, self.radio_effect8, self.effectRadio[7])
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slideEffect8, self.effectSlider[7])
        self.Bind(wx.EVT_CHECKBOX, self.radio_effect8, self.effectRadio[7])
        self.Bind(wx.EVT_COMMAND_SCROLL, self.slidePan, self.slider_pan)
        self.Bind(wx.EVT_CHECKBOX, self.radioPan, self.checkbox_pan)
        self.Bind(wx.EVT_BUTTON, self.removeEffec, self.removeEffect_btn)
        self.Bind(wx.EVT_BUTTON, self.refreshInput, self.refresh_btn)
        # end wxGlade
        

        #Ajout de gestion a l'initialisation
        #added by me
        self.activated=False
        self.paused=False
        self.effect=[]
        self.slideEffect = [0,0,0,0,0,0,0,0]
        
        self.synth=synth
        self.slideInstru = [[-1,self.synth.instrument.setMul],
                            [-1,self.synth.masterCtl[2].setMul],
                            [-1,self.synth.masterCtl[0].setFreq],
                            [-1,self.synth.masterCtl[1].setFreq],
                            [-1,self.synth.masterCtl[2].setFreq],
                            [-1,self.synth.masterCtl[3].setPan]]
                            
        self.ctl=synth.getCtl()[:]
        self.indexSpin.SetRange(0,0)
        for i in range(8):
            self.effectSlider[i].Enable(False) 
            self.effectInputBox[i].Enable(False) 
            self.effectRadio[i].Enable(False) 
        for i in range(5):
            self.instruSlider[i].Enable(False) 
            self.instruInputBox[i].Enable(False) 
            self.instruRadio[i].Enable(False) 
        self.checkbox_pan.Enable(False) 
        self.slider_pan.Enable(False) 
        self.combo_box_pan.Enable(False) 
        
    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("frame_1"))
        self.instruSlider[0].SetMinSize((80, 200))
        self.instruInputBox[0].SetMinSize((62, 31))
        self.instruSlider[1].SetMinSize((80, 200))
        self.instruInputBox[1].SetMinSize((62, 31))
        self.instruSlider[2].SetMinSize((80, 200))
        self.instruInputBox[2].SetMinSize((62, 31))
        self.instruSlider[3].SetMinSize((80, 200))
        self.instruInputBox[3].SetMinSize((62, 31))
        self.instruSlider[4].SetMinSize((79, 200))
        self.instruInputBox[4].SetMinSize((62, 31))      
        self.slider_pan.SetMinSize((200, 80))
        self.combo_box_pan.SetMinSize((62, 31))
        self.effectSelectBox.SetSelection(-1)
        self.addEffectIndex_btn.SetMinSize((86, 30))
        self.indexSpin.SetMinSize((62, 31))
        self.myEffectBox.SetSelection(-1)
        self.effectSlider[0].SetMinSize((150, 30))
        self.effectInputBox[0].SetMinSize((62, 31))
        self.effectSlider[1].SetMinSize((150, 30))
        self.effectInputBox[1].SetMinSize((62, 31))
        self.effectSlider[2].SetMinSize((150, 30))
        self.effectInputBox[2].SetMinSize((62, 31))
        self.effectSlider[3].SetMinSize((150, 30))
        self.effectInputBox[3].SetMinSize((62, 31))
        self.panel_1.SetMinSize((136,31))
        self.effectSlider[4].SetMinSize((150, 30))
        self.effectInputBox[4].SetMinSize((62, 31))
        self.effectSlider[5].SetMinSize((150, 30))
        self.effectInputBox[5].SetMinSize((62, 31))
        self.effectSlider[6].SetMinSize((150, 30))
        self.effectInputBox[6].SetMinSize((62, 31))
        self.effectSlider[7].SetMinSize((150, 30))
        self.effectInputBox[7].SetMinSize((62, 31))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("My Effects")), wx.HORIZONTAL)
        sizer_27_copy_copy_1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_effect = []
        self.sizer_instru = []
        self.sizer_effect.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("label")), wx.VERTICAL))
        sizer_29_copy_2_copy_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_effect.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("label")), wx.VERTICAL))
        sizer_29_copy_3_copy_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_effect.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("label")), wx.VERTICAL))
        sizer_29_copy_4_copy_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_effect.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("label")), wx.VERTICAL))
        sizer_29_copy_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_27_copy_copy = wx.BoxSizer(wx.VERTICAL)
        self.sizer_effect.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("label")), wx.VERTICAL))
        sizer_29_copy_5_copy_copy = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_effect.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("label")), wx.VERTICAL))
        sizer_29_copy_6_copy_copy = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_effect.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("label")), wx.VERTICAL))
        sizer_29_copy_7_copy_copy = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_effect.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("label")), wx.VERTICAL))
        sizer_29_copy_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Effect")), wx.VERTICAL)
        sizer_26 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Name :")), wx.HORIZONTAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("sizer_3")), wx.VERTICAL)
        sizer_6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Pan")), wx.HORIZONTAL)
        sizer_22 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_instru.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Midi Volume")), wx.VERTICAL))
        sizer_17_copy_2_copy_copy_3 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_instru.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Master Volume")), wx.VERTICAL))
        sizer_17_copy_2_copy_copy_2 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_instru.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Treble")), wx.VERTICAL))
        sizer_17_copy_2_copy_copy_1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_instru.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Bass")), wx.VERTICAL))
        sizer_17_copy_2_copy_copy = wx.BoxSizer(wx.VERTICAL)
        self.sizer_instru.append(wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("middle")), wx.VERTICAL))
        sizer_17_copy_2_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.start_stop, 0, 0, 0)
        sizer_4.Add(self.button_2, 0, 0, 0)
        sizer_3.Add(sizer_4, 0, 0, 0)
        sizer_3.Add(self.instru_box, 0, 0, 0)
        self.sizer_instru[0].Add(self.instruSlider[0], 0, wx.ALIGN_CENTER, 0)
        sizer_17_copy_2_copy.Add(self.instruRadio[0], 0, wx.EXPAND, 0)
        sizer_17_copy_2_copy.Add(self.instruInputBox[0], 0, wx.ALL, 0)
        self.sizer_instru[0].Add(sizer_17_copy_2_copy, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_5.Add(self.sizer_instru[0], 0, wx.ALIGN_CENTER, 0)
        self.sizer_instru[1].Add(self.instruSlider[1], 0, wx.ALIGN_CENTER, 0)
        sizer_17_copy_2_copy_copy.Add(self.instruRadio[1], 0, wx.EXPAND, 0)
        sizer_17_copy_2_copy_copy.Add(self.instruInputBox[1], 0, wx.ALL, 0)
        self.sizer_instru[1].Add(sizer_17_copy_2_copy_copy, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_5.Add(self.sizer_instru[1], 0, wx.ALIGN_CENTER, 0)
        self.sizer_instru[2].Add(self.instruSlider[2], 0, wx.ALIGN_CENTER, 0)
        sizer_17_copy_2_copy_copy_1.Add(self.instruRadio[2], 0, wx.EXPAND, 0)
        sizer_17_copy_2_copy_copy_1.Add(self.instruInputBox[2], 0, wx.ALL, 0)
        self.sizer_instru[2].Add(sizer_17_copy_2_copy_copy_1, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_5.Add(self.sizer_instru[2], 0, wx.ALIGN_CENTER, 0)
        self.sizer_instru[3].Add(self.instruSlider[3], 0, wx.ALIGN_CENTER, 0)
        sizer_17_copy_2_copy_copy_2.Add(self.instruRadio[3], 0, wx.EXPAND, 0)
        sizer_17_copy_2_copy_copy_2.Add(self.instruInputBox[3], 0, wx.ALL, 0)
        self.sizer_instru[3].Add(sizer_17_copy_2_copy_copy_2, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_5.Add(self.sizer_instru[3], 0, wx.ALIGN_CENTER, 0)
        self.sizer_instru[4].Add(self.instruSlider[4], 0, wx.ALIGN_CENTER, 0)
        sizer_17_copy_2_copy_copy_3.Add(self.instruRadio[4], 0, wx.EXPAND, 0)
        sizer_17_copy_2_copy_copy_3.Add(self.instruInputBox[4], 0, wx.ALL, 0)
        self.sizer_instru[4].Add(sizer_17_copy_2_copy_copy_3, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_5.Add(self.sizer_instru[4], 0, wx.ALIGN_CENTER, 0)
        sizer_3.Add(sizer_5, 1, 0, 0)
        sizer_12.Add(self.slider_pan, 0, 0, 0)
        sizer_12.Add(self.refresh_btn, 0, 0, 0)
        sizer_6.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_22.Add(self.checkbox_pan, 0, 0, 0)
        sizer_22.Add(self.combo_box_pan, 0, 0, 0)
        sizer_6.Add(sizer_22, 1, 0, 0)
        sizer_3.Add(sizer_6, 1, 0, 0)
        sizer_2.Add(sizer_3, 1, wx.ALL | wx.EXPAND, 0)
        sizer_24.Add(self.effectSelectBox, 0, 0, 0)
        sizer_24.Add(self.addEffectFirst_btn, 0, 0, 0)
        sizer_24.Add(self.addEffectLast_btn, 0, 0, 0)
        sizer_25.Add(self.addEffectIndex_btn, 0, 0, 0)
        sizer_25.Add(self.indexSpin, 0, 0, 0)
        sizer_24.Add(sizer_25, 0, 0, 0)
        sizer_26.Add(self.effectName, 0, 0, 0)
        sizer_24.Add(sizer_26, 0, 0, 0)
        sizer_23.Add(sizer_24, 0, 0, 0)
        sizer_27_copy_copy.Add(self.myEffectBox, 0, 0, 0)
        self.sizer_effect[0].Add(self.effectSlider[0], 0, 0, 0)
        sizer_29_copy_copy.Add(self.effectRadio[0], 0, 0, 0)
        sizer_29_copy_copy.Add(self.effectInputBox[0], 0, 0, 0)
        self.sizer_effect[0].Add(sizer_29_copy_copy, 1, 0, 0)
        sizer_27_copy_copy.Add(self.sizer_effect[0], 1, 0, 0)
        self.sizer_effect[1].Add(self.effectSlider[1], 0, 0, 0)
        sizer_29_copy_7_copy_copy.Add(self.effectRadio[1], 0, 0, 0)
        sizer_29_copy_7_copy_copy.Add(self.effectInputBox[1], 0, 0, 0)
        self.sizer_effect[1].Add(sizer_29_copy_7_copy_copy, 1, 0, 0)
        sizer_27_copy_copy.Add(self.sizer_effect[1], 1, 0, 0)
        self.sizer_effect[2].Add(self.effectSlider[2], 0, 0, 0)
        sizer_29_copy_6_copy_copy.Add(self.effectRadio[2], 0, 0, 0)
        sizer_29_copy_6_copy_copy.Add(self.effectInputBox[2], 0, 0, 0)
        self.sizer_effect[2].Add(sizer_29_copy_6_copy_copy, 1, 0, 0)
        sizer_27_copy_copy.Add(self.sizer_effect[2], 1, 0, 0)
        self.sizer_effect[3].Add(self.effectSlider[3], 0, 0, 0)
        sizer_29_copy_5_copy_copy.Add(self.effectRadio[3], 0, 0, 0)
        sizer_29_copy_5_copy_copy.Add(self.effectInputBox[3], 0, 0, 0)
        self.sizer_effect[3].Add(sizer_29_copy_5_copy_copy, 1, 0, 0)
        sizer_27_copy_copy.Add(self.sizer_effect[3], 1, 0, 0)
        sizer_13.Add(sizer_27_copy_copy, 1, 0, 0)
        sizer_27_copy_copy_1.Add(self.panel_1, 0, wx.ALL | wx.EXPAND, 0)
        self.sizer_effect[4].Add(self.effectSlider[4], 0, 0, 0)
        sizer_29_copy_copy_1.Add(self.effectRadio[4], 0, 0, 0)
        sizer_29_copy_copy_1.Add(self.effectInputBox[4], 0, 0, 0)
        self.sizer_effect[4].Add(sizer_29_copy_copy_1, 1, 0, 0)
        sizer_27_copy_copy_1.Add(self.sizer_effect[4], 1, 0, 0)
        self.sizer_effect[5].Add(self.effectSlider[5], 0, 0, 0)
        sizer_29_copy_4_copy_copy_1.Add(self.effectRadio[5], 0, 0, 0)
        sizer_29_copy_4_copy_copy_1.Add(self.effectInputBox[5], 0, 0, 0)
        self.sizer_effect[5].Add(sizer_29_copy_4_copy_copy_1, 1, 0, 0)
        sizer_27_copy_copy_1.Add(self.sizer_effect[5], 1, 0, 0)
        self.sizer_effect[6].Add(self.effectSlider[6], 0, 0, 0)
        sizer_29_copy_3_copy_copy_1.Add(self.effectRadio[6], 0, 0, 0)
        sizer_29_copy_3_copy_copy_1.Add(self.effectInputBox[6], 0, 0, 0)
        self.sizer_effect[6].Add(sizer_29_copy_3_copy_copy_1, 1, 0, 0)
        sizer_27_copy_copy_1.Add(self.sizer_effect[6], 1, 0, 0)
        self.sizer_effect[7].Add(self.effectSlider[7], 0, 0, 0)
        sizer_29_copy_2_copy_copy_1.Add(self.effectRadio[7], 0, 0, 0)
        sizer_29_copy_2_copy_copy_1.Add(self.effectInputBox[7], 0, 0, 0)
        self.sizer_effect[7].Add(sizer_29_copy_2_copy_copy_1, 1, 0, 0)
        sizer_27_copy_copy_1.Add(self.sizer_effect[7], 1, 0, 0)
        sizer_27_copy_copy_1.Add(self.removeEffect_btn, 0, 0, 0)
        sizer_13.Add(sizer_27_copy_copy_1, 1, 0, 0)
        sizer_23.Add(sizer_13, 0, 0, 0)
        sizer_2.Add(sizer_23, 0, 0, 0)
        sizer_1.Add(sizer_2, 1, 0, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

####

###La suite du fichier contient toutes les fonctions communiquant avec les autres classes

    #Demarre le serveur ou l'arrete
    def startstop(self, event):  # wxGlade: MyFrame.<event_handler>
        if not self.activated:
            self.synth.start("defaut")
            self.activated=True
            self.selectedInstru()
            for i in range(5):
                self.instruSlider[i].Enable(True) 
                self.instruInputBox[i].Enable(True) 
                self.instruRadio[i].Enable(True) 
            self.checkbox_pan.Enable(True) 
            self.slider_pan.Enable(True) 
            self.combo_box_pan.Enable(True) 
        else:
            self.synth.stop()
            self.activated=False
            for i in range(5):
                self.instruSlider[i].Enable(False) 
                self.instruInputBox[i].Enable(False) 
                self.instruRadio[i].Enable(False) 
            self.checkbox_pan.Enable(False) 
            self.slider_pan.Enable(False) 
            self.combo_box_pan.Enable(False) 
        self.refreshCtl()
        event.Skip()

    #arrete le signal de sortie, ou le redemarre
    def playpause(self, event):  # wxGlade: MyFrame.<event_handler>
        if self.activated and not self.paused:
            self.synth.pause()
            self.paused=True
        elif self.activated and self.paused:
            self.synth.resume()
            self.paused=False
        event.Skip()

    #change l'instrument sur selection
    def selectInstru(self, event):  # wxGlade: MyFrame.<event_handler>
        self.synth.changeInstrument(self.instru_box.GetStringSelection())
        event.Skip()


    
    ###ajoute d'effet a une position donnee###
    def addeffectfirst(self, event):  # wxGlade: MyFrame.<event_handler>
        self.addEffect(0)
        event.Skip()

    def addeffectlast(self, event):  # wxGlade: MyFrame.<event_handler>
        self.addEffect(len(self.synth.effectOrder))
        
    def addeffectAtIndex(self, event):  # wxGlade: MyFrame.<event_handler>
        self.addEffect(int(self.indexSpin.GetValue()))
        event.Skip()
    def addEffect(self,pos):
        if(self.effectSelectBox.GetSelection() != -1):
            print(self.effectName.GetValue())
            added=False
            index = 0
            txt=self.effectName.GetValue()
            if(txt == ""):
                txt=self.effectSelectBox.GetValue()
            while(not added):
                tmp = txt + str(index)
                if tmp in self.effect :
                    index +=1
                else:
                    self.effect.append(tmp)
                    added = True
            self.synth.addEffect(self.effectSelectBox.GetValue(),txt+str(index),pos)
            txt=self.effectName.SetValue("")
            self.effectSelectBox.SetValue("")
            self.myEffectBox.Clear()
            self.indexSpin.SetRange(0,len(self.synth.effectOrder))
            for i in self.synth.effectOrder:
                self.myEffectBox.Append(i)
######

    ###Selection de l'effet
    def selectedEffect(self, event):  # wxGlade: MyFrame.<event_handler>
        self.refreshCtl()
        self.resetEnable()
        self.inputs = self.synth.effects[self.myEffectBox.GetValue()].keys
        self.parametre = self.synth.effects[self.myEffectBox.GetValue()].parametre
        for i in range(len(self.inputs)):
            self.slideEffect[i] = (self.parametre[self.inputs[i]])
            if(self.slideEffect[i][4] == -1):
                self.effectSlider[i].Enable(True)
                self.effectInputBox[i].Enable(True)
            else:
                self.effectRadio[i].SetValue(True)
                self.effectInputBox[i].SetValue(str(self.slideEffect[i][4]))
            self.effectRadio[i].Enable(True)
            self.sizer_effect[i].GetStaticBox().SetLabel(self.inputs[i])
            vals = self.parametre[self.inputs[i]]
            value = 127*(vals[1]-vals[2])/(vals[3]-vals[2])
            self.effectSlider[i].SetValue(value)
        event.Skip()
        
    ###lors de l'initialisation de l'instrument
    def selectedInstru(self):  # wxGlade: MyFrame.<event_handler>
        for i in range(5):
            if(self.slideInstru[i][0] == -1):
                self.instruSlider[i].Enable(True)
                self.instruInputBox[i].Enable(True)
            else:
                self.instruRadio[i].SetValue(True)
                self.instruInputBox[i].SetValue(str(self.slideInstru[i][0]))
            self.instruRadio[i].Enable(True)
            self.instruSlider[i].SetValue(int(127*0.5))
        
   
    ###Gestion des sliders
    def sliderEffect(self,event,i):
        x = event.GetInt()
        x = changeRange(0,127,self.slideEffect[i][2],self.slideEffect[i][3],x)
        self.slideEffect[i][1]=x
        self.slideEffect[i][0](x)
        print(x)
        event.Skip()
        
    def sliderInstru(self,event,i):
        x = event.GetInt()
        if i<2:
            x = changeRange(0,127,0,2,x)
        else:
            x = changeRange(0,127,50,5000,x)
        self.slideInstru[i][1](x)
        print(x)
        event.Skip()
        
    def slidePan(self,event):
        x = event.GetInt()
        x = changeRange(0,127,0,1,x)
        self.slideInstru[5][1](x)
        print(x)
        event.Skip()
    #####
    ###Gestion des checkbox lors de selection de input
    def radio_effect(self,x):
        if(self.effectRadio[x].GetValue()):
            if(self.effectInputBox[x].GetSelection() is not -1):
                self.synth.useCtl(int(self.effectInputBox[x].GetValue()),self.parametre[self.inputs[x]][2],self.parametre[self.inputs[x]][3],self.parametre[self.inputs[x]][0])
                self.effectSlider[x].Enable(False)
                self.effectInputBox[x].Enable(False)
                self.slideEffect[x][4]=int(self.effectInputBox[x].GetValue())
            else:
                self.effectRadio[x].SetValue(False)
            
        else:
            self.effectSlider[x].Enable(True)
            self.effectInputBox[x].Enable(True)
            self.effectSlider[x].SetValue(changeRange(0,1,0,127,0.5))
            changeRange(0,1,self.slideEffect[x][2],self.slideEffect[x][3],0.5)
            self.synth.freeCtl(self.slideEffect[x][4])
            self.slideEffect[x][4]=-1
            self.effectInputBox[x].SetValue("")
        self.refreshCtl()
        
    def radio_instru(self,x,min,max,fn):
        if(self.instruRadio[x].GetValue()):
            if(self.instruInputBox[x].GetSelection() is not -1):
                self.synth.useCtl(int(self.instruInputBox[x].GetValue()),min,max,fn)
                self.instruSlider[x].Enable(False)
                self.instruInputBox[x].Enable(False)
                self.slideInstru[x][0]=int(self.instruInputBox[x].GetValue())
            else:
                self.instruRadio[x].SetValue(False)
            
        else:
            self.instruSlider[x].Enable(True)
            self.instruInputBox[x].Enable(True)
            self.instruSlider[x].SetValue(changeRange(0,1,0,127,0.5))
            self.synth.freeCtl(self.slideInstru[x][0])
            self.slideInstru[x][0]=-1
            fn(changeRange(0,1,min,max,0.5))
            self.instruInputBox[x].SetValue("")
        self.refreshCtl()
        
    def radioPan(self,event):
        if(self.checkbox_pan.GetValue()):
            if(self.combo_box_pan.GetSelection() is not -1):
                self.synth.useCtl(int(self.combo_box_pan.GetValue()),0,1,self.slideInstru[5][1])
                self.slider_pan.Enable(False)
                self.combo_box_pan.Enable(False)
                self.slideInstru[5][0]=int(self.combo_box_pan.GetValue())
            else:
                self.checkbox_pan.SetValue(False)
            
        else:
            self.slider_pan.Enable(True)
            self.combo_box_pan.Enable(True)
            self.slider_pan.SetValue(changeRange(0,1,0,127,0.5))
            self.synth.freeCtl(self.slideInstru[5][0])
            self.slideInstru[5][0]=-1
            self.slideInstru[5][1](int(127/2))
            self.combo_box_pan.SetValue("")
        self.refreshCtl()
        event.Skip()
        #####

    ### retire l'effet selectionner
    def removeEffec(self, event):  # wxGlade: MyFrame.<event_handler>
        if(self.myEffectBox.GetSelection() is not -1):
            for i in range(8):
                if(self.effectRadio[i].GetValue()):
                    self.effectRadio[i].SetValue(False)
                    self.radio_effect(i)
            self.synth.removeEffect(self.myEffectBox.GetValue())
            self.myEffectBox.SetValue("")
            self.resetEnable()
            self.myEffectBox.Clear()
            self.indexSpin.SetRange(0,len(self.synth.effectOrder))
            for i in self.synth.effectOrder:
                self.myEffectBox.Append(i)
            self.myEffectBox.SetValue("")
            
                
        event.Skip()
    ### rafraichit les inputs
    def refreshInput(self,event):
        self.refreshCtl()
        event.Skip()
    def refreshCtl(self):
        ctl = self.synth.getCtl()
        ctlToAdd =[]
        for j in self.ctl:
            if(j in ctl):
                ctlToAdd.append(str(j))
        for j in ctl:
            if(j not in self.ctl):
                ctlToAdd.append(str(j))
        print(ctlToAdd)
        for i in range(8):
            self.effectInputBox[i].Clear()
            for j in ctlToAdd:
                self.effectInputBox[i].Append(j)
        for i in range(5):
            self.instruInputBox[i].Clear()
            for j in ctlToAdd:
                self.instruInputBox[i].Append(j)
        self.combo_box_pan.Clear()
        for j in ctlToAdd:
            self.combo_box_pan.Append(j)
####

    ###met a jour les valeur disponnilbe pour les effets
    def resetEnable(self):
        for i in range(8):
            self.effectSlider[i].Enable(False) 
            self.effectInputBox[i].Enable(False) 
            self.effectRadio[i].Enable(False)
            self.effectRadio[i].SetValue(False)
            self.effectInputBox[i].SetValue("")
            

    ###Rassemblement de fonction de simplification
    def slideEffect1(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderEffect(event,0)
    def slideEffect2(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderEffect(event,1)
    def slideEffect3(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderEffect(event,2)
    def slideEffect4(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderEffect(event,3)
    def slideEffect5(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderEffect(event,4)
    def slideEffect6(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderEffect(event,5)
    def slideEffect7(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderEffect(event,6)
    def slideEffect8(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderEffect(event,7)
        
    def slideInstru1(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderInstru(event,0)
    def slideInstru2(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderInstru(event,1)
    def slideInstru3(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderInstru(event,2)
    def slideInstru4(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderInstru(event,3)
    def slideInstru5(self, event):  # wxGlade: MyFrame.<event_handler>
        self.sliderInstru(event,4)
        
    def radio_effect1(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_effect(0)
    def radio_effect2(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_effect(1)
    def radio_effect3(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_effect(2)
    def radio_effect4(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_effect(3)
    def radio_effect5(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_effect(4)
    def radio_effect6(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_effect(5)
    def radio_effect7(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_effect(6)
    def radio_effect8(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_effect(7)
        
    def radio_instru1(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_instru(0,0,2,self.synth.instrument.setMul)
    def radio_instru2(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_instru(1,0,2,self.synth.masterCtl[2].setMul)
    def radio_instru3(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_instru(2,50,5000,self.synth.masterCtl[0].setFreq)
    def radio_instru4(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_instru(3,50,5000,self.synth.masterCtl[1].setFreq)
    def radio_instru5(self, event):  # wxGlade: MyFrame.<event_handler>
        self.radio_instru(4,50,5000,self.synth.masterCtl[2].setFreq)
        

def changeRange(minIn,maxIn,minOut,maxOut,valIn):
    value = ((float(maxOut)-float(minOut))*(float(valIn)-float(minIn))/(float(maxIn)-float(minIn)))+float(minOut)
    return value
# end of class MyFrame
def run(synth):
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp()
    frame_3 = MyFrame(synth, None, wx.ID_ANY, "")
    app.SetTopWindow(frame_3)
    frame_3.Show()
    app.MainLoop()
    


