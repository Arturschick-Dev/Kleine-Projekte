# Zeiterfassungsprogramm by Artur
# v1.0

import time
from datetime import datetime
import os


jetzt = datetime.now()

zeiten = []

def lade_zeiten():
    global zeiten
    try:
        with open("timeDoku.txt","r") as datei:
            zeiten = [zeile.strip() for zeile in datei]
    except FileNotFoundError:
        zeiten = []
        
        
def speicher_zeiten():
    
    with open("timeDoku.txt","w") as datei:
        for eintrag in zeiten:
            datei.write(eintrag + "\n")

        

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def zeitenAnzeige():
    print("Test1")

def zeitenKorrektur():
    print("Test2")

def zeitenErfassung():
    start_zeit = datetime.now()
    print(f"Zeiterfassung wurde um {start_zeit.strftime('%H:%M:%S')} gestartet. Zum Stoppen, bitte Enter drücken.")
    input() # warte auf Eingabe für Beendigung der Zeit.
    end_zeit = datetime.now()
    print(f"Zeiterfassung wurde um {end_zeit.strftime('%H:%M:%S')} Gestoppt.")
    dauer = end_zeit - start_zeit
    gesamte_zeit = str(dauer).split(".")[0]
    print(f"Erfasste Zeit: {gesamte_zeit}")
    try:
        speichern = input("Möchtest du diese Zeit Speichern?\ny = Ja\nn = Nein\n\nEingabe: ")
        if speichern == "y":
            zeiten.append(gesamte_zeit)
            speicher_zeiten()
        else:
            print("Okay, deine Zeit wurde nicht abgespeichert.")
    except ValueError:
        print("Falsche eingabe, bitte 'Y' für Speichern oder 'N' für nicht Speichern, tippen.")
            
            
    
    
    
def zeitenFurz():
    print("Furz")
    


lade_zeiten()
print(f"\n{jetzt.strftime('%d-%m-%Y - %H:%M:%S')}")
print("\nWillkommen bei der Zeiterfassungsmaschine\nWas moechtest du tun?\n")
print("1 - Zeiten Anzeigen lassen\n2 - Zeitenkorrektur vornehmen\n3 - Zeiterfassung beginnen\n\n9 - Programm beenden\n")

while True:
    try:
        eingabe = int(input("\nTriff deine Auswahl: "))
    except ValueError:
        print("Deine Eingabe ist Ungueltig, bitte nur Zahlen 1-3 oder 9 nutzen!")
        continue            # zurück zum Schleifenanfang
        
    if eingabe == 9:
        clear()
        time.sleep(1)
        print("3... - Daten werden gespeichert!\n")
        time.sleep(1)
        print("2... - Deine Fotos, Videos und Passwörter werden gedownloadet!\n")
        time.sleep(2)
        print("1... - Daten an die USA Verkauft!")
        time.sleep(2)
        print("NEIN SPAAAAAAAAAAAß!\n")
        time.sleep(3)
        print("Bis bald!\nProgramm wurde beendet.")
        exit()
    elif eingabe == 1:
        clear()
        zeitenAnzeige()
    elif eingabe == 2:
        clear()
        zeitenKorrektur()
    elif eingabe == 3:
        clear()
        zeitenErfassung()
    elif eingabe == 4:
        clear()
        zeitenFurz()
    else:
        print("Bitte wähle zwischen 1-3 oder 9 zum Beenden!")