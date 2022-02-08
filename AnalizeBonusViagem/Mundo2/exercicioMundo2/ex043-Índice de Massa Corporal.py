#desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule sei IMC, e mostre seu status de caordo
#com a tabela

#abaixo de 18.5 abaixo do peso
#entre 18.5 e 25 peso ideal
#25 a 30 sobrepeso
#30 ate 40 obesidade
#acima de 40 obesidade mórbida

altura = float(input('digite sua altura exemplo 1.65!'))
peso = float(input('digite seu peso exemplo 67.5!'))

imc = peso / (altura**2)

if imc < 18.5:
    print('voce esta abaixo dp peso')
elif imc >= 18.5 and imc < 25:
    print('voce esta no peso ideal')
elif imc >= 25 and imc < 30:
    print('voce esta com sobrepeso')
elif imc >= 30 and imc < 40:
    print('obesidade')
elif imc > 40:
    print('Obesidade morbida')