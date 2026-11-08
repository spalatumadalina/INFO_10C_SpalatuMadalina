from enum import Enum
class Anotimp(Enum):
    PRIMAVARA = 1
    VARA = 2
    TOAMNA = 3
    IARNA = 4
cod = int(input("Introdu codul: "))
print(Anotimp(cod).name)
print(Anotimp(cod).value)