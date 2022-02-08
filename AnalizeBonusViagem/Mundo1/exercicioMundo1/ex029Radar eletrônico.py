
import random
velocidade = random.randint(0,120)
print('voce foi multado a velocidade de {}km por horA'.format(velocidade) if velocidade >= 80 else 'voce nao recebeu nenhuma multa')


velocidade2 = random.randint(0,120)

if velocidade2 > 80:
    multa = velocidade2 - 80
    multa = multa * 7
    print('voce foi multado a {} km por hora'.format(velocidade2))
    print('a multa vai custar {} reais'.format(multa))
else:
    print('bom motorista')




velocidade3 = float(input('qual é a velociade atual do carro'))
if velocidade3 > 80:
    print('multado! Voce exedeu o limite de velocidade que é de 80km/h')
    multa2 = (velocidade3-80) * 7
    print('voce deve pagar uma multa de r${:.2f}!'.format(multa2))
print('tenha um bom dia! Dirija com segurança!')