import numpy as np
from math import log
from matplotlib import pyplot
import math
def f1(x):
  return np.log(x/1)
x=range(-10,10)
pyplot.plot(x, [f1(i) for i in x])
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
pyplot.show()