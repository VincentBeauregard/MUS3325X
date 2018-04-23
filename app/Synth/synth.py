from pyo import *
import pyo
from random import uniform
sys.path.insert(0, '/home/vincent/Documents/univ/hiver2018/mus3325/git/MUS3325X/app/Effect')
import effect
sys.path.insert(0, '/home/vincent/Documents/univ/hiver2018/mus3325/git/MUS3325X/app/Instrument')
from instrument import *


s = Server()

ctl = [74,71,81,91,16,80,19,2]
usedCtl=[[1,7]]
def ctl_scan(ctlnum,v1):
    if(ctlnum not in ctl and ctlnum not in usedCtl ):
        ctl.append(ctlnum)
    print(ctl)
outt=0
class Synth:
    def __init__(self,input):
        global usedCtl, ctl
        s.setMidiInputDevice(3)
        s.boot()
        self.note = Notein(poly=10, scale=1, first=0, last=127)
        self.ctl = Midictl(1, minscale=0, maxscale=2)
        self.bend = Bendin(brange=2, scale=1)
        self.lf = Sine(freq=5, mul=self.ctl, add=1)
        self.vol = Midictl(ctlnumber=7, minscale=0, maxscale=2)
        self.amp = Port(self.vol, .02)
        self.instrument = Defaut(self.note , transpo = self.lf * self.bend, amp=self.amp)
        self.a = pyo.CtlScan2(self.ctl_scan)
        self.a.setFunction(ctl_scan)
        self.effects = {}
        self.effectOrder = []
        self.midiCtls = {}
        self.ports = {}
        self.out = self.instrument
    def ctl_scan(ctlnum):
        print("test")
    def start(self,instrument):
        s.start()
        self.out.out()
    def stop(self):
        self.effects = {}
        self.effectOrder = []
        self.out=self.instrument
        self.out.stop()
        
    def exit(self):
        s.stop()
    def pause(self):
        self.out.stop()
    def resume(self):
        self.out.out()
    def addEffect(self,eff,name,pos):
        print(name)
        self.pause()
        if(len(self.effectOrder)==0):#empty
            self.effects[name]=self.setEffect(eff,self.out.sig)                
            self.effectOrder.append(name)
            self.out = self.effects[name].out()
        elif(len(self.effectOrder)==pos):#add last
            self.effects[name]=self.setEffect(eff,self.effects[self.effectOrder[len(self.effectOrder)-1]].effect)                
            self.effectOrder.append(name)
            self.out = self.effects[name].out()
        elif(pos==0):#add first
            self.effects[name]=self.setEffect(eff,self.instrument.sig)         
            self.effectOrder.insert(pos,name)
            self.effects[self.effectOrder[pos+1]].effect.setInput(self.effects[name].effect)   
            self.out = self.effects[self.effectOrder[len(self.effectOrder)-1]].out()
        elif(pos > 0 and pos < len(self.effectOrder)):
            self.effects[name]=self.setEffect(eff,self.effects[self.effectOrder[pos-1]].effect)          
            self.effectOrder.insert(pos,name)
            self.effects[self.effectOrder[pos+1]].effect.setInput(self.effects[name].effect)  
            self.out = self.effects[self.effectOrder[len(self.effectOrder)-1]].out()
        self.resume()


    def setEffect(self,name,input):
        if(name=="Disto"):
            return effect.Disto_(input)
        elif(name=="Delay"):
            return effect.Delay_(input)
        if(name=="SDelay"):
            return effect.SDelay_(input)
        elif(name=="Delay1"):
            return effect.Delay1_(input)
        if(name=="Waveguide"):
            return effect.Waveguide_(input)
        if(name=="AllpassWG"):
            return effect.AllpassWG_(input)
        elif(name=="Freeverb"):
            return effect.Freeverb_(input)
        if(name=="WGVerb"):
            return effect.WGVerb_(input)
        elif(name=="Chorus"):
            return effect.Chorus_(input)
        if(name=="Harmonizer"):
            return effect.Harmonizer_(input)
        if(name=="FreqShift"):
            return effect.FreqShift_(input)
        elif(name=="STRev"):
            return effect.STRev_(input)
        elif(name=="SmoothDelay"):
            return effect.SmoothDelay_(input)
        
    def removeEffect(self,name):
        index = self.effectOrder.index(name)
        self.pause()
        if(len(self.effectOrder)==1):#alone
            self.effects={}              
            self.effectOrder=[]
            self.out = self.instrument
        elif(len(self.effectOrder)-1==index):#removeLast
            self.out = self.effects[self.effectOrder[index-1]]
            self.effects.pop(name)                
            self.effectOrder.remove(name)
        elif(index==0):#remove first
            self.effects[self.effectOrder[index+1]].effect.setInput(self.instrument.sig)
            self.effects.pop(name)                
            self.effectOrder.remove(name)
        elif(index > 0 and index < len(self.effectOrder)):
            self.effects[self.effectOrder[index+1]].effect.setInput(self.effects[self.effectOrder[index-1]].effect)  
            self.effects.pop(name)                
            self.effectOrder.remove(name)
        self.resume()
    def changeInstrument(self,instrument):
        print(instrument)
        self.pause()
        valide=False
        tmpinstru = PyoObject()
        if(instrument == "defaut"):
            tmpinstru = Defaut(self.note , transpo = self.lf * self.bend, amp=self.amp)
            valide = True
        elif (instrument == 'sinein'):
            tmpinstru = Sinein(self.note , transpo = self.lf * self.bend, amp=self.amp)
            valide = True
        elif (instrument == 'auxin'):
            tmpinstru = AuxIn(self.note , transpo = self.lf * self.bend, amp=self.amp)
            valide = True
        elif (instrument == 'synthandy'):
            tmpinstru = SynthAndy(self.note , transpo = self.lf * self.bend, amp=self.amp)
            valide = True
        elif (instrument == 'pyotoolsfatbass'):
            tmpinstru = pyotoolsfatbass(self.note , transpo = self.lf * self.bend, amp=self.amp)
            valide = True
        if valide:
            if (len(self.effectOrder)!= 0):
                print(self.effectOrder[0])
                del self.instrument
                self.instrument=tmpinstru
                self.effects[self.effectOrder[0]].effect.setInput(self.instrument.sig)
                self.out=self.effects[self.effectOrder[len(self.effectOrder)-1]]
            else:
                self.instrument=tmpinstru
                self.out=self.instrument
        self.resume()
        
    def getCtl(self):
        return ctl
    def useCtl(self,index,min,max,fn):
        self.midiCtls[index]=Midictl(ctlnumber=index, minscale=min, maxscale=max)
        self.ports[index]=Port(self.midiCtls[index], .02)
        fn(self.ports[index])
        ctl.remove(index)
        usedCtl.append(index)
    def freeCtl(self,index):
        self.ports.pop(index)
        self.midiCtls.pop(index)
        ctl.append(index)
        usedCtl.remove(index)
            
