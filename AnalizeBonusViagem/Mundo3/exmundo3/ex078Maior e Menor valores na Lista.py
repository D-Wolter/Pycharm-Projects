# cod prof

listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f'digite um numero para posicao {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'voce digitou os valores {listanum}')
print(f'omaior numero digitado foi {mai} nas posiçoes ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'omenor valor digitado foi {men} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()



# valor = []
# valores= []
# cont = 0
# posMax = []
# posMin = []
# while cont <= 4:
#     valor = int(input(f'Digite um valor para Posição {cont}: '))
#     if 0 <= valor <= 9:
#         cont += 1
#         valores.append(valor)
#     else:
#         print('voce deve digitarnumeros de 0 a 9')
#
# print(min(valores))
# print(valores.index(min(valores)))
# min = [valores.index(min(valores))]
#
# print(max(valores))
# print(valores.index(max(valores)))
# max = [valores.index(max(valores))]
#
# print(f'Voce digitou os valores {valores}')
#
#



