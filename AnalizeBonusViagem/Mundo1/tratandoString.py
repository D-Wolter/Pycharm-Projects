#Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o
# Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(),
# title(), strip(), junção com join().


frase = '  Daniel Wolter Martins  '
print(len(frase))#25
#fatiamento de strings
print(frase[::2])# Dne otrMris
print(frase[0:13])# Daniel Wolt

print('Wolter'in frase)#True existe wolter na variavel
print(frase.find('Wol'))# 9 mostra o range de onde inicia

#print(variavel[inicio, fim, unidades])

print("""A revolucao acomteceu
deposde das gyerras
e alem""")

print(frase.count('a'))# 2 contagem caracter de a minusculo

print(frase.upper().count('A'))# 2 transforma tudo para maisculo e depois conta os carcteres

print(len(frase))# 25 conta tamanho da string

print(len(frase.strip()))# 21 strip retira espacos antes e depois das strings
#rstrip() remove espaços da apenas da direita
#lstrip() remove apenas espaços a esquerda

print(frase.replace('Wolter', 'Silva'))#  Daniel Silva Martins

frase = frase.replace('Daniel Wolter Martins', 'D4n13l W0lt3r')
dividido = frase.split() #dividide string dentro de lista

print(dividido)#['D4n13l', 'W0lt3r']

minusculo = 'daniel wolter martins'
print(minusculo.capitalize())#primeira letra maiscula
print(minusculo.title())#poe todas letra em maiusciulos depois do espaços

#dividir strings

#variavel.split() dividi string pelos espaços e gera uma lista

#'-'.join(variavel) junta elementos da lista numa string separadas pelo digito indicado -



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

print('pazre em conhecer {: ^20}!'.format(a))#pazre em conhecer @@@daniel wolter@@@@!
print('pazre em  \n conhecer {:@^20}!'.format(a))
#pazre em
# conhecer @@@daniel wolter@@@@!

print('pazre em conhecer {:@^20}!'.format(a), end=(' XXX '))
#pazre em conhecer @@@@@@dani wol@@@@@@! XXX