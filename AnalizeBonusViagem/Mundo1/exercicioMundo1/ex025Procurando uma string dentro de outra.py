#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.


if sepaRADAS.count('martins') == 1:
    print('ela tem wolter no nome')
else:
    print('nao tem silva no nome')

print('primeiro {}'.format(sepaRADAS[0]))

tamanho = len(sepaRADAS)
tamanho = int(tamanho)
#print('ultima {}'.format(sepaRADAS[tamanho]))

#solucao professor
name = str(input('digite seu nome completo')).strip()
print('seu nome tem silva {}'.format( 'silva' in name.lower()))
