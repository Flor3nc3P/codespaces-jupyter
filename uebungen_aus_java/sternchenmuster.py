#Ausgabe soll eine Seite eines auf und absteigenden * Musters sein.
#In der FOR-Schleife (Initialisierung; Bedingung; Modifikation)
#Die FOR-Schleife ist eine Kopfgesteuerte Schleife oder auch eine abweisende Schleife.
#Die Schleife kann durch die Bedingung gleich am Anfang abgebrochen werden, wenn die Bedingung erfüllt ist.
#Bedeutet Sie durchläuft nicht zwingend den Rumpf bzw. die Befehle die im Schleifenkörper stehen. Hier die Print Befehle.
#Ich kann mit "" und '' printen. Vorteil von '' ist, das ich in meinem String "" verweden kann ohne das Python verwirrt ist.
#Mit ''' kann ich Mehrzeilige Strings in der print Funktion schreiben.
#Die input() Funktion in verbindung mit der print(f'') Funktion erlaubt es mir, meinen Überschrift variabel zu gestalten.
#Mit der Type Casting Funktion kann ich meinen Datentyp in der Input Funktion festlegen.

titel_für_muster = (input("Gib einen passenden Titel ein: \n"))
print(f'''Mein 
      "{titel_für_muster}" :) ''')


zeile=0
spalte=0

for  zeile in zeile<10, zeile+1:
    for spalte in spalte<zeile+1, spalte+1:
        print("*\n")

zeile=9
spalte=9

for zeile in zeile>0, zeile-1:
     for spalte in spalte>zeile, spalte-1:
        print("*\n")


