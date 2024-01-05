#beim BMI kann ich sehen wie man mit Hilfe von Variablen die einen Wert zugewiesen bekommen haben, rechnen kann.
#

print("Berechnung des Body Mass Index")

körpergröße = float(input("Gib deine Körpergröße ein (m): \n"))
körpergewicht = float(input("Gib dein Körpergewicht ein(kg): \n"))
BMI = körpergewicht / (körpergröße*körpergröße)

print(f"Dein BMI beträgt {BMI:.2f}kg/m.")
