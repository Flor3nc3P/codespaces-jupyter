# Scope auch Gloabe und Lokale Variablen
# Variablen sind nur in dem Bereich (Scope) verfügbar in dem sie erstellt wurde

# def --> definiert eine Funktion
# hier die Funktion ScopeTest
# diese wird mit () beendet und der Funktionsblock mit : eingeleitet

##
def ScopeTest():
    lokaleVariable = "lokale Variable"
    print(globaleVariable)
    print(lokaleVariable)    


globaleVariable = "globale Variable"

ScopeTest()
print(globaleVariable)
print(lokaleVariable)

# AUSGABE ##
# globale Variable
# lokale Variable
# globale Variable
# Error: "lokaleVariable" is not defined

# In übergeordneten Scops(Bereichen) kann auf Variablen in untergeordnete Funktionen zugegriffen werden, 
# aber nicht andersherum!

# Python arbeitet immer mit der möglichst spezifischeren Variable

# Wenn eine Variable mit gleichem Namen innerhalb und außerhalb einer Funktion genutzt wird,
# erstellt Python automatisch zwei verschiedene Variablen – eine globale sowie eine lokale.

##
def ScopeTest2():
    globaleVariable = "lokale Variable mit gleichem Namen"
    lokaleVariable = "lokale Variable"
    print(globaleVariable)
    print(lokaleVariable)    


globaleVariable = "globale Variable"
print(globaleVariable)

##
ScopeTest2()

print(globaleVariable)

# AUSGABE ##
# globale Variable
# lokale Variable mit gleichem Namen
# lokale Variable
# globale Variable

# Innerhalb der Funktion erstellt Python die lokale Variable, 
# während die globale unverändert bleibt.

# Um den Wert einer globalen Variable mit einer untergeordneten Funktion zu ändern, 
# solltest du am besten mit Rückgabewerten arbeiten.

##
def ScopeTest3():    
    return "geänderte globale Variable"


globaleVariable = "globale Variable"
print(globaleVariable)

globaleVariable = ScopeTest3()

print(globaleVariable)

# AUSGABE ##
# globale Variable
# geänderte globale Variable


# Es kann auch alternativ explizit mit dem Schlüsselwort „global“ auf die globale Variable 
# referenziert werden und anschließend damit gearbeitet werden.

## 
def ScopeTest4():
    global globaleVariable 
    globaleVariable = "geänderte globale Variable"
    print(globaleVariable) 


globaleVariable = "globale Variable"
print(globaleVariable)

ScopeTest4()

print(globaleVariable)

# AUSGABE ##
# globale Variable
# geänderte globale Variable
# geänderte globale Variable


