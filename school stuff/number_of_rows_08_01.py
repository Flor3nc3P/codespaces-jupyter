# Speed

rows = int(input("Gib die Anzahl der Zeilen ein:"))
for i in range (1, rows + 1):
    for j in range (1, i + 1):
        print(i, end=" ")
    print()

# Kürzere Lösung:
# for i in range(int(input("Number"))): print(str(i)*i)        