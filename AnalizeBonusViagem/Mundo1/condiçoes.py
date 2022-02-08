

tempo = int(input('quantos anos tem seu carro'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
    print(' fim')

#forma resumida
print('carro novo' if tempo<=3 else 'carro velho')

#######################################################

nome = str(input('Digite seu nome')).upper().strip()
if nome == 'DANIEL':
    print('que lindo nome voce tem')
else:
    print('seu nome é tao normal')
print('Bom dia {}'.format(nome))

#################################5

n1 = float(input('digite a primeira nota'))
n2 = float(input('dogite a segunda nota'))
m = (n1 + n2)/2
print('a sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua media foi boa parabens')
else:
    print('sua media foi ruim')
#resumido
print('o cara é bom mesmo' if m >= 6.0 else 'otario')












