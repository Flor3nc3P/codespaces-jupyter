## Implizite Konvertierung ##

ganzzahl = 1
# Datentyp Int
kommazahl = 2.5
# (gleitkommazahl) Datentyp Float
summe = ganzzahl + kommazahl
print(summe)
# Ausgabe: 3.5, da die Ganzzahl in den nächst höheren Datentyp umgewandelt wurde. Int wurde in Float umgewandelt.


## Explizite Konvertierung ##

ganzzahl = 1
# Datentyp Int
stringzahl = "2.5"
# Datentyp String
kommazahl = float(stringzahl)
# Inhalt aus stringzahl (den String) in Datentyp Float umgewandelt
summe = ganzzahl + kommazahl
print(summe)
# Ausgabe: 3.5, als Float.


# Achtung Datenverlust #

ganzzahl = 1 
# Datentyp Int
kommazahl = 2.5
# Datentyp Float
ganzzahl_2 = int(kommazahl)
# Inhalt aus kommazahl in Datentyp Int umgewandelt
summe = ganzzahl + ganzzahl_2
print(summe)
# Ausgabe: 3, die kommazahl wurde in einen niedrigeren Datentyp konvertiert und abgeschnitten (3.5 -->3)