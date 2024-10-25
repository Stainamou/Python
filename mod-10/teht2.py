class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, haluttu_kerros):
        while self.nykyinen_kerros < haluttu_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > haluttu_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on kerroksessa: {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros >  self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksesa: {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.alin_kerros_numero = alin_kerros
        self.ylin_kerros_numero = ylin_kerros
        self.hissien_lukumäärä = hissien_lukumäärä
        self.hissit = []

        for i in range(hissien_lukumäärä):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissi_numero, kohdekerros):
        if 0 <= hissi_numero < self.hissien_lukumäärä:
            self.hissit[hissi_numero].siirry_kerrokseen(kohdekerros)

talo = Talo(0, 10, 3)

talo.aja_hissiä(0, 5)

talo.aja_hissiä(1, 1)
