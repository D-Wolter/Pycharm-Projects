#exibaa tabuada de um numero
# numTabuada = 6
# contador = 1
# while (contador<99):
#     print(contador,numTabuada*contador)
#     contador = contador+1
#
#prof cod
num = int(input('digite um numero para ver a tabuada'))
contador = 1

while contador<11:
    print('{} x {:2}  =  {}'.format(num, contador, num*contador))
    contador = contador+1