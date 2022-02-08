import moeda

p = float(input('digite um preçoR$'))
print(f'Ametade de {p} é {moeda.metade(p)}')
print(f'aumentando preço 20 % temos r$ {moeda.aumentar(p, 20)}')
print(moeda.moeda(p))