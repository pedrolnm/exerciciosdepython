def remove_repetidos(x):
    x.sort()
    c = 0
    while c < len(x) - 1:
        if x[c] == x[c + 1]:
            del x[c + 1]
        else:
            c += 1
    return x
