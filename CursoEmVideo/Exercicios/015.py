dias = int(input('Por quantos dias você alugou o carro?'))
km = float(input('Quantos KM vc rodou com o carro?'))

dias = dias * 60
km = km * 0.15

total = dias+km

print(f'Você deve pagar um total de R${total:.2f}, R${dias:.2f} referente aos dias e R${km:.2f} pela quilometragem rodada')