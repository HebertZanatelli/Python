resto50 = resto10 = resto20 = resto1 = nota1 = nota10 = nota20 = nota50 = 0

print('==='*10)
print('banco brasil'.upper().center(30))
print('==='*10)

saque = int(input('Digite o valor para sacar: '))
if saque >= 50:
    nota50 = saque//50
    resto50 = saque - (50 * nota50)
    nota20 = resto50//20
    resto20 = resto50 - (20*nota20)
    nota10 = resto20 // 10
    resto10 = resto20 - (10*nota10)
    nota1 = resto10
if  saque >=20 and saque < 50:
    nota20 = saque//20
    resto20 = saque - (20 * nota20)
    nota10 = resto20 // 10
    resto10 = resto20 - (10 * nota10)
    nota1 = resto10
if saque >= 10 and saque < 20:
    nota10 = saque//10
    resto10 = saque - (10 * nota10)
    nota1 = resto10

if nota50 > 0:
    print(f'Total de {nota50} cédulas de R$50,00')
if nota20 > 0:
    print(f'Total de {nota20} cédulas de R$20,00')
if nota10 > 0:
    print(f'Total de {nota10} cédulas de R$10,00')
if nota1 > 0:
    print(f'Total de {nota1} cédulas de R$1,00')

