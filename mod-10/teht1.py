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

hissi = Hissi(0, 10)
hissi.siirry_kerrokseen(10)
hissi.siirry_kerrokseen(1)