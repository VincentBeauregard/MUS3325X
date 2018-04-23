from pyo import *
from pyotools import *
import pyo
from random import uniform
sys.path.insert(0, '/home/vincent/Documents/univ/hiver2018/mus3325/git/MUS3325X/app/Effect')
import effect
sys.path.insert(0, '/home/vincent/Documents/univ/hiver2018/mus3325/git/MUS3325X/app/Instrument')
import instrument

        
class Instrument():
    def __init__(self,note,ctl,transpo,amp):
        self.ctl=ctl
        self.transpo = Sig(transpo)
        self.note = note
        self.freq = self.note['pitch'] * self.transpo
        self.amp = MidiAdsr(self.note['velocity'], attack=0.01, 
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
        
class AuxIn(Instrument):
    def __init__(self, note, ctl=[74,71,81,91,16,80,19,2],transpo=2,amp=1):
        Instrument.__init__(self,note,ctl,transpo,amp)
        self.sf = Input(mul=amp)
        self.harm = Harmonizer(self.sf, transpo=(self.transpo*10-10), feedback=0, winsize=0.0,mul=amp, add=0)
        self.mix=Mix([self.harm,self.harm],voices=2)
        self.output=self.mix
        self.sig=[self.harm,self.harm]

class SynthAndy(Instrument):
    def __init__(self, note, ctl=[74,71,81,91,16,80,19,2],transpo=2,amp=1):
        Instrument.__init__(self,note,ctl,transpo,amp)
        self.amps = MidiAdsr(note["velocity"], 0.001, 0.01, 0.7, 0.05)
        self.lfo = Sine(5, mul=self.amp, add=1)
        self.synth1 = RCOsc(freq=self.freq*self.lfo, sharp=0.75, mul=self.amp)
        self.synth2 = RCOsc(freq=self.freq*self.lfo*1.01, sharp=0.74, mul=self.amp)
        self.stereo = Mix([self.synth1, self.synth2], voices=2)
        self.rev = STRev(self.stereo, inpos=[0,1], revtime=2, bal=0.25, mul=0.2)
        self.output=self.rev
        self.sig=[self.rev,self.rev]
        
class pyotoolsfatbass(Instrument):
     def __init__(self, note, ctl=[74,71,81,91,16,80,19,2],transpo=2,amp=1):
         Instrument.__init__(self,note,ctl,transpo,amp)
         #self.octave = Sine([0.15,0.13]).range(0.1, 0.9)
         #self.duty = Sine([0.07, .1]).range(0.1, 0.5)
         #self.osc = FatBass(self.freq, self.octave, self.duty, 2500, 0, mul=self.amp)
         self.osc = FatBass(self.freq,mul=self.amp, add=0)
         self.output=self.osc
         self.sig=self.osc

