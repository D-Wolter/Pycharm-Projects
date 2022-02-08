'''
#CALCULAR DESCONTO
preço = 100
desconto = (preço*5/100)
valorfinal = preço-desconto
print(valorfinal)

#prof cod
#calcula o valor de 5 porcento de 10 reais
print(10*5/100)

#calcula o valor de 10 porcento de 1500 reais
print(1500*10/100)

#calcula o valor de 15 poecento de 875 reais
print(875*15/100)

'''

valor = float(input('digite o valor'))
desc = int(input('digite o desconto'))
vdesc = (valor*desc/100)
descontado = valor - vdesc
print('o produto custa {:.2f}reais, mas com desconto de {}% de desconto vai custar {:.2f}reais'.format(valor, desc, descontado))