
'''
#ano1 = 365.2421

ano = int(input('digite seu ano de nascimento'))
if ano % 4 == 0 or ano % 400 == 0:
    print('a ano de {} e bissexto'.format(ano))
else:
    print('nao e bissexto')
1201



import datetime

anoAtual = datetime.datetime.now()
data = anoAtual.date()
ano = data.strftime("%Y")
print(ano)

'''
from datetime import date

ano = int(input('digite o ano'))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é Bissexto'.format(ano))
else:
    print('O ano de {} não é Bissexto'.format(ano))