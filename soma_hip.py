def é_hipotenusa(n):
    éHip = False
    i = j = 1
    while i < n:
        j = 1
        while j < n:
            éHip = n == ((i ** 2) + (j ** 2)) ** 0.5
            if éHip:
                return True
            j += 1
        i += 1
    return False

def soma_hipotenusas(n):
    c = 1
    somaHip = 0
    while n >= c:
            if é_hipotenusa(c):
                somaHip += c
            c += 1
    return somaHip
