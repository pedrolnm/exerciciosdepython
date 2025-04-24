n = int(input('Digite o número a ser somado: '))
soma = 0
while n:
    soma += n % 10
    n = n // 10

print(soma)
