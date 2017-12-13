import math

a = int(raw_input("Podaj a:"))
b = int(raw_input("Podaj b:"))
c = int(raw_input("Podaj c:"))

delta = (b*b) - (4*a*c)
print("a=delta: {}".format(delta))

if delta < 0:
    print "Delta mniejsza od 0"
elif delta == 0:
    x = - b / 2 * a
    print("x1 i x2 równe: {}".format(x))
else:
    x1 = (- b - sqrt (delta)) / 2 * a
    x2 = (- b + sqrt (delta)) / 2 * a
    print ("x1 równe: {},x2 równe: {}".format(x1,x2))
