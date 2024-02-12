# Listen
# Sammlung von Elementen
# Zählung beginnt immer bei 0
# Index 1 ist somit Platz 2 der Liste

## Leere Liste erstellen
listeLeer = []
print(listeLeer)
print(type(listeLeer))

## Liste von Strings, Integers, Floats, Listen ##
listeVonStrings = ["a","b","c"]     # Liste mit Buchstaben/Strings
print(listeVonStrings)
listeVonIntegers = [4,21,7,1,2,3,4,5,6,7,8] # Liste mit Integers/Zahlen
print(listeVonIntegers)
listeVonFloats = [1.1,2.2,3.3,4.4,5.5]  # Liste mit Kommazhalen/Floats
print(listeVonFloats)
listeVonListen = [[1,3],[3,7]] # Liste mit Listen/Arrays
print(listeVonListen)

## Elemente anhängen ##
listeVonIntegers.append(9)              # Element an Ende der Liste anhängen, im Beispiel steht die "9" dann hinter der 7
print(listeVonIntegers)
listeVonIntegers.insert(2,8)            # (Index(2), Element(8)) wird an Liste angehängt, im Beispiel vor die 0, 
                                        # da bei 0 angefangen wird zu zählen
print(listeVonIntegers) 
print(listeVonIntegers +[10,11,12,13])  # Listen verknüpfen, neue Liste wird eifach rangehängt

## Elemente einer Liste auslesen und anpassen - Liste[Start:Ende] ##
print(listeVonIntegers[0])      # erstes Element
listeVonIntegers[0] = 99        # Überschreibt den Wert bei Index 0 mit dem Wert 99
print(listeVonIntegers[0])
print(listeVonIntegers[-1])     # letztes Element
print(listeVonIntegers[2])      # Elemente an indizierter Stelle (3. Element/Index 2)
print(listeVonIntegers[1:3])    # Element von Start (ausschließlich) bis Ende (ausschließlich)
print(listeVonIntegers[:3])     # Element von Start bis Ende (ausschließlich)
print(listeVonIntegers[:2])     # Element von Start (einschließlich) bis Ende

##  Erweitertes Slicing - Liste [Start:Ende:Schrittweite] ##
print(listeVonIntegers[::1])    # gibt jedes Element einer Liste zurück
print(listeVonIntegers[::2])    # gibt jedes zweite Element einer Liste zurück
print(listeVonIntegers[::-1])   # gibt jedes Element einer Liste in Umgekehrter Reihenfolge zurück
print(listeVonIntegers[1:-1:2]) # gibt jedes zweite Element zwischen dem zweiten und letzten zurück

## Elemente entfernen ##
listeVonIntegers.remove(7)      # erstes Element mit Wert 7 entfernen
print(listeVonIntegers)
listeVonIntegers.remove(listeVonIntegers[1])    # Element an Index 1 entfernen
print(listeVonIntegers)
print(listeVonIntegers.pop())   # entfernt und gibt das letzte Element der Liste zurück
print(listeVonIntegers)

## Kennzahlen ##
print(len(listeVonIntegers))    # Länge der Liste/Anzahl der Zahlen in der Liste
print(min(listeVonIntegers))    # Kleinste Zahl in der Liste
print(max(listeVonIntegers))    # Größte Zahl in der Liste
print(sum(listeVonIntegers))    # Summe aller Zahlen in der Liste

## Methoden für Listen ##
print(listeVonIntegers.index(2))    # gibt Index von erstem Element mit Wert 2 zurück
print(listeVonIntegers.count(9))    # gibt Anzahl von Elementen mit Wert 9 zurück
listeVonIntegers.sort()             # sortiert (aufsteigend) die Elemente/Zahlen der Liste
print(listeVonIntegers)
listeVonIntegers.reverse()          # kehrt Reihenfolge der Elemente in der Liste um
print(listeVonIntegers)

## Bestimmtes Element in Liste suchen ##
print(21 in listeVonIntegers)
print(99 in listeVonIntegers)

## Schleifendurchlauf durch Elemente der Liste ##
for element in listeVonIntegers:
    print(element)

## Liste kopieren ##
print(listeVonIntegers)

# 1. Referenz auf eine bestehende Liste #
kopiertelisteVonIntegers = listeVonIntegers
kopiertelisteVonIntegers.append(87)
print(kopiertelisteVonIntegers) # Wird der Kopie etwas hinzugefügt, wird es auch dem Original hinzugefügt
print(listeVonIntegers)         # Ist eine Referenz (Kopie==Original)

# 2. Kopie einer bereits bestehenden Liste erstellen #
kopiertelisteVonIntegers2 = listeVonIntegers[:]
kopiertelisteVonIntegers2.append(77)
print(kopiertelisteVonIntegers2) # Wird der Kopie etwas hinzugefügt, ist es nur in der Kopie
print(listeVonIntegers)
