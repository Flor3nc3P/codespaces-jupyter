# Geldwechsel Übung aus ThInf Skript Seite 17
# Wechselkurs und Dollar_Betrag sind die Eingabewerte als float 
# float sind Gleitkommazahlen (Zahlen mit Dezimalstellen)
# Euro_Betrag ist die Division aus dem Dollar_Betrag und dem Wechselkurs
# Zum Schluss wird der Euro_Betrag ausgegeben mit .2f
# .2f sind zwei Nachkommastellen


Wechselkurs = float(input("Aktueller Dollarkurs pro Euro: \n"))
Dollar_Betrag = float(input("Dollarbetrag: \n"))

Euro_Betrag = Dollar_Betrag / Wechselkurs

print(f"Der Umtauschwert von {Dollar_Betrag} Dollar ist {Euro_Betrag:.2f} Euro.")
