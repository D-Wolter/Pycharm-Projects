

lanche = ('lapis', 1.75, 'Borracha', 2, 'caderno', 15.9, 'estojo', 25, 'tranfer', 4.5, 'compasso', 9.99,
            'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90)
nome = 'LISTAGEM DE PREÇOS'
print('-'*40)
print(f'{nome: ^40}')
print('-'*40)
for cont in range(0, len(lanche)):
    if cont % 2 == 0:#separa as pares que sao os prodiutos e inpares os precos
        print(f'{lanche[cont]:.<30}', end='')#alinhado a direita
    else:
        print(f'R${lanche[cont]:>7.2f}')#alinhado na ersquerda
print('-'*40)

# ----------------------------------------
#            LISTAGEM DE PREÇOS
# ----------------------------------------
# lapis.........................R$   1.75
# Borracha......................R$   2.00
# caderno.......................R$  15.90
# estojo........................R$  25.00
# tranfer.......................R$   4.50
# compasso......................R$   9.99
# mochila.......................R$ 120.32
# canetas.......................R$  22.30
# livro.........................R$  34.90
# ----------------------------------------