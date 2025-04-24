n = int(input('Digite um número natural '))
c = 1
d = 0
while c <= n // 2: 
    if n % c == 0:
        d += 1
    c += 1
if d == 1:
    print('primo')
else:
    print('não primo')
