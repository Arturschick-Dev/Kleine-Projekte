# V1
# Made by Arturschick
# 

import time
import random
import os


spielen = True

def spiel_Start():                  #Spielstart
    global spielen
    
    zahl = random.randint(1,100)
    versuche = 0
    
    while spielen is True:
        print("Eine Zahl wurde bereits für dich festgelegt")
        print("Randomzahl:",zahl)           # Debug, später Löschen.
        
        try:
            eingabe = int(input("Welche Zahl wählst du?\nZahl: "))
        except:
            clear()
            print("Ungültige Eingabe, Nutze nur Zahlen zwischen 1 und 100.\n")
            continue
        if eingabe >0 and eingabe <100:
            versuche+=1
            clear()
            print(f"\nVersuche {versuche}/10\n")
        
        if versuche >10:
            clear()
            print("\n###### GAME OVER ######\n")
            print("Leider alle Versuche aufgebraucht, versuch es gleich nochmal!\n")
            time.sleep(5)
            break
        
        if eingabe in range(0, 100):
            if eingabe == zahl:
                clear()
                print("Du hast richtig geraten!\nWoho!!!\n\nMöchtest du weiterspielen?\n\nWeiterspielen = y\nBeenden = Sonstige Eingabe")
                time.sleep(3)
                weiterspielen = input("\nEingabe: ")
                if weiterspielen == "y":
                    spiel_Start()
                else:
                    clear()
                    spielen = False
                    print("Bis Bald!\nDas Spiel wird Beendet...")
                    break
                

def clear():                        # Reine Clearfunktion
    os.system('cls' if os.name == 'nt' else 'clear')

print("Willkommen bei 'Errate die Zahl'\nLass uns gleich anfangen!")
print("\n\n######### Spielregeln #########\n")
print("Errate die Zahl zwischen 1 und 100\nDu hast genau 10 versuche um erfolgreich zu sein =)\n")
input("Bestätige mit Enter um zu beginnen...")
clear()
spiel_Start()