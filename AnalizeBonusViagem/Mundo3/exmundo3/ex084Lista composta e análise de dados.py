#
# pessoas = []
#
# temp = []
# maior = 0
# menor = 0
# listmaior = []
# listmenor = []
# while True:
#     temp.append((input('Nome: ')))
#     temp.append((float(input('Peso: '))))
#     pessoas.append(temp[:])
#     temp.clear()
#     res = str(input('Quer continuar [S/N]'))
#     if res not in 'sSnN':
#         res = str(input('Quer continuar [S/N]'))
#     if res in 'nN':
#         break
#
# maior = (max(pessoas))
# menor = (min(pessoas))
# for p in pessoas:
#     if p[1] == maior[1]:
#         listmaior.append(p[0])
#     if p[1] == menor[1]:
#         listmenor.append(p[0])
#
#
# print(f'ao todo , voce cadastrou {len(pessoas)}.')
# print(f'o maior peso foi de {maior[1]} Peso de {listmaior} ')
# print(f'o menor peso foi {menor[1]} peso de {listmenor}')

#cod prof
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ)  == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar [S/N]'))
    if resp in 'nN':
        break
print('-='*30)
print(f'ao todo vovce cadasrtrou {len(princ)} pessoas')
print(f'omaior peso foi de {mai}kg. peso de ',end='')
for p in princ:
    if p[1]  == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'o menor peso foi de {men}kg. peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()


