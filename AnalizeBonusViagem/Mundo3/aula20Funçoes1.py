def nomeComplet():
    print('Daniel Wolter Martins')
def lin():
    print('----------------------------------------------------')
lin()
nomeComplet()
lin()

def mensagem(msg):
    print('----------------------------------------------------')
    print(msg)
    print('----------------------------------------------------')
mensagem('Restauros de Arte')

def parImpar(n):
    if n % 2 == 0:
        print(f'O Numero {n} é Par')
    else:
        print(f'O Numero {n} é Impar')
parImpar(11)

def divisao(a,b):
    d = a / b
    print(f'A divisão de {a} por {b} é igual a {d:.2f} ')
divisao(30, 4)
divisao(b=30, a=4)#podemos nomear a ordem

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores temos {s} ')
soma(30, 4)
soma(30, 4, 300)#podemos nomear a ordem


#   (*num) pode reber valores indefinidos em quantidade de uma tupla
def contador(*núm):#le varias tuplas  nomeadas com a funcao
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} Números')
    for valor in núm:
        print(valor, end='')
    print()
    print('fim')
contador(2, 1, 7)
contador(8,0)
contador(4, 4, 7, 6, 2)

#dobrando valores dendtro de uma lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)




