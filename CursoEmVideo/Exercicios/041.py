import datetime
ano = int(input('Insira o seu ano de nascimento: '))
atual = datetime.date.today().year
classificacao = atual - ano

print(f'O atleta tem {classificacao} anos.')

if classificacao <=9:
    print('Classificação: MIRIM')
elif 9 < classificacao <= 14:
    print('Classificação: INFANTIL')
elif 14 < classificacao <= 19:
    print('Classificação: JUNIOR')
elif 19 < classificacao <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')