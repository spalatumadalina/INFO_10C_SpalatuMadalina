from enum import Enum 
class Club(Enum):
    ROBOTICA = 1
    ARTA = 2
    SPORT = 3
alegere:Club = Club(int(input("Introdu alegerea: ")))
print(alegere.name)
print(alegere == Club.ROBOTICA)