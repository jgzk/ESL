#!/usr/bin/python

import random
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Lock, Array
import matplotlib.pyplot as plt

def Lista():
    list = []
    for i in range(0,100):
        list.append(random.randint(0, 39))
    return list

def Histogram(size):
    hist = [0]*40
    return hist

def hist(hist, histogram, lk):
    for l in list:
        histogram[l] = histogram[l] + 1
    return histogram
    
l = Lock()
pool = Pool(processes=2)

list = Lista(100)
histogram = Histogram(40)
hist(list,histogram,l)
arr = Array('i', range(40))

for k in range(0,40):
    arr[k] = 0

p1 = Process(target=hist, args=(list[0:50], arr, l))
p2 = Process(target=hist, args=(list[50:100], arr, l))


p1.start()
p2.start()


p1.join()
p2.join()


plt.hist(list, bins = 40)
plt.show();