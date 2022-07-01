import datetime
ano = datetime.date.today().year
cadastro = {'nome': input('Nome: '), 'idade': ano - int(input('Ano de Nascimento: ')),'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if cadastro['ctps'] > 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['contratação'] + 35 - cadastro['idade']
print('=-' * 30)
for k, v in cadastro.items():
    print(f'    - {k} tem o valor {v}')