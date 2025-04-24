import math
a = float(input('Digite o parâmetro a: '))
b = float(input('Digite o parâmetro b: '))
c = float(input('Digite o parâmetro c: '))
delta = ((b ** 2) - 4 * a * c)
if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    x1 = -b / (2 * a)
    print(f'a raiz desta equação é {x1:.1f}')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(f'as raízes da equação são {x1:.1f} e {x2:.1f}')
    
