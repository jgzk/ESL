import numpy
from random import randint

a = numpy.random.randint(10,size=(8, 8))
b = numpy.random.randint(10,size=(8, 8))
c = numpy.zeros((8,8), dtype=numpy.int))

for i in range(8):
    for j in range(8):
        for k in range(8):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]