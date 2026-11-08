from enum import Enum
class Culoare(Enum):
    ROSU = 1
    GALBEN = 2
    VERDE = 3
c1 = Culoare(int(input(" Prima culoare: ")))
c2 = Culoare(int(input(" A doua culoare: ")))
print(c1.name, c2.name)
print(c1 == c2)