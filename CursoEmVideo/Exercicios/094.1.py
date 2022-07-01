pessoa = dict()
cadastros = list()
somid = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').title()
    while True:
        pessoa['sexo'] = input('Sexo: [M/F]').upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite uma opção válida!')
    pessoa['idade'] = int(input('Idade: '))
    somid += pessoa['idade']
    while True:
        parar = input('Deseja continuar? [S/N]').upper().strip()[0]
        if parar in 'SN':
            break
        print('ERRO! Digite uma opção válida!')
    cadastros.append(pessoa.copy())
    if parar == 'N':
        break
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')
print(f'B) A média da idade das pessoas cadastradas é {somid/len(cadastros):5.2f} anos ')
print('C) As mulheres cadastradas são: ', end='')
for c in cadastros:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print(f'\nD) Lista de pessoas com idade acima da média: ')
for c in cadastros:
    if c['idade'] >= somid/len(cadastros):
        for k, v in c.items():
            print(f' {k}  =  {v}', end='; ')
print(f'\nEncerrando!')
