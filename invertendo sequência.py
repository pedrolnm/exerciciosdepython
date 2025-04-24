n = int(input('Digite um número: '))
c = 1
seq = []

while n:
    seq.append(n)
    n = int(input('Digite um número: '))

for num in reversed(seq):
    print(num)
