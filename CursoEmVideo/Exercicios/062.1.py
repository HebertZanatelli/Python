print('''Gerador de PA''')
print('=-=' * 5)
primeiro = int(input('Digite o Primeiro Termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
cont = 1
termo = primeiro
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end=' ')
        termo += razao
        cont = cont +1
    print('PAUSE')
    mais = int(input('Quantos termos voce deseja mostrar a mais?'))
print(f'''Voce encerrou o programa.
Você mostrou {total} termos''')

