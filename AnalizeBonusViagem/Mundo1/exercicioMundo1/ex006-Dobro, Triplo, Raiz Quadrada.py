
#leia um numero mostre o dobro e o quadrado do numero

num = int(input('digite um numero'))
dobro = num*2
triplo = num*3
raiz = num**2
print('o numero escolhido é {}, o valor do dobro é {}, o triplo é {} e o valor da raiz quadrada é {}!'.format(num, dobro, triplo, raiz))


#prof cod
#leia um numero mostre o dobro  triplo e o raiz quadrada
nu = int(input('digite um numero'))
d = nu * 2
t = nu * 3
r = nu ** (1/2)
print('o dobro de {} vale {}, o triplo de {} vale {}, a raiz de {} VALE {:.2f}'.format(nu, d, nu, t, nu, r))

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} e igual a {}'.format(num, raiz))
print('A raiz de {} e igual a {:.2f}'.format(num, raiz))
print('A raiz de {} e igual a {}'.format(num, math.ceil(raiz)))         #arredonda rai pra cima
print('A raiz de {} e igual a {}'.format(num, math.floor(raiz)))          #arredonda raiz p baixo


