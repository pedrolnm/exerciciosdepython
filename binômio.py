n = int(input('Escreva o valor de n: '))
k = int(input('Escreva o valor de k: '))
def fatorial(x):
    c = 1
    f = 1
    while c <= x:
        f = f * c
        c += 1
    return f

def binomial(x, y):
    b = fatorial(x) // (fatorial(y) * fatorial(x - y))
    return b

print(binomial(n, k))
