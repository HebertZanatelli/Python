import math
ang = float(input('Digite o valor do angulo para descobrir o Seno, Cosseno e Tangente'))

cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tg = math.tan(math.radians(ang))

print(f'O seno do angulo {ang}º é {sen}')
print(f'O Cosseno do angulo {ang}º é {cos}')
print(f'A Tangente do angulo {ang}º é {tg}')
