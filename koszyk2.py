hodowla = [
    {'zwierze': 'kot', 'ilosc': 10, 'cena': 100},
    {'zwierze': 'pies', 'ilosc': 20, 'cena': 500},
    {'zwierze': 'kura', 'ilosc': 40, 'cena': 25}
]

suma = 0
for poz in hodowla:
    il = poz['ilosc']
    c = poz['cena']
    sum =  suma + (c * il)
    # print(c)
    # print(suma)
    #print(poz)
print(suma)
