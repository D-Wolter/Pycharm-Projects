# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
#APOS A SOPA,
# A SACADA DA CASA,
# A TORRE DA DERROTA,
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

# palavra = 'a sacada da casa'
# palavra = palavra.replace(' ', '')
# invertido = palavra[::-1]
#
# if invertido == palavra:
#     print('a frase é um PALÍNDROMO')
# elif invertido != palavra:
#     print('a frase nao forma um polindromo')


#cod prof
frase =str(input('digite uma frase; ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O imverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palíndromo')
else:
    print('a frase digitada nao é um palíndromo')