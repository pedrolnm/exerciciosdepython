def éPrimo(n):
    nPrimo = 0
    c = 1
    d = 0
    while c <= n // 2: 
        if n % c == 0:
            d += 1
        c += 1
    if d == 1:
        nPrimo = True
        return nPrimo

def n_primos(n):
    numPrimos = 0
    while n > 1:
        if éPrimo(n):
            numPrimos += 1
        n -= 1
    return numPrimos



