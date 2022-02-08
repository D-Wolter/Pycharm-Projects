# valores = []
# impares = []
# pares = []
# for n in range(0, 7):
#     valor = int(input(f'Digite o {n+1}o. valor: '))
#     valores.append(valor)
# for nu in valores:
#     if nu % 2 == 0:
#         pares.append(nu)
#     else:
#         impares.append(nu)
# impares = sorted(impares)
# pares = sorted(pares)
# print(f'os valores pares digitados foram: {pares}')
# print(f'os valores impares digitados foram {impares}')

#cod prof

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'digite o {c}o. valor'))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'os valores pares digitados foram {num[0]}')
print(f'os valores impares digitados foram {num[1]}')