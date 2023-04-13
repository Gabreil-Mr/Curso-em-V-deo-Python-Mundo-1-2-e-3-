from random import randint

linha  = []
matriz = []
cont = 0

print('-'*10,'Gerador de Matrizes Aleatórias','-'*10)

print('Como vai ser sua matriz?')
h = int(input('Altura: '))
comp = int(input('Comprimento: '))
print(f'{comp}x{h}')
print('-'*40)
rand = int(input('Maior número possível: '))
# preenchendo a matriz
for c in range(0,h):
    for d in range(0,comp):
        linha.append(randint(0,rand))
    matriz.append(linha[:])
    linha.clear()
print('-'*40)
# resultado final
for li in matriz:
    for n in li:
        print(f"[{n:^5}]",end='')
    print('')
    cont += 1