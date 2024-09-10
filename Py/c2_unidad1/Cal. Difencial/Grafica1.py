import math as mt
from matplotlib import pyplot
def f1(x):
  return 3*(x) + 2
x=range(-10,10)
pyplot.plot(x, [f1(i) for i in x])
pyplot.axhline(0, color="blue")
pyplot.axvline(0, color="red")
pyplot.show()