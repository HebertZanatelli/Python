maior = homem = mulher = 0
while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    sexo = ' '
    parar = ' '
    idade = int(input('Digite a Idade: '))
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper().strip()[0]
    print('-' * 25)
    while parar not in 'SN':
        parar = input('Deseja Continuar? [S/N] ').upper().strip()[0]

    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if parar == 'N':
        break
print('=-'*23)
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulher(es) com menos de 20 anos.')
print('=-'*23)
print('Fim do Programa, Obrigado.')