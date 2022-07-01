numero = int(input('Digite um numero para criar sua Fatorial n! '))
fatorial = 1
contador = numero
print(f'Fatorial de {numero}! é: ', end= '')
while contador > 0:
    print(numero, end=' ')
    numero = numero -1
    if numero >= 1:
        print('x ', end='')
    else:
        print('= ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)

num2 = int(input('Digite outro numero para criar sua fatorial n!: '))
c = num2
fat = 1
print(f'Fatorial de {num2}! é: ')
for c in range(c,0,-1):
    print(c,end=' ')
    num2 = num2 -1
    if num2 >= 1:
        print('x ',end='')
    else:
        print('= ', end='')
    fat = fat * c
print(fat)