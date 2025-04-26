n = int(input('Digite um número inteiro '))
s = 0
while n:
    n1 = n % 10
    s += n1
    n = n // 10

print(s)
