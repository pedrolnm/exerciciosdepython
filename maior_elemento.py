def maior_elemento(x):
   maior = x[0]
   c = 1
   while c < len(x):
        if x[c] > maior:
            maior = x[c]
        c += 1
   return maior
