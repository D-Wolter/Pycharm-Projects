
#Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else
#em programas Python.

#if
#elif
#elif
#elif
#elif   pode usar quanntos elif quiser
#else:


nome = str(input('digite seu nome!')).lower().strip()
if nome == 'gustavo':
    print('nome bonito')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome e popular')
elif nome in 'ana claudia jessica juliana':
    print('belo nome feminino')
else:#caso nome nao estaja listado mosta aqui
    print('seu nome nao conhecia')
print('tenha um bom dia {}'.format(nome))