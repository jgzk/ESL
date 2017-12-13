import random

seed()
liczby = []

for i in range(50):
     liczby.append(random.randint(0,1000))


factor = False
while not factor:
  factor = True
  for i in range(len(liczby)-1):
    if liczby[i] < l[i+1]:
      s = False
      liczby[i], liczby[i+1] = liczby[i+1], liczby[i]
  
print(liczby)