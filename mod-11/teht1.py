class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivut):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivut = sivut

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Kirjailija: {self.kirjailija}")
        print(f"Sivut: {self.sivut}")

lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.tulosta_tiedot()
print()
kirja.tulosta_tiedot()