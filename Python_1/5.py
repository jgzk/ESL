# !/usr/bin/python

import os

dir = str(raw_input("Podaj katalog:"))
for root, dirs, files in os.walk(dir, topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))