#refaça o desafio 035 dos tringulos, acrescentando o recurso de mostrar que tipo de tringulo sera formado:
#Equilátero todos os lados iguais
#Isósceles dois lados iguais
#Escaleno todos os lados diferentes

'''
r1 = float(input('digite o valor da primeira reta'))
r2 = float(input('digite o valor da segunda reta'))
r3 = float(input('diite o valor da terceira reta'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("a reta 1 de {} a reta 2 de {} e a reta 3 de {} podem formar um triangulo".format(r1, r2, r3))

else:
    print("a reta 1 de {} a reta 2 de {} e a reta 3 de {} NAO 5.PODEM FORMAR TRIAGULO")

if r1 == r2  == r3:
    print('O tringulo é Equilátero e tem todos os lados iguais')
elif r1 != r2 and r2 == r3:
    print('o triangulo é Isósceles com dois lados iguais')
elif r1 == r2 and r1 != r3:
    print('o triangulo é Isósceles com dois lados iguais')
elif r1 != r2 and r3 != r1 and r2 != r3:
    print('o triangulo é escaleno com todos lados diferntes')
'''

#cod prof

l1 = float(input('primeiro segmento'))
l2 = float(input('segundo segumento'))
l3 = float(input('terceiro segumento'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print('Os segmentos acima podem forma tringulo ', end='')
    if l1 == l2 == l3:
        print("equilatero")
    elif l1 != l2 != l3 != l1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('os segmentos acima nao podem formar triagulo')