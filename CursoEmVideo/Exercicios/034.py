salario = float(input('Digite o seu salário: '))

if salario > 1250:
    print(f'o seu salário será {salario * 1.1}')
else:
    print(f'O seu salario será {salario * 1.15}')