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
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = Delay(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["delay"] = [self.effect.setDelay,self.effect.delay,0,1,-1]
        self.parametre["feedback"] = [self.effect.setFeedback,self.effect.feedback,0,1,-1]
        self.keys = ["mul","delay","feedback"]

class SDelay_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = SDelay(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["delay"] = [self.effect.setDelay,self.effect.delay,0,1,-1]
        self.keys = ["mul","delay"]

        
class Delay1_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = Delay1(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.keys = ["mul"]

class Waveguide_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = Waveguide(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["freq"] = [self.effect.setFreq,self.effect.freq,100,2000,-1]
        self.parametre["dur"] = [self.effect.setDur,self.effect.dur,0,100,-1]
        self.keys = ["mul","freq","dur"]
class AllpassWG_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = AllpassWG(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["freq"] = [self.effect.setFreq,self.effect.freq,100,2000,-1]
        self.parametre["feed"] = [self.effect.setFeed,self.effect.feed,0,1,-1]
        self.parametre["detune"] = [self.effect.setDetune,self.effect.detune,0,1,-1]
        self.keys = ["mul","freq","feed","detune"]
class Freeverb_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = Freeverb(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["size"] = [self.effect.setSize,self.effect.size,0,1,-1]
        self.parametre["damp"] = [self.effect.setDamp,self.effect.damp,0,1,-1]
        self.parametre["bal"] = [self.effect.setBal,self.effect.bal,0,1,-1]
        self.keys = ["mul","size","damp","bal"]
#class Convolve_(Effect):
#    def __init__(self, sigFreq):
class WGVerb_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = WGVerb(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["feedback"] = [self.effect.setFeedback,self.effect.feedback,0,1,-1]
        self.parametre["cutoff"] = [self.effect.setCutoff,self.effect.cutoff,100,8000,-1]
        self.parametre["bal"] = [self.effect.setBal,self.effect.bal,0,1,-1]
        self.keys = ["mul","feedback","cutoff","bal"]
class Chorus_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = Chorus(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["feedback"] = [self.effect.setFeedback,self.effect.feedback,0,1,-1]
        self.parametre["depth"] = [self.effect.setDepth,self.effect.depth,0,5,-1]
        self.parametre["bal"] = [self.effect.setBal,self.effect.bal,0,1,-1]
        self.keys = ["mul","feedback","depth","bal"]
class Harmonizer_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = Harmonizer(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["feedback"] = [self.effect.setFeedback,self.effect.feedback,0,1,-1]
        self.parametre["transpo"] = [self.effect.setTranspo,self.effect.transpo,-27,100,-1]
        self.parametre["winsize"] = [self.effect.setWinsize,self.effect.winsize,0,1,-1]
        self.keys = ["mul","feedback","transpo","winsize"]
class FreqShift_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = FreqShift(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["shift"] = [self.effect.setShift,self.effect.shift,-1000,1000,-1]
        self.keys = ["mul","shift"]
class STRev_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = STRev(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["inpos"] = [self.effect.setInpos,self.effect.inpos,0,1,-1]
        self.parametre["revtime"] = [self.effect.setRevtime,self.effect.revtime,0,5,-1]
        self.parametre["cutoff"] = [self.effect.setCutoff,self.effect.cutoff,100,8000,-1]
        self.parametre["bal"] = [self.effect.setBal,self.effect.bal,0.25,4,-1]
        self.parametre["roomSize"] = [self.effect.setRoomSize,self.effect.roomSize,0,1,-1]
        self.parametre["firstRefGain"] = [self.effect.setFirstRefGain,self.effect.firstRefGain,-10,10,-1]
        self.keys = ["mul","inpos","revtime","cutoff","bal","roomSize","firstRefGain"]
class SmoothDelay_(Effect):
    def __init__(self, sigFreq):
        Effect.__init__(self, sigFreq)
        self.effect = SmoothDelay(self.sigFreq)
        self.output = Mix(self.effect, voices=2)
        self.parametre["mul"] = [self.effect.setMul,self.effect.mul,0,1,-1]
        self.parametre["delay"] = [self.effect.setDelay,self.effect.delay,0,1,-1]
        self.parametre["feedback"] = [self.effect.setFeedback,self.effect.feedback,0,1,-1]
        self.parametre["crossfade"] = [self.effect.setCrossfade,self.effect.crossfade,0,1,-1]
        self.keys = ["mul","delay","feedback","crossfade"]
























