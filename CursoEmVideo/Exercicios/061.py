print('''Gerador de PA''')
print('=-=' * 5)
termo = int(input('Digite o Primeiro Termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
c = 0
while c < 10:
    print(f'{termo} >',end=' ')
    termo += razao
    c += 1
print('FIM', end='')

