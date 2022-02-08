# lista = []
# player = {}
# gols = []
# sgol  = 0
# while True:
#     sgol = 0
#     gols.clear()
#     player.clear()
#     player['indi'] = 0
#     player['nome'] = str(input(f'Nome do Jogador: '))
#     player['partidas'] = int(input(f'Quantas partidas {player["nome"]} jogou? '))
#     for v in range(1, player['partidas']+1):
#         temp = int(input(f'Quantos gols na partida {v}? '))
#         gols.append(temp)
#         sgol += temp
#     player['sgol'] = sgol
#     player['gols'] = gols.copy()
#     lista.append(player.copy())
#     resp = str(input(f'Quer continuar [S/N] '))
#     if resp not in 'sSnN':
#         resp = str(input(f'ERRO escolha [S/N] '))
#     if resp in 'sS':
#         break
# print('-=' * 30)
# print('cod nome            gols               total')
# print('-' * 50)
# for i, v in enumerate(lista):
#     print(f'  {i} {v["nome"]}     {v["gols"]}        {v["sgol"]}')
# print('-' * 50)
# conti = int(input('Mostrar detalhes dos gols de qul jogador? (999 para sair) '))
# for i, v in enumerate(lista):
#     if conti == v['sgol']:
#         print(f'No jogo {i} fez {v["sgol"]} gols.')
#




#cod prof
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quanta partidas {jogador["nome"]} jogou ?'))
    partida.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp  in 'SN':
            break
        print('ERRo Responda apenas [S/N]')
    if resp == 'N':
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:3>} ', end='')
    for d in v.values():
        print(f'{str(d):<15}')
    print()
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'     => na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}!')
    else:
        print(f'  -- Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols.')
