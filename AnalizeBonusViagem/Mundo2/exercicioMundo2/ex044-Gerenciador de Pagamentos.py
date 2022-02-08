#elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e
#condiçoes de pagamento

#a vista dinheiro ou cheque 10% desconto
#avista no cartao 5% de desconto
#em ate 2x no cartao preço normal
#em 3x ou mais 20% de juros

produto = 120.50

pagamento = int(input('escolha a forma de pagamento \n'
                      '(1) a vista no dinheiro ou cheque \n'
                      '(2) a vista do cartao de credito \n'
                      '(3) em ate 2x no cartao de credito \n'
                      '(4) em 3x ou mais no cartao de credito \n'
                      '        ESCOLHA A OPCAO DE 1 A 4'))
if pagamento != 1 and pagamento != 2 and pagamento != 3 and pagamento != 4:
    print('voce deve indicar o numero de 1 ate 4')

desconto10 = (produto*10/100)
desconto5 = (produto*5/100)
juros20 = (produto*20/100)


if pagamento == 1:
    print('voce escolheu a opcao a vista no dinheiro oe cheque e o valor recebe 10% \n'
          'de desconto, valor de {} reais'.format(produto-desconto10))
if pagamento == 2:
    print('voce escolheu pagamento a vista no cartao \n'
          'recebe 5% de desconto e paga o valor de {:.2f} reais'.format(produto-desconto5))
if pagamento == 3:
    total = produto
    print('voce escolheu pagamento em 2x no cartao \n'
          'nao tem direito a desconto o valor fica em duas parcelas de {:.2f} reais'.format(total/2))
if pagamento ==4:
    total = produto+juros20
    parcelas = int(input('quantas parcela deseja ate 10 vezes'))
    print('voce escolheu pagar parcelado \n'
          'o valor vai ser de {} parcelas de {:.2f} reais no total de {:.2f} reais'.format(parcelas, (total/parcelas), total))