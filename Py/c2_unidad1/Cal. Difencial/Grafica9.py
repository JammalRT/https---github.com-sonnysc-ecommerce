import math as mt
from matplotlib import pyplot
def f1(x):
  
  return mt.tan(3*x)
x=range(-5,10)
pyplot.plot(x, [f1(i) for i in x])
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
pyplot.show()