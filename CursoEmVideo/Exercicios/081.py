lista = []
while True:
    num = int(input('Digite um valor:'))
    lista.append(num)
    opcao = input('Deseja Continuar? [S/N]').strip().upper()
    while opcao != 'N' and opcao != 'S':
        print('Voce digitou uma opção invalida, tente novamente:', end='')
        opcao = input('[S/N]').strip().upper()
    if opcao == 'N':
        break

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescete são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado dentro da lista')