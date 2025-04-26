def soma_elementos(x):
    soma = 0
    c = 0
    while c <= len(x) - 1:
        soma += x[c]
        c += 1
    return soma
