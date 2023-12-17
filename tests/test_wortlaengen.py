# Beispiel für eine for-Schleife.
# Eine Liste von Wörtern, deren Wortlänge ausgegeben werden soll.
# len --> gibt die Anzahl der Zeichen (also die Länge) eines Strings an.
# Das f bei (print(f"...")) erlaubt mir die Variablen direkt einzufügen, indem sie in geschweifte Klammern gesetzt werden.

wortliste = ["Apfel", "Auto", "Rathausplatz", "Dualesstudium", "Bücher"]


for wort in wortliste:
    wortlaenge = len(wort)
    print(f"{wort}: Länge {wortlaenge}")


ziel_laenge = 6
print(f"\nWörter mit Länge {ziel_laenge}:")

for wort in wortliste:
    if len(wort) == ziel_laenge:
        print(wort)