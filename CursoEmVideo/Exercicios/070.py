lista = []
cont1000 = soma = menor = cont = 0
nomemenor = ''
while True:
    print('-' *40)
    print('LOJA SUPER BARATÃO'.center(40))
    print('-'*40)
    produto = input('Insira o nome do produto: ').strip().capitalize()
    lista.append(produto)
    preco = float(input('Insira o preço do produto: R$'))
    parar = ' '
    soma += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomemenor = produto
    while parar not in 'SN':
        parar = input('Deseja continuar? [S/N]').strip().upper()[0]
    if preco > 1000:
        cont1000 += 1
    if parar == 'N':
        break
print(' Fim do programa '.center(40, '-').upper())
print(f'O total da compra foi de R${soma:.2f}')
print(f'Os itens comprados foram: {lista}')
print(f'Temos {cont1000} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {nomemenor} que custa {menor}')



