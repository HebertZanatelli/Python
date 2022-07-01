sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe seu sexo: [M/F]').upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Dado incorreto! Informe o seu Sexo corretamente com [M] ou [F]')

print('FIM')