print(f"\033[1;33m{'='*30}\033[1;34m{' Aprofundando For '}\033[1;33m{'='*30}\033[m")

lanche = ('hambuguer','pizza','refrigerante','pudim')

print('=*'*10,'1º Forma','=*'*10)
for comida in lanche:
    print(comida)

print('=*'*10,'2º Forma','=*'*10)
for c in range(0,len(lanche)):
    print(lanche[c])

print('=*'*10,'3º Forma','=*'*10)
for pos,comida in enumerate(lanche):
    print(comida,pos)

print('=*'*26)

print(f"\033[1;33m{'='*73}\033[m")