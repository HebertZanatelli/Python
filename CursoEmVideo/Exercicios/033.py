num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num1 > num2 and num1 > num3:
    print(f'O {num1} é o maior numero')
elif num2 > num1 and num2 > num3:
    print(f'O {num2} é o maior numero')
elif num3 > num1 and num3 > num2:
    print(f'O {num3} é o maior numero')

if num1 < num2 and num1 < num3:
    print(f'O {num1} é o menor numero')
elif num2 < num1 and num2 < num3:
    print(f'O {num2} é o menor numero')
if num3 < num2 and num3 < num1:
    print(f'O {num3} é o menor numero')



