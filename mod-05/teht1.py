import random

lukumäärä = int(input("Anna arpakuutioiden lukumäärä: "))
noppa = []

for i in range(lukumäärä):

    heitto = random.randint(1, 6)
    noppa.append(heitto)

print(noppa)
print("Arpakuutioiden summa on", sum(noppa))
