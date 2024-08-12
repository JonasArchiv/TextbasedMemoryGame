import random

def erstelle_spielbrett():
    symbole = ["🍎", "🍌", "🍒", "🍇", "🍓", "🍉", "🍍", "🥥"]
    symbole = symbole * 2
    random.shuffle(symbole)

    brett = []
    for i in range(4):
        brett.append(symbole[i*4:(i+1)*4])
    return brett

def zeige_brett(brett, aufgedeckt):
    print("\nAktuelles Spielfeld:")
    print("  0 1 2 3")
    for i in range(4):
        reihe = str(i) + " "
        for j in range(4):
            if aufgedeckt[i][j]:
                reihe += brett[i][j] + " "
            else:
                reihe += "❓ "
        print(reihe)
    print()

def abfrage_eingabe():
    while True:
        eingabe = input("Gib die Zeile und Spalte ein (z.B. 0 1): ").split()
        if len(eingabe) != 2:
            print("Ungültige Eingabe. Bitte gib zwei Zahlen ein.")
            continue
        try:
            zeile, spalte = int(eingabe[0]), int(eingabe[1])
            if 0 <= zeile < 4 and 0 <= spalte < 4:
                return zeile, spalte
            else:
                print("Ungültige Koordinaten. Die Werte müssen zwischen 0 und 3 liegen.")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein.")

def spiel():
    brett = erstelle_spielbrett()
    aufgedeckt = [[False] * 4 for _ in range(4)]
    gefundene_paare = 0

    while gefundene_paare < 8:
        zeige_brett(brett, aufgedeckt)

        print("Erste Karte aufdecken:")
        zeile1, spalte1 = abfrage_eingabe()
        if aufgedeckt[zeile1][spalte1]:
            print("Diese Karte ist bereits aufgedeckt. Wähle eine andere.")
            continue
        aufgedeckt[zeile1][spalte1] = True
        zeige_brett(brett, aufgedeckt)

        print("Zweite Karte aufdecken:")
        zeile2, spalte2 = abfrage_eingabe()
        if aufgedeckt[zeile2][spalte2]:
            print("Diese Karte ist bereits aufgedeckt. Wähle eine andere.")
            aufgedeckt[zeile1][spalte1] = False  # Erste Karte wieder verdecken
            continue
        aufgedeckt[zeile2][spalte2] = True
        zeige_brett(brett, aufgedeckt)

        if brett[zeile1][spalte1] == brett[zeile2][spalte2]:
            print("Paar gefunden!")
            gefundene_paare += 1
        else:
            print("Kein Paar! Die Karten werden wieder verdeckt.")
            aufgedeckt[zeile1][spalte1] = False
            aufgedeckt[zeile2][spalte2] = False

    print("Herzlichen Glückwunsch! Du hast alle Paare gefunden!")

spiel()
