preco = float(input('Preço das compras: R$ '))

print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')

opcao = input('Selecione a Opção desejada: ')
juros = preco * 1.2

if opcao == '1':
    print(f'Sua compra de R${preco:.2f} tera um desconto devido a opçao de pagamento, preço final é {preco * 0.9:.2f}')
elif opcao == '2':
    print(f'Sua compra de R${preco:.2f} tera um desconto devido a opçao de pagamento, preço final é {preco * 0.95:.2f}')
elif opcao == '3':
    print(f'Sua compra de R${preco:.2f} tera duas prestações de {preco/2:.2f}')
elif opcao == '4':
    numParcelas = int(input('Informe o nº Parcelas (Max 10x): '))
    print(f'Sua compra será parcelada em {numParcelas}x de {juros/numParcelas:.2f} COM 20% DE JUROS. ')
    print(f'Sua compra de R$ {preco:.2f} irá custar R$ {juros:.2f} no final')

else:
    print('Opção inválida!')