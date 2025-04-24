x1 = float(input('Digite a cordenada x do primeiro ponto: '))
y1 = float(input('Digite a cordenada y do primeiro ponto: '))
x2 = float(input('Digite a cordenada x do segundo ponto: '))
y2 = float(input('Digite a cordenada y do segundo ponto: '))
d = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
if d >= 10:
    print('longe')
else:
    print('perto')
