#escreva um programa para aprova o emprestimo bancario para compra de uma casa, O programa vai perguntar o
#da casa, o salrio do comprador e em quantos anos ele vai pagar.
#caucule o valor prestaçao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

imovel = float(input('qual o valor do imovel'))
salario = float(input('qual o valor do salario'))
anos = int(input('digite quantos anos de financiamento'))

meses = anos * 12
limite33 = salario * 30 / 100
prestacoes = imovel // meses
prestacoes = round(prestacoes + 0.5)

print(meses)
print(limite33)
print(prestacoes)
if prestacoes <= limite33:
    print('emprestimo APROVADO! financiamentos de {:.2f} reais pelo periodo de {} meses pagando ${:.2f}reais'.format(imovel, meses, prestacoes))
else:
    print('emprestimo negado, voce tem o limite de {}reais para desconto mensal, procure um imovel de monor valor ou almente a quantidade de parcelas.'.format(limite33))