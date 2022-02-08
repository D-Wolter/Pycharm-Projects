dadoss = {}
dados = dict()
dado = {'nome':'Pedro','idade':25}#cria chave pra substituir o index numerico
print(dado['nome'])#exibi pelo dicionario criado
print(dado['idade'])

print(f'O {dado["nome"]} tem {dado["idade"]} anos.')
#O Pedro tem 25 anos.

dado['sexo']='M'#adiciona mais uma chave e valor no dicionario
del dado['idade']#deleta alguma chave valor
filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}
print(filme.values())#exibe os conteudos
print(filme.keys())#exibe os nome chaves do dicionario
print(filme.items())#exibe conteudos e chaves
#dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])
for t, f in filme.items():
    print(f'O {t} é {f}')
#O titulo e Star wars
#O ano é 1977
#o diretor é george lucas

for k in filme.keys():
    print(k)#titulo ano diretor

for k in filme.values():
    print(k)#Star Wars 1977 George Lucas

for k in filme.items():
    print(k)# ('titulo', 'Star Wars') ('ano', 1977) ('diretor', 'George Lucas')
filme['titulo'] = 'Star Wars IV uma nova esperança'
for k, v in filme.items():
    print(f'{k} = {v}')
#titulo = Star Wars IV uma nova esperança
#ano = 1977
#diretor = George Lucas

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('unidade federativa'))
    estado['sigla'] = str(input('sigla do estado'))
    brasil.append(estado.copy())
print(brasil)#[{'uf': 'minas', 'sigla': 'mg'}, {'uf': 'acre', 'sigla': 'ac'}, {'uf': 'santa', 'sigla': 'sc'}]