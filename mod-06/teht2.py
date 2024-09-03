import random

def noppa(tahkot):
    heitto = random.randint(1, tahkot)
    return heitto

max_määrä = int(input("Anna maksimisilmäluku: "))
tahkot = int(input("Anna tahkojen määrä: "))
tulos = noppa(tahkot)

while tulos != max_määrä:
    tulos = noppa(tahkot)
    print(tulos)
