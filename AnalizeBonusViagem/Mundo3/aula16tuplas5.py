a =(2, 5 , 4)
b =(5, 8, 1, 2)
c = b + a#cocatena as tuplas a ordem faz diferenca
#conta quantas vezes aparece o numero 5
print(len(c))
print(c.count(5))

#prucura dentro da tupla onde aparece na primeira vez o 8
print(c.index(8))

print(c.index(2, 4))#podese indicar a partir de que index procurar no caso a partri do 4 procurar proximo dois

#deleta tupla
del(c)