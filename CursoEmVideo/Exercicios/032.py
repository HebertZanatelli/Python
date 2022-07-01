import datetime
# while True:
ano = int(input('Qual o ano que quer analisar? Coloque 0 para verificar o ano atual '))
if ano == 0:
    ano = datetime.date.today().year

elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')