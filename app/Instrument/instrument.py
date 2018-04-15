from pyo import *
import pyo
from random import uniform
sys.path.insert(0, '/home/vincent/Documents/univ/hiver2018/mus3325/git/MUS3325X/app/Effect')
import effect


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
        s.setMidiInputDevice(9999)
        s.boot()
        self.note = Notein(poly=10, scale=1, first=0, last=127)
        self.ctl = Midictl(1, minscale=0, maxscale=2)#Modulo
        self.bend = Bendin(brange=2, scale=1) # Pitch bend
        self.lf = Sine(freq=5, mul=self.ctl, add=1) # Vibrato
        self.vol = Midictl(ctlnumber=7, minscale=0, maxscale=2)
        self.amp = Port(self.vol, .02)
        self.a1 = Sinein(self.note , transpo = self.lf * self.bend, amp=self.amp)
        self.a = pyo.CtlScan2(self.ctl_scan)
        self.a.setFunction(ctl_scan)
        self.effect = [self.a1]
        self.midiCtls = [[self.vol]]
        self.ports = [[self.amp]]
        self.out = self.effect[len(self.effect)-1].out()
    def ctl_scan(ctlnum):
        print("test")
    def start(self):
        self.out.out()
        s.start()
    def stop(self):
        self.out.stop()
    def exit(self):
        s.stop()
    def resetCtl():
        ctl=[]
    def addEffect(self,eff):
        if eff == "Disto":
            popped = 0
            if(len(ctl)>=3):
                popped1=ctl.pop(0)
                popped2=ctl.pop(0)
                popped3=ctl.pop(0)
                usedCtl.append([popped1,popped2,popped3])
                self.midiCtls.append([Midictl(ctlnumber=popped1, minscale=0, maxscale=1),
                                      Midictl(ctlnumber=popped2, minscale=0, maxscale=1),
                                      Midictl(ctlnumber=popped3, minscale=0, maxscale=1)])
                self.ports.append([Port(self.midiCtls[len(self.midiCtls)-1][0], .02),
                                   Port(self.midiCtls[len(self.midiCtls)-1][1], .02),
                                   Port(self.midiCtls[len(self.midiCtls)-1][2], .02)])
                self.stop()
                tmp = self.effect[len(self.effect)-1].sig
                tmp = effect.Disto_(tmp, self.ports[len(self.ports)-1])
                self.effect.append(tmp)
                self.out = self.effect[len(self.effect)-1].out()
                self.start()
    def removeEffect(self,index):
        self.ports.pop(index)
        self.midiCtls.pop(index)
        ctl.extend(usedCtl.pop(index))
        self.effect.pop(index)
        self.out = self.effect[len(self.effect)-1].out()

        
        
            
        
class Instrument():
    def __init__(self,note,ctl,transpo,amp):
        self.ctl=ctl
        self.transpo = Sig(transpo)
        self.note = note
        self.freq = self.note['pitch'] * self.transpo
        self.amp = MidiAdsr(self.note['velocity'], attack=0.001, 
                            decay=.1, sustain=.7, release=1, mul=.3)*amp
        self.output = PyoObject()
        self.sig = PyoObject()
    def out(self):
        print("start")
        self.output.out()
        return self
    def stop(self):
        print("stop")
        self.output.stop()
        return self
    def sig(self):
        return self.sig

class Defaut(Instrument):
    def __init__(self, note, ctl=[74,71,81,91,16,80,19,2],transpo=2,amp=1):
        Instrument.__init__(self,note,ctl,transpo,amp)
        self.osc1 = LFO(freq=self.freq, sharp=0.25, mul=self.amp).mix(1)
        self.osc2 = LFO(freq=self.freq*0.997, sharp=0.25, mul=self.amp).mix(1)
        self.osc3 = LFO(freq=self.freq*1.004, sharp=0.25, mul=self.amp).mix(1)
        self.osc4 = LFO(freq=self.freq*1.009, sharp=0.25, mul=self.amp).mix(1)
        self.sig=([self.osc1+self.osc3, self.osc2+self.osc4])
        # Mix stereo (osc1 et osc3 a gauche, osc2 et osc4 a droite)
        self.mix = Mix(self.sig, voices=2)
        # Distortion avec LFO sur le drive
        self.lfo = Sine(freq=uniform(.2,.4), mul=0.45, add=0.5)
        self.disto = Disto(self.mix, drive=self.lfo, slope=0.95, mul=.5)
        self.output=self.disto
        
class Sinein(Instrument):
    def __init__(self, note, ctl=[74,71,81,91,16,80,19,2],transpo=2,amp=1):
        Instrument.__init__(self,note,ctl,transpo,amp)
        self.sine=Sine(freq=self.freq, phase=0, mul=self.amp, add=0).mix(1)
        self.mix=Mix([self.sine,self.sine],voices=2)
        self.output=self.mix
        self.sig=[self.sine,self.sine]

