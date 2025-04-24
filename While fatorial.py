def fatorial(n):
    f = 1
    while 1 < n:
        f = f * n
        n -= 1
    return f

n = int(input('Digite um número natural, ou digite um número negativo para sair: '))

while n >= 0:  
    print(fatorial(n))
    n = int(input('Digite um número natural, ou digite um número negativo para sair: '))

