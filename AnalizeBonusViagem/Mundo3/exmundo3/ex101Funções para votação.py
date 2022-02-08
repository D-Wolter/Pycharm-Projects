
def voto(a):
    from datetime import datetime
    anoAtual = datetime.now().year
    idade = anoAtual - a
    if idade < 18:
        return print(f'Coma {idade} anos: NÃo VOTA.')
    if idade >= 18 and idade < 65:
        return print(f'Coma {idade} anos: O voto é Obrigatorio')
    if idade >= 65:
        return print(f'Com {idade} anos: O voto é Opcional')

ano = int(input('Em que ano voce nasceu? '))
voto(ano)