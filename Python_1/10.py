plik_we = str(raw_input("Podaj sciezke pliku wej:"))
plik_wy = str(raw_input("Podaj sciezke do pliku wyj:"))

slowa = {"i":"oraz", "oraz":"i", "nigdy":"prawie nigdy", "dlaczego":"czemu"}

file_open = open(plik_we).readlines()
file_save = open(plik_wy, "w")

for word in file_open:
    for key in slowa.keys():
	if word == key:
	file_save.write(line.replace(key,slowa.get(key)))
	
file_open.close()
file_save.close()
	