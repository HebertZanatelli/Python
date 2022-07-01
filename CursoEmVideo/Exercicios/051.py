termo = int(input('Digite o PRIMEIRO TERMO da nossa PA: '))
razao = int(input('Digite a RAZAO da nossa PA: '))
decimo = termo + (11-1) * razao
for c in range(termo,decimo, razao):
    print(c, end=' ')
print('ACABOU')