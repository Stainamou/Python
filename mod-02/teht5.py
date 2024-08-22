import math

leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

kokonnaisgrammat = float(leiviskät * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3)

kilogrammat = int(kokonnaisgrammat // 1000)
grammat = (kokonnaisgrammat % 1000)

print(f"Kokonnaispaino on {kilogrammat} kilogrammaa ja {grammat:.2f} grammaa")