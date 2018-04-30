from pyo import *

        ### La classe parente Effect reuni une majorite des parametre et fonction disponible pour les effet disponible
        ### on y retrouve la liste dispnnible a la page http://ajaxsoundstudio.com/pyodoc/api/classes/effects.html

class Effect():
    def __init__(self, sigFreq):
        self.sigFreq=sigFreq        
        self.output = PyoObject()
        self.sig = PyoObject()
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
        return self.sig
    def setinput(self,input):
        self.sig.setInput(input)

class Disto_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = Disto(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["drive"] = [self.sig.setDrive,self.sig.drive,0,1,-1]
        self.parametre["slope"] = [self.sig.setSlope,self.sig.slope,0,1,-1]
        self.keys = ["mul","drive","slope"]
        
class Delay_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = Delay(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["delay"] = [self.sig.setDelay,self.sig.delay,0,1,-1]
        self.parametre["feedback"] = [self.sig.setFeedback,self.sig.feedback,0,1,-1]
        self.keys = ["mul","delay","feedback"]

class SDelay_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = SDelay(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["delay"] = [self.sig.setDelay,self.sig.delay,0,1,-1]
        self.keys = ["mul","delay"]

        
class Delay1_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = Delay1(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.keys = ["mul"]

class Waveguide_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = Waveguide(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["freq"] = [self.sig.setFreq,self.sig.freq,100,2000,-1]
        self.parametre["dur"] = [self.sig.setDur,self.sig.dur,0,100,-1]
        self.keys = ["mul","freq","dur"]
class AllpassWG_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = AllpassWG(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["freq"] = [self.sig.setFreq,self.sig.freq,100,2000,-1]
        self.parametre["feed"] = [self.sig.setFeed,self.sig.feed,0,1,-1]
        self.parametre["detune"] = [self.sig.setDetune,self.sig.detune,0,1,-1]
        self.keys = ["mul","freq","feed","detune"]
class Freeverb_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = Freeverb(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["size"] = [self.sig.setSize,self.sig.size,0,1,-1]
        self.parametre["damp"] = [self.sig.setDamp,self.sig.damp,0,1,-1]
        self.parametre["bal"] = [self.sig.setBal,self.sig.bal,0,1,-1]
        self.keys = ["mul","size","damp","bal"]
#class Convolve_(Effect):
#    def __init__(self, sigFreq):
class WGVerb_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = WGVerb(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["feedback"] = [self.sig.setFeedback,self.sig.feedback,0,1,-1]
        self.parametre["cutoff"] = [self.sig.setCutoff,self.sig.cutoff,100,8000,-1]
        self.parametre["bal"] = [self.sig.setBal,self.sig.bal,0,1,-1]
        self.keys = ["mul","feedback","cutoff","bal"]
class Chorus_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = Chorus(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["feedback"] = [self.sig.setFeedback,self.sig.feedback,0,1,-1]
        self.parametre["depth"] = [self.sig.setDepth,self.sig.depth,0,5,-1]
        self.parametre["bal"] = [self.sig.setBal,self.sig.bal,0,1,-1]
        self.keys = ["mul","feedback","depth","bal"]
class Harmonizer_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = Harmonizer(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["feedback"] = [self.sig.setFeedback,self.sig.feedback,0,1,-1]
        self.parametre["transpo"] = [self.sig.setTranspo,self.sig.transpo,-27,100,-1]
        self.parametre["winsize"] = [self.sig.setWinsize,self.sig.winsize,0,1,-1]
        self.keys = ["mul","feedback","transpo","winsize"]
class FreqShift_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = FreqShift(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["shift"] = [self.sig.setShift,self.sig.shift,-1000,1000,-1]
        self.keys = ["mul","shift"]
class STRev_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = STRev(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["inpos"] = [self.sig.setInpos,self.sig.inpos,0,1,-1]
        self.parametre["revtime"] = [self.sig.setRevtime,self.sig.revtime,0,5,-1]
        self.parametre["cutoff"] = [self.sig.setCutoff,self.sig.cutoff,100,8000,-1]
        self.parametre["bal"] = [self.sig.setBal,self.sig.bal,0.25,4,-1]
        self.parametre["roomSize"] = [self.sig.setRoomSize,self.sig.roomSize,0,1,-1]
        self.parametre["firstRefGain"] = [self.sig.setFirstRefGain,self.sig.firstRefGain,-10,10,-1]
        self.keys = ["mul","inpos","revtime","cutoff","bal","roomSize","firstRefGain"]
class SmoothDelay_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.sig = SmoothDelay(self.sigFreq)
        self.output = Mix(self.sig, voices=2)
        self.parametre["mul"] = [self.sig.setMul,self.sig.mul,0,1,-1]
        self.parametre["delay"] = [self.sig.setDelay,self.sig.delay,0,1,-1]
        self.parametre["feedback"] = [self.sig.setFeedback,self.sig.feedback,0,1,-1]
        self.parametre["crossfade"] = [self.sig.setCrossfade,self.sig.crossfade,0,1,-1]
        self.keys = ["mul","delay","feedback","crossfade"]
























