class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, hetk_nopeus, kulj_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetk_nopeus = hetk_nopeus
        self.kulj_matka = kulj_matka

auto = Auto("ABC-123", 142, 0, 0)
print(f"Rekisteritunnus: {auto.rekisteritunnus:s}, huippunopeus: {auto.huippunopeus:d} km/h, hetkellinen nopeus: {auto.hetk_nopeus:d} km/h, kuljettu matka: {auto.kulj_matka:d} km")