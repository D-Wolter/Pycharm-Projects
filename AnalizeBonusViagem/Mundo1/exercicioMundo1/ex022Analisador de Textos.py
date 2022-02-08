


frase = 'Daniel Wolter silva Martins'

frasemin = frase.lower()
#mostrar todas letras maisculas
print('mostrar todas letras maisculas {}'.format(frase.upper()))
#mostrar todas letra minusculas
print('mostrar todas letra minusculas {}'.format(frase.lower()))
#contar letras sem consideras espaços
dividir = frase.replace(' ', '')
print(len(dividir))
print(len(frase))
#Quantas letras tem o prmeiro nome
minuscula = frase.lower()
sepaRADAS = minuscula.split()#separa string lista
print(sepaRADAS[0])#exibe indice 0
print(len(sepaRADAS[0]))#contar indice 0




#soluçao prof
nome = str(input('Dite seu niome completo')).strip()
print('Analizando seu nome...')
print('seu nome em minusculas é {}'.format(nome.upper()))
print('seu nome em maiusculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('seu nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e le tem {} letras'.format(separa[0], len(separa[0])))


