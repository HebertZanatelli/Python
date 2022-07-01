r1 = float(input('Digite o Primeiro segmento: '))
r2 = float(input('Digite o Segundo segmento: '))
r3 = float(input('Digite o Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Triangulo Equilatero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')
else:
    print('Não é possivel fazer um triangulo.')