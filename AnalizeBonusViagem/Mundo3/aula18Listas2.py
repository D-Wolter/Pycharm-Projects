
dados =['pedro', 25]

pessoas = []
pessoas.append(dados[:])
pessoas = [['pedro', 25], ['maria', 19], ['joao', 32], ]
print(pessoas[0][0])#pedro
print(pessoas[1][0])#maria
print(pessoas[2][0])#joao
print(pessoas[1])#['maria', 19]

for p in pessoas:
    print(p)
    # ['pedro', 25]
    # ['maria', 19]
    # ['joao', 32]
    print(f'{p[0]} tem {p[1]} anos de idade.')


galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores de idade.')