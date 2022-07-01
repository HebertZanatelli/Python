cidade = input('Digite o nome da cidade: ').strip()

santo = cidade.lower()

if (santo[0:5]) == 'santo':
    print('Verdadeiro')

else:
    print('Falso')