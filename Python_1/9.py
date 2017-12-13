plik_we = str(raw_input("Podaj sciezke pliku wej:"))
plik_wy = str(raw_input("Podaj sciezke do pliku wyj:"))

slowa = ["się", "i", "oraz", "nigdy", "dlaczego"]

file_open = open(plik_we)
file_save = open(plik_wy, "w")
for line in file_open:
    for word in slowa:
        line = line.replace(word, "")
    file_save.write(line)
file_open.close()
file_save.close()
