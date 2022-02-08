n = int(input('digite um numero [999 para parar]'))
cont = 0
soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('digite um numero [999 para parar]'))
print('Voce digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

