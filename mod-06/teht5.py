kokonaisluvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def palauta_parittomat(lista):
    parittomat = []
    for i in lista:
        if i % 2 != 0:
            parittomat.append(i)
    return parittomat

print(f"Alkuperäiset luvut ovat: {kokonaisluvut}")
print(f"Parittomat luvut ovat: {palauta_parittomat(kokonaisluvut)}")