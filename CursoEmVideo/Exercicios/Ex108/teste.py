import moeda
import time

r = float(input('Digite o Preço: R$ '))
print(f'A metade de {r} é R$ {moeda.metade(r):.2f}')
time.sleep(1)
print(f'O dobro de {r} é R$ {moeda.dobro(r):.2f}')
time.sleep(1)
taxa = float(input('Informe o % da taxa desejada: '))
print(f'O preço aumentado em {taxa}% é R$ {moeda.aumentar(r,taxa):.2f}')
time.sleep(1)
print(f'O preço diminuído em {taxa}% é R$ {moeda.diminuir(r, taxa):.2f}')