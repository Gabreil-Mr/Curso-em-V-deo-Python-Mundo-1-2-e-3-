print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 87 '}\033[1;33m{'='*30}\033[m")
from random import randint
linha  = []
matriz = []
cont = par = soma = maior = 0
print('\033[1m-\033[m'*10,'Gerador de Matrizes Aleatórias','\033[1m-\033[m'*10)
print('Como vai ser sua matriz?')
h = int(input('h: '))
comp = int(input('comp: '))
rand = int(input('> nº possível: '))
print(f'{comp}x{h}')
print('\033[1m-\033[m'*52)
# preenchendo a matriz
for c in range(0,h):
    for d in range(0,comp):
        a = randint(0,rand)
        linha.append(a)
        if a % 2 == 0:
            par += a
        if c == 2:
            soma += a
        if c == 1:
            if a > maior:
                maior = a
    matriz.append(linha[:])
    linha.clear()
# resultado final
for li in matriz:
    for n in li:
        print(f"[{n:^5}]",end='')
    print('')
    cont += 1
print('\033[1m-\033[m'*52)
# adicional

print(f"\033[35ma)\033[m Soma de todos valores pares: \033[34m{par}\033[m")
print(f"\033[35mb)\033[m Soma de todos valores da 3ª coluna: \033[34m{soma}\033[m")
print(f"\033[35mc)\033[m O maior número da 2ª coluna: \033[34m{maior}\033[m")

print(f"\033[1;33m{'=' * 73}\033[m")
