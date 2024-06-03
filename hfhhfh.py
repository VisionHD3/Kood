from easygui import *
from urllib.request import urlopen

def loe_fail():
    failinimi = fileopenbox("Vali fail, mida soovite lugeda:")
    if failinimi:
        fail = open(failinimi, encoding="utf-8")
        sisu = fail.read()
        fail.close()
        if sisu:
            textbox(sisu)

def kirjuta_fail():
    failinimi = filesavebox("Vali fail, kuhu soovite kirjutada:")
    if failinimi:
        sisu = enterbox("Sisesta tekst, mida soovite faili kirjutada:")
        if sisu:
            fail = open(failinimi, 'w', encoding='utf-8')
            fail.write(sisu)
            fail.close()
            msgbox("Tekst salvestatud.")
            
def loe_veebileht():
    url = "https://example-files.online-convert.com/document/txt/example.txt"
    sisu = urlopen(url).read().decode('utf-8')

    textbox(sisu)

nupud = ["Loe failist", "Kirjuta faili", "Loe veebist"]
valik = buttonbox("Vali tegevus:",choices=nupud)
    
if valik == "Loe failist":
    loe_fail()
    
elif valik == "Kirjuta faili":
    kirjuta_fail()
    
elif valik == "Loe veebist":
    loe_veebileht()