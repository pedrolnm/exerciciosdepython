n = int(input('Digite um número '))
numAd = False
while n:
    n2 = n % 10
    n3 = (n // 10) % 10
    if n2 == n3:
        numAd = True
        break
    n = n // 10

if numAd:
    print('sim')
else:
    print('não')
