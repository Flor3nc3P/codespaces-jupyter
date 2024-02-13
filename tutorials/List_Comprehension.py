# List Comprehension / Listen-Abstraktion
# Kompakte Schreibweise um Listen zu erstellen


## Listen erstellen ##
manuelleListe = [0,1,2,3,4,5,6,7,8,9,10] # manuell erstellt
print(manuelleListe)

initialisierteListe = [zahl for zahl in range(11)] # Liste berechnen lassen
print(initialisierteListe)

## Liste aus den quadrierten Einträgen der initialisiertenListe erstellen ##
quadrierteListe = []
for zahl in initialisierteListe:
    quadrierteListe.append(zahl ** 2) # ausführlich
print(quadrierteListe)    

quadrierteListe2 = [zahl ** 2 for zahl in initialisierteListe] # kompackt
print(quadrierteListe2)

## Liste aller ungeraden Einträge der initialisierten Liste erstellen ## 
ungerade1 = []
for zahl in initialisierteListe:
    if zahl % 2 !=0:
        ungerade1.append(zahl) # ausführlich
print(ungerade1)

ungerade2 = [zahl for zahl in initialisierteListe if zahl % 2 !=0] # kompackt
print(ungerade2)

## Liste aus allen Kombinationen der Elemente aus zwei anderen Listen ##
kombiniert1 = []
for zahl in initialisierteListe:
    for buchstabe in "abc":
        kombiniert1.append((zahl, buchstabe)) # ausführlich
print(kombiniert1)

kombiniert2 = [(zahl, buchstabe) for zahl in initialisierteListe for buchstabe in "abc"] # kompackt
print(kombiniert2)
