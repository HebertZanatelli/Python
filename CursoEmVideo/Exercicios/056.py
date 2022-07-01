medId = 0
mulher20 = 0
maior = 0
nome1 = ''
for c in range(1,5):
    print(f'----- {c}ª PESSOA -----')
    nome = input('Nome:').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    medId += idade
    if sexo == 'M' and idade > maior:
        maior = idade
        nome1 = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1

print(f'A média de idade do grupo é de {medId/4} anos;')
print(f'O homem mais velho tem {maior} e se chama {nome1}.')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos. ')
