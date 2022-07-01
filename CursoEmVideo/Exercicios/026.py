frase = input('Digite uma frase: ').strip().lower()
print(f'a letra "A" aparece: {frase.count("a")}')
print(f'a primeira letra "A" apareceu na posição: {frase.find("a") + 1}')
print(f' a ultima letra "a" é na posição: {frase.rfind("a")+1}')
