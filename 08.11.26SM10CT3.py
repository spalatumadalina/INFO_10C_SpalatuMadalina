from enum import Enum
class Culoare(Enum):
    ROSU = 1
    GALBEN = 2
    VERDE = 3
for culoare in Culoare:
    print(culoare.name, culoare.value)