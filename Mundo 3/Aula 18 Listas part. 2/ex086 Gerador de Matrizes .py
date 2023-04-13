print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 86 '}\033[1;33m{'='*30}\033[m")
# Minha Solução
linha  = []
matriz = []
cont = 0

print('-'*10,'Gerador de Matrizes','-'*10)
print('Como vai ser sua matriz?')
h = int(input('Altura: '))
comp = int(input('Comprimento: '))
print(f'{comp}x{h}')
print('-'*40)
# preenchendo a matriz
for c in range(0,h):
    for d in range(0,comp):
        linha.append(int(input(f"{c+1}x{d+1}) ")))
    matriz.append(linha[:])
    linha.clear()
print('-'*40)
# resultado final
for li in matriz:
    for n in li:
        print(f"[{n:^5}]",end='')
    print('')
    cont += 1

print(f"\033[1;33m{'=' * 73}\033[m")
# Solução + enxuta

matriz = [[],[],[]]
for l in range(0,3):
        for c in range(0,3):
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*30)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()