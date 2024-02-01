# ## Kann als Break benutzt werden. :)

##
testString = "Hello World =)"
print(testString)

# AUSGABE ##
# Hello World =)

##
# Prüfen ob ein bestimmtes Zeichen oder ein Wort in einem String vorkommt, 
# entweder mit der .find() oder der .index() Funktion.

print(testString.find("World"))
print(testString.find("Wrld")) # gibt -1 zurück, wenn nicht gefunden
print(testString.index("World")) # gibt Fehlermeldung zurück, wenn nicht gefunden

# AUSGABE ##
# 6
# -1
# 6

# Die Funktionen geben jeweils den Index der Position an, 
# an der das gesuchte Wort oder Zeichen zum ersten Mal gefunden wird.
# Wenn nichts gefunden wurde gibt die .find() Funktion den Wert -1 und 
# die .index() Funktion eine Fehlermeldung zurück.

##
# Die len() Funktion kann abfragen wie viele Zeichen in einem String enthalten sind.

print(len(testString))

# AUSGABE ##
# 14

# if len(testString) größer 0 kann abfragen ob der String leer ist:
if len(testString)>0:
    print("Der String ist nicht leer")

else: print("Der String hat keinen Inhalt")

##
# Die Funktion .count() kann genutzt werden um zu zählen,
# wie häufig ein bestimmtes Zeichen in einem String vorkommt.

print(testString.count("l"))

# AUSGABE ##
# 3

##
# Mit der Funktion .isalpha() kann überprüft werden,
# ob ein String ausschließlich aus Buchstaben besteht.
# Analog dazu kann .isalnum() überprüfen,
# ob dei String ausschließlich Zahlen enthält.

print(testString.isalpha())
print("abcdefg".isalpha())
print(testString.isalnum())
print("123456".isalnum())

# AUSGABE ##
# False
# True
# False
# True