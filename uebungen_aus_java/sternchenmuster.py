# Ausgabe soll eine Seite eines auf und absteigenden * Musters sein.
# In der FOR-Schleife (Initialisierung; Bedingung; Modifikation)
# Die FOR-Schleife ist eine Kopfgesteuerte Schleife oder auch eine abweisende Schleife.
# Die Schleife kann durch die Bedingung gleich am Anfang abgebrochen werden, wenn die Bedingung erfüllt ist.
# Bedeutet Sie durchläuft nicht zwingend den Rumpf bzw. die Befehle die im Schleifenkörper stehen. Hier die Print Befehle.
# Ich kann mit "" und '' printen. Vorteil von '' ist, das ich in meinem String "" verweden kann ohne das Python verwirrt ist.
# Mit ''' kann ich Mehrzeilige Strings in der print Funktion schreiben.
# Die input() Funktion in verbindung mit der print(f'') Funktion erlaubt es mir, meinen Überschrift variabel zu gestalten.
# Mit der Type Casting Funktion kann ich meinen Datentyp in der Input Funktion festlegen.


# Titel für Muster eintippen
titel_für_muster = (input("Gib einen passenden Titel ein: \n"))
print(f'''Mein 
      "{titel_für_muster}" :) ''')


# Figur 1 Orininalmuster
# Sternchen hoch
for zeile in range(10):
    for spalte in range(zeile + 1):
        print("x", end="")
    print()

# Sternchen runter
for zeile in range(9, 0, -1):
    for spalte in range(zeile):
        print("x", end="")
    print()



# Originalmuster links vertikal gespiegelt
anzahlZeilen = 21
anzahlX = 0

for zeile in range(anzahlZeilen):
    if zeile <= anzahlZeilen // 2:
        anzahlX += 2
    else:
        anzahlX -= 2
    
    anzahlLeerzeichen = ((anzahlZeilen + 1) - anzahlX) // 2
    
    for n in range(anzahlLeerzeichen):
        print(" ", end="")
    for n in range(anzahlX):
        print("x", end="")
    
    print()



# Originalmuster rechts vertikal gespiegelt 
# Originalmuster
for zeile in range(10):
    for spalte in range(zeile + 1):
        print("x", end="")
        
        # Spiegelachse
    for spalte in range(9 - zeile):
        print(" ", end="")
    print(end=" | ")
    for spalte in range(9 - zeile):
        print(" ", end="")
        # Spiegelachse ende

    for spalte in range(zeile + 1):
        print("x", end="")
    print()

# Gespiegeltes Originalmuster
for zeile in range(9, 0, -1):
    for spalte in range(zeile):
        print("x", end="")

        # Spiegelachse
    for spalte in range(10 - zeile):
        print(" ", end="")
    print(end=" | ")
    for spalte in range(10 - zeile):
        print(" ", end="")
        #Spiegelachse ende

    for spalte in range(zeile):
        print("x", end="")
    print()
