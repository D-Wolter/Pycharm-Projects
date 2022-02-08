

jogador = {}
soma = 0
gols = []
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['njogos'] = int(input(f'Quanta partidas {jogador["nome"]} Jogou?'))
for v in range(0, jogador['njogos']):
    temp = int(input(f'Quantos gols na partida {v}? '))
    soma += temp
    gols.append(temp)
jogador['gols'] = gols[:]
print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'O campo nome tem o valor {jogador["nome"]}')
print(f'O campo gols tem o valor {gols}')
print(f'O campo total tem o valor {soma}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["njogos"]} partidas.')
for i, v in enumerate(gols):
    print(f'     => Na partida {i}, fez {v} gols')
print(f'Foi um total de {soma}')


