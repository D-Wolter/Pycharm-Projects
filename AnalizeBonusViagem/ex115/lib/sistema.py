from ex115.lib.interface import *
from time import sleep

while True:
        resposta = menu(['Criar Arquivo', 'CAdastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
        if resposta == 1:
            cabeçalho('Opção 1')
        elif resposta == 2:
            cabeçalho('Opçaõ 2')
        elif resposta == 3:
            cabeçalho('Saindo do Sistema')
            break
        else:
            print('\033[31mERRO! Digite uma opcao valida!\033[m')
        sleep(2)