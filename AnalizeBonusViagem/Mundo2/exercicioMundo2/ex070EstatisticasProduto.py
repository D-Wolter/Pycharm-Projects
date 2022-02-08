
total = 0
mais1000 = 0
nomebarato = ''
mbarato = 0.0
while True:
    produto = str(input('Nome do produto')).strip()
    valor = float(input(f'Qual o valor do {produto}'))

    total += valor

    if valor > 1000:
        mais1000 += 1

    if mbarato == 0.0 or valor < mbarato:
        mbarato = valor
        nomebarato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'o total gasto na compra é de R${total:.2f}')
print(f'fORAM COMPRADOS {mais1000} PRODUTOS DE MAIS DE 1000 REAIS')
print(f'o produto mais barato foi o {nomebarato}')


