lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
       'estudar', 'praticar','trabalhar','mercado','programador', 'futuro')
vogais = 'AaeEiIoOuU'
for c in lista:
    print(f'\nNa palavra {c.upper()} temos as vogais:', end=' ')
    for letra in c:
        if letra in vogais:
            print(letra, end=' ')

