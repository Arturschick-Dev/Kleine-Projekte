# Zeiterfassungsprogramm by Artur
# v3.0

import time
from datetime import datetime, timedelta
import os

# Speichert die Datei im gleichen Ordner wie das Skript
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) #
DATEIPFAD = os.path.join(SCRIPT_DIR, "timeDoku.txt")    #
# Speichert die Datei im gleichen Ordner wie das Skript


zeiten = []

DT_FMT_STORAGE = "%Y-%m-%d %H:%M:%S"  # so speicherst du aktuell
DATE_FMT_INPUT = "%d.%m.%Y"           # Eingabeformat für den Nutzer (DE)


def lade_zeiten():
    global zeiten
    try:
        with open(DATEIPFAD,"r") as datei:
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
        
### GPT ###
def parse_start_dt(entry: str) -> datetime:
    """Zieht die Start-Datetime aus einem gespeicherten Eintrag."""
    # Beispiel-Eintrag: "2025-09-02 14:23:05 - 14:55:19 | Dauer: 00:32:14"
    start_str = entry.split(" - ")[0].strip()
    return datetime.strptime(start_str, DT_FMT_STORAGE)

def show_entries(entries):
    """Einträge hübsch ausgeben + Pause."""
    if not entries:
        print("\nKeine passenden Einträge gefunden.\n")
    else:
        for i, e in enumerate(entries, 1):
            print(f"{i}. {e}")
        print(f"\n{len(entries)} Einträge.\n")
    input("Weiter mit Enter...")

def filter_by_day_loop():
    while True:
        tag = input("Datum (dd.mm.yyyy): ").strip()
        try:
            ziel = datetime.strptime(tag, DATE_FMT_INPUT).date()
            ergebnis = [e for e in zeiten if parse_start_dt(e).date() == ziel]
            show_entries(ergebnis)
            break
        except ValueError:
            print("Ungültiges Format! Bitte dd.mm.yyyy verwenden.")

def filter_by_month_loop():
    while True:
        monat = input("Monat.Jahr (mm.yyyy): ").strip()
        try:
            first = datetime.strptime("01." + monat, DATE_FMT_INPUT)
            ergebnis = [e for e in zeiten
                        if (dt := parse_start_dt(e)).year == first.year and dt.month == first.month]
            show_entries(ergebnis)
            break
        except ValueError:
            print("Ungültiges Format! Bitte mm.yyyy verwenden.")

def filter_by_year_loop():
    while True:
        jahr = input("Jahr (yyyy): ").strip()
        if jahr.isdigit() and len(jahr) == 4:
            y = int(jahr)
            ergebnis = [e for e in zeiten if parse_start_dt(e).year == y]
            show_entries(ergebnis)
            break
        else:
            print("Ungültiges Format! Bitte yyyy verwenden (z. B. 2025).")

def filter_between_loop():
    while True:
        von = input("Von (dd.mm.yyyy): ").strip()
        bis = input("Bis (dd.mm.yyyy): ").strip()
        try:
            start = datetime.strptime(von, DATE_FMT_INPUT)
            ende  = datetime.strptime(bis, DATE_FMT_INPUT) + timedelta(days=1) - timedelta(seconds=1)
            if ende < start:  # falls vertauscht, tauschen
                start, ende = ende, start
            ergebnis = [e for e in zeiten if start <= parse_start_dt(e) <= ende]
            show_entries(ergebnis)
            break
        except ValueError:
            print("Ungültiges Format! Bitte dd.mm.yyyy verwenden.")

### GPT ###

def zeitenAnzeige():
    while True:
        try:
            auswahl = int(input(
                "Was benötigst du?\n\n"
                "1 - Bestimmten Tag (dd.mm.yyyy)\n"
                "2 - Bestimmten Monat (mm.yyyy)\n"
                "3 - Bestimmtes Jahr (yyyy)\n"
                "4 - Zwischenräume (von dd.mm.yyyy bis dd.mm.yyyy)\n"
                "5 - Alle Einträge\n\n"
                "Bitte deine Auswahl: "
            ))
            if auswahl in (1,2,3,4,5):
                break
            print("Ungültige Eingabe! Bitte 1,2,3,4 oder 5 eingeben.")
        except ValueError:
            print("Ungültige Eingabe! Bitte nur Zahlen eingeben.")

    if auswahl == 5:
        show_entries(zeiten)
    elif auswahl == 1:
        filter_by_day_loop()
    elif auswahl == 2:
        filter_by_month_loop()
    elif auswahl == 3:
        filter_by_year_loop()
    elif auswahl == 4:
        filter_between_loop()
        return
#def zeitenAnzeige():
#    
#    while True:
#        try:
#            anzeigeauswahl = int(input("Was benötigst du?\n\n"
#                                       "1 - Bestimmten Tag\n"
#                                       "2 - Bestimmten Monat\n"
#                                       "3 - Bestimmtes Jahr\n"
#                                       "4 - Zwischenräume 'von xx.xx.xxxx bis xx.xx.xxxx'\n"
#                                       "5 - Alle Eintraege\n\n"
#                                       "Bitte deine Auswahl: "))
#            if anzeigeauswahl in (1,2,3,4,5):
#                break
#            else:
#                print("Ungültige Eingabe! Bitte 1,2,3,4 oder 5 eingeben.\n")
#        except ValueError:
#            print("Ungültige Eingabe! Bitte nur Zahlen eingeben.\n")
#            
#    if anzeigeauswahl == 5:
#        clear()
#        for index, eintrag in enumerate(zeiten):
#            print(f"[{index}] - {eintrag}")
#        print(f"\nDeine Liste hat {len(zeiten)} Einträge.\n")
#        print("\033[31mMit \033[1mEnter verlassen\033[22m Sie die Ansicht.\033[0m")
#        input()

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