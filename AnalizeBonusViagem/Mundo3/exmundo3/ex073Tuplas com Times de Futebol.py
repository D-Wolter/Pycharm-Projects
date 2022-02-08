listaCampeoes = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense','América-MG',
                 'Atlético-GO','Santos','Ceará','Internacional','São Paulo','Athletico-PR','Cuiabá','Juventude','Grêmio'
                 ,'Bahia','Sport','Chapecoense')

for pos,  time in enumerate(listaCampeoes[0:5]):
    print(f'{pos+1} - {time}')
print('-=' * 20)

for pos,  time in enumerate(listaCampeoes[16:]):
    print(f'{pos+17} - {time}')
print('-=' * 20)

print(sorted(listaCampeoes))
print('-=' * 20)

print(listaCampeoes.index('Chapecoense')+1)
#
# times = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense','América-MG',
#                  'Atlético-GO','Santos','Ceará','Internacional','São Paulo','Athletico-PR','Cuiabá','Juventude','Grêmio'
#                  ,'Bahia','Sport','Chapecoense')

