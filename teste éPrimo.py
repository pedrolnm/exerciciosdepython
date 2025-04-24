
def maior_primo(n):
    def éPrimo(n):
        c = 2
        d = 0
        while c <= n:
            if n % c == 0:
                d += 1
            c += 1
        if d == 1:
            return True
        else:
            return False

    while not éPrimo(n):
        n -= 1

    return print(n)
