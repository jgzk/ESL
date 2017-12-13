File = open("plik.txt", "w")
Text = raw_input("Tekst: ")
File.write(Text)
File.close()

File = open("plik.txt", "r")
Read = File.readline()
print Read
File.close()
