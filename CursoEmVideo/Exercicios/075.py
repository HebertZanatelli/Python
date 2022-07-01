tupla = (int(input('Digite um número: ')),
         int(input('Digite outro numero:')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
lista = []
print(f'Você digitou os valores: {tupla}')
print(f'O numero 9 apareceu {tupla.count(9)} vezes')
print(f'O valor {tupla[1]} apareceu na 2ª posição')
for n in tupla:
    if n % 2 == 0:
        lista.append(n)
print(f'Os numeros pares sao {lista}')