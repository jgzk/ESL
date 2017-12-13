from PIL import Image

plik=input("Podaj plik do konwersji:")
jpg = plik + '.jpg'
png = plik+ '.png'

im = Image.open(jpg)
im.save(png)