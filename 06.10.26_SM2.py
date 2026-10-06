Putere=int(input('Dati puterea(W):'))
Timp=int(input('Dati timpul(h):'))
Energie=Putere*Timp/1000
print(f'Spre achitare {Energie:.2f} kWh')
Tarif=float(input('Dati tariful actual:'))
Costul=Energie*Tarif
print(f'Spre achitare {cost:.2f} lei')