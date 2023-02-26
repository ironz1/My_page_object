import random

print('Turniej Wroclaw 2023')
Kuba = 8
Janek = 1
Hubert = 8
Kamil = 2
Antek = 7
Wiktor = 8
Kacper = 100

# print(f'Zespół APO zdobył razem {Kuba+Janek+Hubert+Kamil+Antek+Wiktor+Kacper} goli')
# x = random.randint(1,10)

lista = ['Kuba', 'Janek', 'Hubert', 'Kamil', 'Antek', 'Wiktor']
lista2 = {'Kuba': 8, 'Janek': 2, 'Hubert': 8, 'Kamil': 5, 'Antek': 8, 'Wiktor': 10}

najwiecej_goli = 0
krol_strzelcow = ''
# for name in lista:
#     gole = random.randint(0, 10)
#
#     print(f'{name} strzelił {gole} goli')
#     if gole > najwiecej_goli:
#         najwiecej_goli = gole
#         krol = gole
#         krol_strzelcow = name

for key in lista2:
    if lista2[key] > 3:
        minimal = 3
    else:
        minimal = 0
    gole = random.randint(minimal, lista2[key])
    print(f'{key} strzelił {gole} goli')
    if gole > najwiecej_goli:
        najwiecej_goli = gole
        krol = gole
        krol_strzelcow = key

print(f'Królem strzelców jest {krol_strzelcow}')