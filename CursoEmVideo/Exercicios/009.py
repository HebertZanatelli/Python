num = input('Digite um numero para ver a tabuada: ')

if num.isnumeric() == True:
    num = int(num)
    print('-' * 12)
    if num > 0:
        for a in range(1,11):
            print(f'{num} * {a:2} = {a*num}')
        print('-' * 12)
else:
    print('Não é um número, digite um número válido')