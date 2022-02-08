
distancia = int(input('quantos kilometos a distancia'))

if distancia <= 200:
    tarifa = distancia * 0.50
    print('voce ira pagar 0,50 por km o valor de {:.2f} reais'.format(tarifa))
else:
    tarifa2 = distancia * 0.45
    print('voce ira pagar 0,45 por km o valor de {:.2f} reais'.format(tarifa2))


#cod prof
kilometragem = float(input('qual kilometragem da viagem'))
print('voce esta prestes a comecar uma viagem de {} km'.format(kilometragem))
preco = kilometragem * 0.50 if kilometragem <= 200 else kilometragem* 0.45
print('o preco de sua passagem sera de r$ {:.2f}'.format(preco))