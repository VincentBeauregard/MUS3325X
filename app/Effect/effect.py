from pyo import *
class Effect():
    def __init__(self, sigFreq,ctl):
        self.sigFreq=sigFreq
        self.ctl = ctl
        self.output = PyoObject()
        self.effect = PyoObject()
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

class Disto_(Effect):
    def __init__(self, sigFreq,ctl):
        Effect.__init__(self, sigFreq,ctl)
        self.effect = Disto(self.sigFreq, drive=ctl[0], slope=ctl[1], mul=ctl[2])
        self.output = Mix(self.effect, voices=2)
        
class Delay_(Effect):
    def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class SDelay_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class Delay1_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class Waveguide_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class AllpassWG(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class Freeverb_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class Convolve_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class WGVerb_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class Chorus_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class Harmonizer_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class FreqShift_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class STRev_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)
class SmoothDelay_(Effect):
	def __init__(self, sigFreq, sigAmp,ctl=0):
		Effect.__init__(self, sigFreq, sigAmp,ctl)

























