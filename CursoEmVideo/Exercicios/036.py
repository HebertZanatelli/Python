valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o Salario do comprador: '))
tempo = float(input('Digite em quantos anos será o financiamento: '))
tempo = tempo * 12
entrada = float(input('Digite o valor de entrada: '))

final = valorCasa - entrada

prestacao = final / tempo

if prestacao <= salario*0.3:
    print(f'Emprestimo concedido.')
else:
    print('Renda incompativel')