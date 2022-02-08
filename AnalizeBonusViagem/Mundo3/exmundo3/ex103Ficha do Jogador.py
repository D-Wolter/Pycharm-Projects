#
# def ficha(nome='', gols=''):
#     if nome == '':
#         nome = '<desconhecido>'
#     elif gols == '':
#         gols = 0
#     print(f'O jogador {nome} fez {gols} no campeonato')
#
#
# nome = str(input('Nome do jogador'))
#
# gols = str(input('Numero de Gols'))
# ficha(nome, gols)



#cod prof
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
    #programa pricipal
n = str(input('Nome do Jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
