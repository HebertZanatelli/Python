soma = 0
c = 0
while True:
    num = int(input('Digite um numero para somar [999 para parar]: '))
    if num == 999:
        break
    soma += num
    c += 1

print(f'A soma dos {c} valores é: {soma}')