velocidade = float(input('Digite a velocidade atual do carro: '))

multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Parabens, voce está dentro da velocidade adequada.')
    print('Dirija com Cuidado!')

else:
    print('Você está acima da velocidade permitida')
    print(f'Pague uma multa de R${multa:.2f}!! Dirija com Cuidado!')