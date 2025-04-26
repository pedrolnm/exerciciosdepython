import cmath
a = float(input('Digite o parâmetro a: '))
b = float(input('Digite o parâmetro b: '))
c = float(input('Digite o parâmetro c: '))
delta = ((b ** 2) - 4 * a * c)
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)
if delta < 0:
    print('esta equação não possui raízes reais')
if delta == 0:
    print(f'a raiz desta equação é {x1}')
if delta > 0:
    if x1 < x2:
        print(f'as raízes da equação são {x1} e {x2}')
    else:
        print(f'as raízes da equação são {x2} e {x1}')
