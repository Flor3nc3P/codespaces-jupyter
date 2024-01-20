# programmieren starten Video 22/24 Klasse  und Objekte
# __init__ ist eine Funktion (bzw. Methode, da innerhalb einer Klasse definiert)
# Methoden haben einen (self) Parameter, Funktionen nicht
# self beinhaltet eine Referenz auf das aufrufende Objekt
# def definiert eine Funktion/ wird vor die Funktion geschrieben


# Klasse Auto anlegen und für das Auto Eigenschaften/Atribute anlegen
class Car:
    def __init__(self):
        # Atribute das das Auto haben soll
        self.car_brand=None
        self.horse_power=None
        self.color=None
        self.car_model=None	
        self.x_position = 5
        self.y_position = 5

# Referenz auf die Klasse Auto in Variable car1 gespeichert
        
car1=Car() 
# Werte noch leer
print(car1.car_brand)

# car_brand einen neuen Wert zuweisen
car1.car_brand = "BMW"
car1.color = "ROT"
car1.horse_power = 350
print(car1.car_brand,car1.color,car1.horse_power)


car2=Car()
car2.car_brand = "BMW"
car2.car_model = "M2"
car2.horse_power = 460
car2.color = "Metallic ROT"

print(car2.car_brand,car2.car_model,car2.horse_power,car2.horse_power)

# Gibt den Speicherbereich/Referenz/Adresse in dem alle Daten des erzeugten Objekts gespeichert sind
print(car1)
print(car2)

# car3 speichert die Referenz aus car1 und hat dementsprechend genau die selbe Referenz wie car1
car3 = car1
print(car3)


def drive(self,x,y):
    self.x_position += x
    self.y_position += y





