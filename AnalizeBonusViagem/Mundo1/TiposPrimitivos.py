

#verificar se existe valor dentro da variavel input
nome = str(input('digite seu nome'))

if nome != True:
    print('bem vindo {}'.format(nome))
else:
    print('voce deve digita seu nome')

#verificar a classe da variavel
print(type(nome))


#verificar se a  string tem apenas numeros para poder converter em numero ou usalas como numero
numero = '41'
numero2 = '4.4'

print(numero.isnumeric())
print(numero2.isnumeric())

#verificar se o input é letras

print(nome.isalpha())
