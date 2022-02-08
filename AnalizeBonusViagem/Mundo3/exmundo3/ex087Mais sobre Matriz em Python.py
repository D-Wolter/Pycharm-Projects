# tabela = []
# somapares = 0
# s3coluna = 0
# s2linha = []
# for n in range(0, 3):
#     tabela.append(int(input(f'digite um valor para [0, {n}: ')))
# s3coluna += tabela[2]
# for n in range(0, 3):
#     tabela.append(int(input(f'digite um valor para [1, {n}: ')))
#
#
# s3coluna += tabela[5]
# for n in range(0, 3):
#     tabela.append(int(input(f'digite um valor para [2, {n}: ')))
#
# s3coluna += tabela[8]
# s2linha.append(tabela[3])
# s2linha.append(tabela[4])
# s2linha.append(tabela[5])
# maximo = (max(s2linha))
# print('-=' * 30)
# print(
#     f'\n [ {tabela[0]} ][ {tabela[1]} ][ {tabela[2]} ]\n [ {tabela[3]} ][ {tabela[4]} ][ {tabela[5]} ]\n [ {tabela[6]} ][ {tabela[7]} ][ {tabela[8]} ]')
# print('-=' * 30)
#
# for v in tabela:
#     if v % 2 == 0:
#         somapares += v
#
# print(f'a soma dos valores pares é {somapares}')
# print(f'a soma dos valores da terceira coluna é {s3coluna}')
# print(f'o maior valor da segunda linha é {maximo}')





#cod prof
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar  = mai = men = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor para linha {l+1} coluna {c+1}: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'a soma dos alores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]#soma os numeros na que tem index 2 na coluna
print(f'a soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if mai ==0:
        mai = matriz[1][c]
    elif matriz[1][c]:
        mai = matriz[1][c]
print(f'o maior valor da segunda linha é {mai}.')