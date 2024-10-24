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

    def kulje(self, tuntimäärä):
        if self.tämänhetkinen_nopeus > 0:
            kuljettu_matka = tuntimäärä * self.tämänhetkinen_nopeus
            self.kuljettu_matka += kuljettu_matka


auto = Auto("ABC-123", 142, 0, 2000)

auto.kiihdytä(60)
auto.kulje(1.5)
print(f"Tuntimäärä on: {auto.kuljettu_matka:.2f}")




