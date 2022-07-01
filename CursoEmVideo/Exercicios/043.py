altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso em KG: '))
imc = peso / altura**2

if imc < 18.5:
    print(f'IMC {imc:.2f}, você está ABAIXO DO PESO.')
elif imc < 25:
    print(f'IMC {imc:.2f}, você está no PESO IDEAL')
elif imc < 30:
    print(f'IMC {imc:.2f}, você está com SOBREPESO')
elif imc < 40:
    print(f'IMC {imc:.2f}, Voce está com OBESIDADE')
else:
    print(f'IMC {imc:.2f}, você está com OBESIDADE MORBIDA')


