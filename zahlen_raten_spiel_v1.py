# V1
# Made by Arturschick
# 

import random
spielen = True

def spiel_Start():
    global spielen
    zahl = random.randint(1,100)
    while spielen is True:
        print("Eine Zahl wurde bereits für dich festgelegt")
        print("Randomzahl:",zahl)
        eingabe = int(input("Welche Zahl wählst du?\nZahl: "))
        try:
            if eingabe in range(0, 100):
                if eingabe == zahl:
                    print("Du hast richtig geraten! Woho!!!\nMöchtest du weiterspielen?\n\nWeiterspielen = y/Y")
                    weiterspielen = input("\n Eingabe: ")
                    if weiterspielen == "y":
                        spiel_Start()
                    else:
                        spielen = False
                        print("Bis Bald!\nDas Spiel wird Beendet...")
                        break
        except:
            print("Ungültige Eingabe, Nutze nur Zahlen zwischen 1 und 100.")

print("Willkommen bei 'Errate die Zahl'\nLass uns gleich anfangen!")
print("\n\n######### Spielregeln #########\n")
print("Errate die Zahl zwischen 1 und 100\nDu hast genau 10 versuche um erfolgreich zu sein =)\n")
input("Bestätige mit Enter um zu beginnen...")
spiel_Start()