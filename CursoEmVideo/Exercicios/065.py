opcao = 'S'
cont = soma = 0
lista = []

while opcao == 'S':
    num = int(input('Digite um numero:'))
    opcao = input('Deseja continuar? [S/N]').strip().upper()
    lista.append(num)
    soma += num
    cont += 1
    lista.sort()
print(f'Você digitou {cont} números e a média foi {(soma/cont):.2f}')
print(f'O maior valor foi {lista[-1]} e o menor valor foi {lista[0]}.')
print('Fim do Programa')