nsegundos = int(input("digite o número de segndos "))
horas = nsegundos // 3600
segundos = nsegundos % 3600
minutos = segundos // 60
segrest = segundos % 60

print(f'{horas} horas, {minutos} minutos e {segrest} segundos')
