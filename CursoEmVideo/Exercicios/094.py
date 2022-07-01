cadastro = {}
cadfinal = []
mulheres = []
media = 0
while True:
    cadastro.clear()
    cadastro['nome'] = input('Nome: ')
    while True:
        cadastro['sexo'] = input('Sexo: [M/F]').strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'])
    cadastro['idade'] = int(input('Idade: '))
    cadfinal.append(cadastro.copy())
    media += cadastro['idade']
    while True:
        parar = input('Deseja continuar? [S/N]').strip().upper()[0]
        if parar in 'SN':
            break
        print('ERRO! Digite apenas M ou F.')
    if parar == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(cadfinal)} pessoas cadastradas.')
print(f'B) a média de idade das pessoas é {media/len(cadfinal):5.2f} anos.')
print(f'C) As Mulheres cadastradas foram', end=' ')
for c in mulheres:
    print(c, end=' ')
print(f'\nD) A lista das pessoas que estão acima da média:')
for c in range(len(cadfinal)):
    if cadfinal[c]["idade"] >= media/len(cadfinal):
        print(cadfinal[c]["Nome"])
