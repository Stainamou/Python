import random

autot = []

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.tämänhetkinen_nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimäärä):
        if self.tämänhetkinen_nopeus > 0:
            kuljettu_matka = tuntimäärä * self.tämänhetkinen_nopeus
            self.kuljettu_matka += kuljettu_matka

for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(uusi_auto)

kilpailun_tila = True
while kilpailun_tila:
    for auto in autot:
        auto.kiihdytä(random.randint(-15, 10))

    for auto in autot:
        auto.kulje(1)

    if any(auto.kuljettu_matka >= 10000 for auto in autot):
        kilpailun_tila = False
        break

for auto in autot:
    print(f"Rekisteritunnus: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}, tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus},"
          f"kuljettu matka: {auto.kuljettu_matka}")





