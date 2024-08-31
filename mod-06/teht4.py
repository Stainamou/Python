
lukuja = [1, 2, 3, 4, 5]
lukuja.append(6)

def summa_lista(list):
    summa = 0
    for i in list:
        summa += i
    return summa
print(summa_lista(lukuja))
