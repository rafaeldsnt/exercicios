
d3 = d1 = {"a": 1, "b" : 2}
d2 = {"b": 3, "d" : 4}

for itemd in d1.values():
    print(itemd)

d1.update(d2)
d2.update(d3)

print("Dicionário de dados D1")
for itemd1 in d1.values():
    print(f" Valor : {itemd1}")

print("Dicionário de dados D2")
for itemd2 in d2.values():
    print(f" Valor : {itemd2}")

print("Dicionário de dados D3")
for itemd3 in d3.values():
    print(f" Valor : {itemd3}")