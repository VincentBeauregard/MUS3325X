from pyo import *
class Effect():
    def __init__(self, sigFreq):
        self.sigFreq=sigFreq        
        self.output = PyoObject()
        self.effect = PyoObject()
        self.parametre = {}
    def out(self):
        print("start")
        self.output.out()
        return self
    def stop(self):
        print("stop")
        self.output.stop()
        return self
    def sig(self):
        return self.effect
    def setinput(self,input):
        self.effect.setInput(input)

class Disto_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = Disto(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["drive"] = [self.effect.setDrive,self.effect.drive,0,1,-1]
        self.parametre["slope"] = [self.effect.setSlope,self.effect.slope,0,1,-1]
        self.keys = ["mul","drive","slope"]
        
class Delay_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
                self.effect = Delay(self.sigFreq, delay=self.port[0], feedback=self.port[1], maxdelay=self.port[2], mul=self.port[3])
                self.output = Mix(self.effect, voices=2)

class SDelay_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = SDelay(self.sigFreq, delay=self.port[0], maxdelay=self.port[1], mul=self.port[2])
        self.output = Mix(self.effect, voices=2)

        
class Delay1_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Delay1(self.sigFreq, mul=self.port[0])
        self.output = Mix(self.effect, voices=2)

class Waveguide_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Waveguide(self.sigFreq, freq=self.port[0], dur=self.port[1], minfreq=self.port[2], mul=self.port[3])
        self.output = Mix(self.effect, voices=2)
class AllpassWG(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = AllpassWG(self.sigFreq, freq=self.port[0], feed=self.port[1], detune=self.port[2], minfreq=self.port[3], mul=self.port[4])
        self.output = Mix(self.effect, voices=2)
class Freeverb_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Freeverb(self.sigFreq, size=self.port[0], damp=self.port[1], bal=self.port[2], mul=self.port[3])
        self.output = Mix(self.effect, voices=2)
class Convolve_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Waveguide(self.sigFreq, freq=ctl[0], dur=ctl[1], minfreq=ctl[2], mul=ctl[3])
        self.output = Mix(self.effect, voices=2)
class WGVerb_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Waveguide(self.sigFreq, freq=ctl[0], dur=ctl[1], minfreq=ctl[2], mul=ctl[3])
        self.output = Mix(self.effect, voices=2)
class Chorus_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Waveguide(self.sigFreq, freq=ctl[0], dur=ctl[1], minfreq=ctl[2], mul=ctl[3])
        self.output = Mix(self.effect, voices=2)
class Harmonizer_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Waveguide(self.sigFreq, freq=ctl[0], dur=ctl[1], minfreq=ctl[2], mul=ctl[3])
        self.output = Mix(self.effect, voices=2)
class FreqShift_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Waveguide(self.sigFreq, freq=ctl[0], dur=ctl[1], minfreq=ctl[2], mul=ctl[3])
        self.output = Mix(self.effect, voices=2)
class STRev_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Waveguide(self.sigFreq, freq=ctl[0], dur=ctl[1], minfreq=ctl[2], mul=ctl[3])
        self.output = Mix(self.effect, voices=2)
class SmoothDelay_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
        Effect.__init__(self, sigFreq, sigAmp,ctl)
        self.effect = Waveguide(self.sigFreq, freq=self.port[0], dur=self.port[1], minfreq=self.port[2], mul=self.port[3])
        self.output = Mix(self.effect, voices=2)

























