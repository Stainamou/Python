class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
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

auto = Auto("ABC-123", 142, 0, 0)

auto.kiihdytä(30)
print(f"Auton nopeus on: {auto.tämänhetkinen_nopeus:d} km/h")

auto.kiihdytä(70)
print(f"Auton nopeus on: {auto.tämänhetkinen_nopeus:d} km/h")

auto.kiihdytä(50)
print(f"Auton nopeus on: {auto.tämänhetkinen_nopeus:d} km/h")

auto.kiihdytä(-200)
print(f"Auton nopeus on: {auto.tämänhetkinen_nopeus:d} km/h")
