dist = float(input('Digite a distancia em KM: '))

if dist > 0 and dist <= 200:
    print(f'O preço da viagem é: {dist * 0.5:.2f}')

else:
    print(f'o preço da viagem é: {dist * 0.45:.2f}')