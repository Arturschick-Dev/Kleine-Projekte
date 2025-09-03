# Zeiterfassungsprogramm by Artur
# v2.0 - Letzter Stand -> Speicherfunktion vollständig eingetragen

import time
from datetime import datetime
import os

# Speichert die Datei im gleichen Ordner wie das Skript
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) #
DATEIPFAD = os.path.join(SCRIPT_DIR, "timeDoku.txt")    #
# Speichert die Datei im gleichen Ordner wie das Skript


zeiten = []


def lade_zeiten():
    global zeiten
    try:
        with open("timeDoku.txt","r") as datei:
            zeiten = [zeile.strip() for zeile in datei]
    except FileNotFoundError:
        zeiten = []
        
        
def speicher_zeiten():
    global zeiten
    dateipfad = os.path.abspath("timeDoku.txt")
    with open(DATEIPFAD,"w") as datei:
        for eintrag in zeiten:
            datei.write(eintrag + "\n")
    print("\n ~~~ Speichern Erfolgreich! ~~~ \n")
    print(f"Datei gespeichert unter: {DATEIPFAD}")
    print(f"Gespeicherte Einträge: {len(zeiten)}\n")

        

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def zeitenAnzeige():
    print("Test1")

def zeitenKorrektur():
    print("Test2")

def zeitenErfassung():                  # Hier beginnt die Zeitenerfassung
    start_zeit = datetime.now()
    print(f"Zeiterfassung wurde um {start_zeit.strftime('%H:%M:%S')} gestartet.\nZum Stoppen, bitte Enter drücken.\n")
    input()                 # warte auf Eingabe für Beendigung der Zeit.
    end_zeit = datetime.now()
    print(f"Zeiterfassung wurde um {end_zeit.strftime('%H:%M:%S')} Gestoppt.\n")
    dauer = end_zeit - start_zeit
    gesamte_zeit = str(dauer).split(".")[0]
    print(f"Erfasste Zeit: {gesamte_zeit}\n")
    speichern = input("Möchtest du diese Zeit speichern?\n[y] Ja\n[n] Nein\n\nEingabe: ").lower()
    while speichern not in ("y", "n"):
        speichern = input("Ungültige Eingabe! Bitte 'y' oder 'n' eingeben: ").lower()
    if speichern == "y":
        eintrag = f"{start_zeit.strftime('%Y-%m-%d %H:%M:%S')} - {end_zeit.strftime('%H:%M:%S')} | Dauer: {gesamte_zeit}"
        zeiten.append(eintrag)
        speicher_zeiten()
        print("Deine Zeit",gesamte_zeit,"wurde gespeichert!\n")
        time.sleep(3)
    elif speichern == "n":
        print("Okay, deine Zeit wurde nicht abgespeichert.")
            
            
    
    
    
def zeitenFurz():
    print("Furz")
    


lade_zeiten()         # Injeziert die bereits gespeicherten Daten

while True:             # Das ist die Hauptschleife
    try:
        print(f"\n{datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}")         # zeit Aktuelles Datum und Uhrzeit an
        print("\nWillkommen bei der Zeiterfassungsmaschine\nWas moechtest du tun?\n")
        print("1 - Zeiträume anzeigen lassen\n2 - Zeiten- Korrektur vornehmen oder Loeschen\n3 - Zeiterfassung beginnen\n\n9 - Programm beenden\n")
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
        clear()
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