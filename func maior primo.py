def maior_primo(n):
    c = 2
    d = 0
    mp = 0

    while mp == 0:
        while c <= n:
            if n % c == 0:
                d += 1
            c += 1
        if d == 1:
            mp = n
            break
        d = 0
        c = 2
        n -= 1
    print(mp)

n = int(input('Digite um número inteiro maior ou igual a 2: '))
maior_primo(
