import math
import statistics

# Absolut Wert
print(abs(-20.08))

# Runden
print(round(2.4))
print(round(2.5))
print(round(2.6)) # ab 0.6 wird aufgerundet
print(round(2.4567,3)) # ,3 um auf 3 Nachkommastellen zu runden

print(math.ceil(2.3)) # Aufrunden mit math.ceil
print(math.floor(2.3)) # Abrunden mit math.floor

# Kennzeichen einer Zahlenreihe
zahlenreihe = [1,2,2,3,4,5,6,7,7,7,7,8,1,2,3]
print(min(zahlenreihe)) # Minimum
print(max(zahlenreihe)) # Maximum
print(sum(zahlenreihe)) # Summe

print(statistics.mean(zahlenreihe)) # Durchschnitt mit statistics.mean
print(statistics.median(zahlenreihe)) # Median (Mittelwert) mit statistics.median
print(statistics.stdev(zahlenreihe)) # Standartabweichung statistics.stdev
print(statistics.variance(zahlenreihe)) # Varianz statistics.variance




