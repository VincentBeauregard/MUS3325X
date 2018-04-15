from pyo import *
s = Server()
s.boot()
s.start()
sin = Sine(freq=1000, phase=0, mul=1, add=0).out()