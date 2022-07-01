cont = 0
num = int(input('Digite um numero: '))
for c in range(1,num+1):
    if num % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('')
print(f'\033[m0 O numero {num} foi divisivel {cont} vezes')
if cont == 2:
    print('É Numero PRIMO')
else:
    print('Não é Numero PRIMO')
