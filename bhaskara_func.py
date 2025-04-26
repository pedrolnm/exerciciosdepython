import math
def delta(a, b, c):
    d = ((b ** 2) - 4 * a * c)
    return d
def raiz_unica(a, b):
    r = -b / (2 * a)
    return r
def raiz_dupla(a, b, delta):
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    if r1 > r2:
        r1, r2 = r2, r1
    return r1, r2

a = float(input('Digite o parâmetro a: '))
b = float(input('Digite o parâmetro b: '))
c = float(input('Digite o parâmetro c: '))
d = delta(a, b, c)
if d < 0:
    print('esta equação não possui raízes reais')
elif d == 0:
    print(f'a raiz desta equação é {raiz_unica(a, b):.1f}')
else:
    r1, r2 = raiz_dupla(a, b, delta)
    print(f'as raízes da equação são {r1:.1f} e {r2:.1f}')
    
