dist = float(input('Digite uma distância em metros: '))

print(f'A medida de {dist:.1f} corresponde a: ')
print(f'{dist/1000:.3f}Km')
print(f'{dist/100:.2f}Hm')
print(f'{dist/10:.1f}Dam')
print(f'{dist*10}Dm')
print(f'{dist*100}cm')
print(f'{dist*1000}mm')