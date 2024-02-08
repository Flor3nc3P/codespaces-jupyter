# Listen
# Sammlung von Elementen

## Leere Liste erstellen
listeLeer = []
print(listeLeer)
print(type(listeLeer))

## Liste von Strings, Integers, Floats, Listen ##
listeVonStrings = ["a","b","c"]
print(listeVonStrings)
listeVonIntegers = [9,21,0,1,2,3,4,5,6,7,8]
print(listeVonIntegers)
listeVonFloats = [1.1,2.2,3.3,4.4,5.5]
print(listeVonFloats)
listeVonListen = [[1,3],[3,7]] # Auch ein Array
print(listeVonListen)

## Elemente anhängen ##
listeVonIntegers.append(9) # Element an Ende der Liste anhängen
print(listeVonIntegers)
listeVonIntegers.insert(2,8) # Element an indizierte Stelle der Liste anhängen liste.insert(Index, Element)
print(listeVonIntegers) 
print(listeVonIntegers +[10,11,12,13]) # Listen verknüpfen

## Elemente einer Liste auslesen und anpassen - Liste[Start:Ende] ##
print(listeVonIntegers[0])      # erstes Element
listeVonIntegers[0] = 99        # Überschreibt den Wert an der Stelle mit Index 0 mit dem Wert 99
print(listeVonIntegers[0])
print(listeVonIntegers[-1])     # letztes Element
print(listeVonIntegers[2])      # Elemente an indizierter Stelle (3. Element)
print(listeVonIntegers[1:3])    # Element von Start (ausschließlich) bis Ende (ausschließlich)
print(listeVonIntegers[:3])     # Element von Start bis Ende (ausschließlich)
print(listeVonIntegers[:2])     # Element von Start (einschließlich) bis Ende

##   ##