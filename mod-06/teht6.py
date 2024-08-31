import math

def pizza(halkaisija, hinta):
    säde = halkaisija / 2
    pinta_ala = math.pi * säde**2
    pinta_ala = pinta_ala / 10000
    hinta_per_neliömetri = hinta / pinta_ala
    print(f"Pinta-ala on {pinta_ala:.2f}m^2")
    print(f"Hinta per neliömetri on {hinta_per_neliömetri:.2f}€")
    return hinta_per_neliömetri

eka_pizza_halkaisija = float(input("Anna ekan pizzan halkaisija senttimetreinä: "))
eka_pizza_hinta = float(input("Anna ekan pizzan hinta euroina: "))
toka_pizza_halkaisija = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
toka_pizza_hinta = float(input("Anna toisen pizzan hinta euroina: "))

pizza1_hinta_per_neliömetri = pizza(eka_pizza_halkaisija, eka_pizza_hinta)
pizza2_hinta_per_neliömetri = pizza(toka_pizza_halkaisija, toka_pizza_hinta)

if pizza1_hinta_per_neliömetri < pizza2_hinta_per_neliömetri:
    print("Ensimmäinen pizza on hintalaatu suhdeltaan parempi")
elif pizza2_hinta_per_neliömetri < pizza1_hinta_per_neliömetri:
    print("Toinen pizza on hintalaatu suhdeltaan parempi")
else:
    print("Pizzat ovat sama laatuisia")