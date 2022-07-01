# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
#
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(estado1)
# print(estado2)
# print(brasil)

n = int(input())
n = n + 1

while True:
    flag = True
    num = n
    while num > 0:
        d = num / 10
        tmp = n

        while tmp > 0:
            if d == tmp / 10:
                quantidade += 1
            tmp //= 10
        if quantidade > 1:
            flag = False
            break
        num //= 10

    if flag == False:
        print(n)
        break
    n = n + 1