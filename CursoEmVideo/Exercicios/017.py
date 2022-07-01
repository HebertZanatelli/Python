# co = float(input('Digite o comprimento do Cateto Oposto: '))
# ca = float(input('Digite o comprimento do Cateto Adjacente: '))
#
# hip = (co**2 + ca**2)**0.5
#
# print(f'O valor da hipotenusa é: {hip:.2f}')

import math
co = float(input('Digite o CO: '))
ca = float(input('Digite o CA: '))

hip = math.hypot(co,ca)

print(f'{hip:.2f}')