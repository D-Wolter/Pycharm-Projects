# valores = []
# pares = []
# impares = []
# resp = 's'
#
# cinco = False
# while resp in 'sS':
#     valor = int(input('Digite um valor: '))
#
#
#     valores.append(valor)
#
#     resp = str(input('Quer Continuar [S/N]'))
#     if valor == 5:
#         cinco = True
#
#     if resp not in 'sSnN':
#         resp = str(input('Quer Continuar [S/N]'))
#     if resp in 'nN':
#         break
#
# for v in valores:
#     if v % 2 == 0:
#         pares.append(v)
#     else:
#         impares.append(v)
#
# print(f'os valores digitados foram {valores}')
# print(f'os valores pares digitados foram {pares}')
# print(f'os valores impares digitados foram {impares}')

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('digite um numero')))
    resp = str(input('quer continuar [S/N]'))
    if resp in 'nN':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'a lista completa é {num}')
print(f'a lista de pares é {pares}')
print(f'alista de impares é {impares}')