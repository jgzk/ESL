import numpy
from random import randint

a = numpy.random.randint(10,size=(128, 128))
b = numpy.random.randint(10,size=(128, 128))
c = numpy.zeros((128,128), dtype=numpy.int))
for i in range(128):
    for j in range(128):
        c[i][j] = a[i][j] + b[i][j]