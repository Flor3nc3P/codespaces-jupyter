
# --Preisberechnung-- 
# Kommentar mit #
# Kommazahlen mit . trennen
# : nach if oder else
# print für die Konsolenausgabe
# input für die Konsoleneingabe
# () Runde Klammern für die Konsole
# Kein trennen der Anweisungsschritte durch ;

start_preis = 5

km = int (input("Kilometer eintippen: "))


if km > 5:
    kosten = 2

else:
    kosten = 1

Endpreis = start_preis * kosten * km
print("Ergebnissrechnung Preis für Kilometer: ", Endpreis)