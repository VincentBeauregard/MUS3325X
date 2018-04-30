from pyo import *
import pyo
from random import uniform
###Changer les lignes suivante en fonction de la position dans votre machine
sys.path.insert(0, '/home/vincent/Documents/univ/hiver2018/mus3325/git/MUS3325X/app/Synth')
####


sys.path.insert(0, sys.path[0]+'/Effect')
sys.path.insert(0, sys.path[1]+'/Instrument')

import effect
from instrument import *


s = Server()



###Le champ controle indique les controleur midi accessible
### Le clavier Midi oxygen 8 d'Olivier Belanger correspond au suivant:
ctl = [74,71,81,91,16,80,19,2]

###un clavier plus standard aura cest parametre.
ctl=[2,3,4,5,6,7,8]
###
ctl=[]






### enregistre les controleur utiliser, on garde le 1 pour le modulo par defaut
usedCtl=[1]

### si les controles ne sont pas connu, il y a moyen de recuperer les controleur en les activant
def ctl_scan(ctlnum,v1):
    if(ctlnum not in ctl and ctlnum not in usedCtl ):
        ctl.append(ctlnum)
    print(ctl)
outt=0

###Synth est la classe de gestion principale pour tout les objet disponnible
class Synth:
    def __init__(self,input):
        #initialisation des paramettres globaux
        global usedCtl, ctl
        s.setMidiInputDevice(999)#possibilite d'ajuster selon votre device
        s.boot()
        self.note = Notein(poly=10, scale=1, first=0, last=127)
        self.ctl = Midictl(1, minscale=0, maxscale=2)
        self.bend = Bendin(brange=2, scale=1)
        self.lf = Sine(freq=5, mul=self.ctl, add=1)
        self.instrument = Defaut(self.note , transpo = self.lf * self.bend, amp=1)
        self.a = pyo.CtlScan2(self.ctl_scan,False)
        self.a.setFunction(ctl_scan)
        self.effects = {}
        self.effectOrder = []
        self.midiCtls = {}
        self.ports = {}
        self.out = self.instrument
        self.amp=1
        #controle des sortie par filtre passe haut passe bas et passe bande
        self.masterCtl=[ButLP(self.out.sig, freq=1000, mul=1, add=0.0001)]
        self.masterCtl.append(ButHP(self.masterCtl[0], freq=1000, mul=1, add=0))
        self.masterCtl.append(ButBP(self.masterCtl[1], freq=1000, mul=1, add=0))
        #sortie stereo
        self.masterCtl.append(Pan(self.masterCtl[2], outs=2, pan=0.50, spread=0.50, mul=1, add=0))
    def ctl_scan(ctlnum):
        print("test")
        #demarre le synth
    def start(self,instrument):
        s.start()
        self.resume()
        #reinitialise le synth
    def stop(self):
        self.effects = {}
        self.effectOrder = []
        self.out=self.instrument
        self.out.stop()
        
    def exit(self):
        s.stop()
    def pause(self):
        self.masterCtl[3].stop()
    def resume(self):
        self.masterCtl[0].setInput(self.out.sig)
        self.masterCtl[3].out()
        
    #ajoute un effet a la postion voulu
    def addEffect(self,eff,name,pos):
        print(name)
        self.pause()
        if(len(self.effectOrder)==0):#empty
            self.effects[name]=self.setEffect(eff,self.out.sig)                
            self.effectOrder.append(name)
            self.out = self.effects[name]
        elif(len(self.effectOrder)==pos):#add last
            self.effects[name]=self.setEffect(eff,self.effects[self.effectOrder[len(self.effectOrder)-1]].sig)                
            self.effectOrder.append(name)
            self.out = self.effects[name]
        elif(pos==0):#add first
            self.effects[name]=self.setEffect(eff,self.instrument.sig)         
            self.effectOrder.insert(pos,name)
            self.effects[self.effectOrder[pos+1]].sig.setInput(self.effects[name].sig)   
            self.out = self.effects[self.effectOrder[len(self.effectOrder)-1]]
        elif(pos > 0 and pos < len(self.effectOrder)):
            self.effects[name]=self.setEffect(eff,self.effects[self.effectOrder[pos-1]].sig)          
            self.effectOrder.insert(pos,name)
            self.effects[self.effectOrder[pos+1]].effect.setInput(self.effects[name].sig)  
            self.out = self.effects[self.effectOrder[len(self.effectOrder)-1]]
        self.resume()

    #creation de l'effet demander
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
        
    #retrait de l'effet selon sa position
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
            self.effects[self.effectOrder[index+1]].effect.setInput(self.effects[self.effectOrder[index-1]].sig)  
            self.effects.pop(name)                
            self.effectOrder.remove(name)
        self.resume()
        
    #change l'instrument utiliser
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
        
    ####les fonction suivante s'occupe de la gestion des controleur MIDI
    def getCtl(self):
        return ctl
    #celle-ci en bloque un et rassemble les parametre en question
    def useCtl(self,index,min,max,fn):
        self.midiCtls[index]=Midictl(ctlnumber=index, minscale=min, maxscale=max)
        self.ports[index]=Port(self.midiCtls[index], .02)
        fn(self.ports[index])
        ctl.remove(index)
        usedCtl.append(index)
    #celle-ci libere un controleur utiliser
    def freeCtl(self,index):
        self.ports.pop(index)
        self.midiCtls.pop(index)
        ctl.append(index)
        usedCtl.remove(index)
            
####