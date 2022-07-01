import datetime
nascimento = int(input('Digite o seu ano de nascimento: '))
alistamento = datetime.date.today().year
idade = alistamento - nascimento
falta = 18 - idade

if idade < 18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {alistamento}')
    print(f'Ainda faltam {falta} Anos para o alistamento militar.')
    print(f'Seu Alistamento será em {nascimento + 18}.')
elif idade > 18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {alistamento}')
    print(f'Você já deveria ter se alistado há {idade-18} anos')
    print(f'Seu alistamento foi em {nascimento+18}')
else:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {alistamento}')
    print('Você deve se alistar IMEDIATAMENTE')