

entrada = input('Digite algo')

print(type(entrada))

print('é numerico', (entrada.isnumeric()))
print('e alfabetico', (entrada.isalpha()))
print('é alfanumerico', (entrada.isalnum()))
print('é algum digito', (entrada.isdigit()))
print('sao maiusculas', (entrada.isupper()))
print('sao minusculas', (entrada.islower()))
print('sao espaços', (entrada.isspace()))


a = input('Digitwe algo') #Daniel Wolter
print('o tipo primitivo desse valor é', type(a)) #class str
print('so tem espaços?', a.isspace()) #False or true
print('é um numero?', a.isnumeric())
print('é alfabetico', a.isalpha())
print('é alfa numerico?', a.isalnum())
print('ésta em maisculas', a.isupper())
print('esta em minusculas', a.islower())
print('esta capitalizada', a.istitle())

print('DWM'*20)
print(5+3*2)#11
print(5**2)#5 ao quadrado == 25
print(5**3)#cinco ao cubo == 125
print(19//2)#divisao inteira == 9
print(19/2)# == 9.5
print(18%2)#resto da divisao == 0
print(122%3)#resto da divisao == 2
print(4**3)# quatro ao cubo == 64
print(pow(4,3))# quatro ao cubo == 64

print('pazre em conhecer {:>20}!'.format(a))## exibir o escrito em input em 20 caracter alinhado a direita
#pazre em conhecer        Daniel Wolter!

print('pazre em conhecer {:@^20}!'.format(a))#pazre em conhecer @@@daniel wolter@@@@!
print('pazre em  \n conhecer {:@^20}!'.format(a))
#pazre em
# conhecer @@@daniel wolter@@@@!

print('pazre em conhecer {:@^20}!'.format(a), end=(' XXX '))
#pazre em conhecer @@@@@@dani wol@@@@@@! XXX