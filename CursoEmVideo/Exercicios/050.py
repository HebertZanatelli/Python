soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Insira o {c} numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} NUMEROS PARES, a soma deles é {soma}')

