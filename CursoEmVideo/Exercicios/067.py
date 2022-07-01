while True:
    print('---'*12)
    num = int(input('QUER VER A TABUADA DE QUAL NUMERO? '))
    print('---'*12)
    if num < 0:
        break

    for c in range(1,11):
        print(f'{num} x {c:2} = {num * c}')

print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')