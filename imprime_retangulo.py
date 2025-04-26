largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
contAlt = 0
contLar = 0
while contAlt < altura:
    while contLar < largura:
        print('#', end=(''))
        contLar += 1
    print()
    contLar = 0
    contAlt += 1
