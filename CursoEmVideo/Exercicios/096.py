def terreno(a, b):
    area = a * b
    print(f'Nosso terreno tem uma área de {area:.2f}m².')

print(' CONTROLE DE TERRENOS')
print('-' * 22)
a = float(input('Largura Terreno (m): '))
b = float(input('Comprimento Terreno (m): '))
terreno(a, b)
