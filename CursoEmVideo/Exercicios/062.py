print('''Gerador de PA''')
print('=-=' * 5)
termo = int(input('Digite o Primeiro Termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
c = 0
contTermo = 0
while c < 10:
    print(f'{termo} >', end=' ')
    termo += razao
    c += 1
    contTermo += 1
print('PAUSA', end='')
print('')

if c == 10:
    while c == 10:
        temp = int(input('Deseja mostrar mais ?'))
        n = 0
        if temp != 0:
            while n < temp:
                print(f'{termo} >', end=' ')
                termo += razao
                n += 1
                contTermo += 1
            print('PAUSA ')
        else:
            c += 1
            print("Voce Desejou sair.")
print(f'Progressão finalizada com {contTermo} termos mostrados')
print('Fim do Programa.')
