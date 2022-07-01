numero = int(input('Digite um numero para exibir sua fatorial: '))
resultado = 1
cont = numero

while cont >= 1:
   resultado *= cont
   if cont != 1:
      print(f'{cont} x', end=' ')
   if cont == 1:
      print(cont, end=' ')
   cont -= 1

print('=', resultado)
