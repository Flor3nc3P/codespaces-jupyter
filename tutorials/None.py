# None
# is vergleicht ob es sich um das gleiche Objekt handelt
# == vergleicht ob es sich um den gleichen Inhalt handelt

variable=None
print(variable)
print(type(variable))

## Testabfragen:

if variable == True:
    print("None is True")
elif variable == False:
    print("None is False")
elif variable == 0:
    print("")
elif variable == "":
    print ("")
elif variable in None:
    print("None ist nur None")

# Funktionen die nichts zurück geben, geben tatsächlich None zurück
def GibNoneZurueck():
    print("Funktion wird ausgeführt")

test = GibNoneZurueck()
print(test)

# Mit None kann nicht gerechnet werden!
print(1 + None)