
#leia um numero ate 9999
numero = input('digite um nuimero de 0 a 9999')

print('unidade',numero[3])
print('dexena',numero[2])
print('centena',numero[1])
print('milhar',numero[0])



#solucao professor
num = int(input('digite um numero de 0 a 9999'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analizando numero {}'.format(num))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))


