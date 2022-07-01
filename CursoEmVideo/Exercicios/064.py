c = 0
# num = 0
soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    c += 1
    soma += num
    num = int(input('Digite um numero [999 para parar]: '))
    # if num == 999:
    #     soma = soma - 999
print(f'Você digitou {c} numeros e a soma entre eles foi {soma}')