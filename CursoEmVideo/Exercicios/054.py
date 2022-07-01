import datetime
dataAtual = datetime.date.today().year
menor = 0
maior = 0
for c in range(1,8):
    num = int(input(f'Digite o ano de nascimento da {c}ª pessoa:'))
    if dataAtual - num > 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')



