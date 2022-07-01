larg = float(input('Digite a Largua da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = larg * alt
tinta = area /2

print(f'Sua parede tem uma dimensão de {larg}m X {alt}m e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')