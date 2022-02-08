
#adicionar
lanche = ['batata','coca','hamburger']
lanche.append('nugets')#adiciona ao fim
print(lanche)#['batata', 'coca', 'hamburger', 'nugets']

lanche.insert(0,'bigMAc')#adiciona no numero do index desejado
print(lanche)#['bigMAc', 'batata', 'coca', 'hamburger', 'nugets']

#apagar remover
del lanche[3]#indica numero index
print(lanche)#['bigMAc', 'batata', 'coca', 'nugets']

lanche.pop(3)#indica numero index (vazio deleta o ultimo
print(lanche)#['bigMAc', 'batata', 'coca']

lanche.remove('coca')#indica valor literario
print(lanche)#['bigMAc', 'batata']

if 'batata' in lanche:
    lanche.remove('batata')
print(lanche)#['bigMAc']

valores = list(range(4, 11))#criar uma lista do 4 ate o 10
print(valores)#[4, 5, 6, 7, 8, 9, 10]

valores1 = [8,4,6,3,7,1,5]
print(valores1)#[8, 4, 6, 3, 7, 1, 5]
valores1.sort()
print(valores1)#[1, 3, 4, 5, 6, 7, 8]
valores1.sort(reverse=True)
print(valores1)#[8, 7, 6, 5, 4, 3, 1]


print(len(valores1))#7

num = [2,5,9,1]
copia = num[:]
num[2] = 3
num.append(7)
#NUM.POP(2) DELETA INDEX 2
num.insert(2, 2)
print(copia)
if 5 in num:
    num.remove(5)
else:
    print('nao achei o numero 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

numeros = []
numeros.append(5)
numeros.append(9)
numeros.append(4)

for cont, vlr in enumerate(numeros):
    print(f'na posiçao {cont+1} encontrei o valor {vlr}!')