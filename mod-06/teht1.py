import random
def noppa():
    heitto = random.randint(1,6 )
    return heitto

tulos = noppa()

while tulos != 6:
    tulos = noppa()
    print(tulos)