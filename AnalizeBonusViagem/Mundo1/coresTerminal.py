#Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus
# programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.
'''
\033[style,text,back]

\033[0:33:44m
'''
#Stylo 0 nenhum    1 bold     4  umnderline      7 negative

#text 30 branco  31vermelho  32verde  33amarelo  34azul   35roxo  36anis   37cinza

#back 40branco   41vermelho  42verde  43amarelo   44azul  45roxo  46anis   47cinza

print('\033[4:31:43mDaniel Wolter')

print('\033[7:31:43mDaniel Wolter\033[m')
print('\033[7:30:43mDaniel Wolter\033[m')

a = 3
b = 5
print('os valores sao \033[7:30:41m{}\033[m e \033[7:30:46m{}\033[m !!!'.format(a, b))
print('os valores sao {}{}{} e {}{}{} !!!'.format('\033[7:30:41m', a, '\033[m','\033[7:30:41m', b, '\033[m',))

nome = 'Daniel wolter Martins'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

print('ola sr {} {} {}!'.format(cores['pretoebranco'], nome, cores['limpa']))