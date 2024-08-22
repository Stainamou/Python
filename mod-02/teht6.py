import random


koodi1 = ''.join([str(random.randint(0, 9)) for i in range(3)])
koodi2 = ''.join([str(random.randint(1, 6)) for i in range(4)])

print("Ensimmäinen koodi on", koodi1, "ja toinen koodi on", koodi2)