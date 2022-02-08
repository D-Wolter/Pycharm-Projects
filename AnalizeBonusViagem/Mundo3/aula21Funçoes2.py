#interactive Help

help(input)
#print(input.__doc__)


#docstrings
def contador(i,f, p):
    """
    Faz contagem e mostra na tela
    :param i: inicio da contagem
    :param f: ultimo numero contagem
    :param p: razao
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')

help(contador)


#argumentos opcionais
def soma(a, b, c=0):#criando um argumento opcional se nao passar valor assumi zero
    s = a + b + c
    print(f'A soma vale {s}')
soma( 3, 2, 5 )
soma(8, 4 )


#escopo de variaveis
def teste(b):
    global a  #tranforma a variavel dentro desse escopo globla
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale(a)')
    print(f'B dentro vale(b)')
    print(f'C dentro vale(c)')
a = 5  #foi anulada pela variavel global criada
teste(a)
print(f'A fora vale {a}')

#retorno de resultados
def somar( a=0, b=0, c=0 ):
    s = a + b + c
    return s  #retorna variavel s para o global=> na variaveia abaixo r1 r2 e r3
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'os resultados foram {r1}, {r2} e {r3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um numero'))
print(par(num))# True or False