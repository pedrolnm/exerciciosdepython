largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
contAlt = 0
contLar = 0
while contAlt < altura:
    while contLar < largura:
        if contLar > 0 and contLar < largura - 1 and contAlt > 0 and contAlt < altura - 1:
            print(' ', end= (''))
        else:
            print('#', end=(''))
        contLar += 1
    print()
    contLar = 0
    contAlt += 1
