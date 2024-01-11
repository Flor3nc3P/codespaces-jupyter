# Testing and Learning
# Block 1: IF-Schleife
# IF Abfrage mit Bedingung und elif als zweite Bedingung falls erste false ergibt.
# Mit dem logischen AND Operator ist es mir möglich, eine IF Abfrage mit mehreren Bedingungen in eine Abfrage zu formulieren.

# Block 2: Funktionen erstellen und aufrufen


print("Block 1")
# Beispiel anhand einer Altersabfrage fürs Casino
# Casinos und ihre Glücksspiele sind ab 18, also:

age =int (input("How old are you? "))
if age < 18:
    print("You are not allowed to play in the Casino, sry.")

elif age == 18:
    print("Almost, welcome at the Lottery!\n")
    number1=int(input("Type your first Number: \n"))
    number2=int(input("Type your second Number: \n"))
    number3=int(input("Type your third Number: \n"))
    #Gewinnerzahl ist die 777
    if number1 == 7 and number2 == 7 and number3 ==7:
        print("Congratulation, you should play in a real Casino!")

else:
    print("Warning: Gambling can be addictive")    

print("Casino closed")    


print("Block 2")
# Funktion mit Rückgabewert erstellen und aufrufen.

def aufrufen():
    print("My first Function in Python")
    print("Text in Function")

aufrufen()

name = "Bumble"
nachname = "Bee"

def name_aufrufen(name, nachname):
    print("Hello " + name + " " + nachname) 
    print("Text in Function")

name_aufrufen(name, nachname) # name_aufrufen("Bumble", "Bee")
print(name_aufrufen)

# Funktionswert zurückgeben

a = 8
b = 10

def maximum(a, b):
    if a<b:
        return b
    else:
        return a
    
result = maximum(a, b) # result = maximum(8, 10)
print(result)
print(type(result)) # print(type(...)) "type" zeigt mir den verwendeten Datentyp von der Variable in der folgenden Klammer.
 