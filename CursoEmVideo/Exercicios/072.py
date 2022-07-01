while True:
    numero = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
    num = int(input('Digite o numero para escreve-lo por extenso: '))
    while num <0 or num > 20:
        print('Dado incorreto. Digite um numero entre 0 e 20. Tente Novamente!')
        num = int(input('Digite o numero para escreve-lo por extenso: '))

    print(numero[num])
    parar = input('Você deseja continuar? [S/N] ').upper().strip()
    if parar == 'N':
        break
print('Fim do Programa.')