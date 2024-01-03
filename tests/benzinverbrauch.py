#print("Test") um eine einfache Zeile auszugeben
#print(f"Test") um in die Ausgabe eine Varbiable einzubauen 
#\n --> Zeilenumbruch
#float = Gleitkommazahl
#{variable:.2f} beschränkt die Darstellung der Variable auf zwei Nachkommastellen



print ("Berechnung des Benzin-Verbrauchs\n")

strecke = float(input("Gefahrene Strecke in km: \n"))
liter = float(input("Benötigtes Benzin in Liter: \n"))
verbrauch = liter/strecke*100
print (f"Der Verbrauch liegt bei {verbrauch:.2f} Liter pro 100km.\n")
streckegesamt = strecke/liter
print (f"Sie können eine Strecke von {streckegesamt:.2f}km pro Liter zurücklegen")

       