print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 78 '}\033[1;33m{'='*30}\033[m")
termos = int(input('Quantos termos quer analisar? '))
lista = []
for c in range(0,termos):
    valores = int(input(f'\033[35m{c+1})\033[m Digite um número: '))
    lista.append(valores)

print('\033[1;33m->\033[m Lista de valores: ',end='')
for num in lista:
    print(f'\033[33m{num}',end=' ')

print('')
print(f'\033[1;33m->\033[m Maior valor: \033[34m{max(lista)}\033[m ---- Posição: \033[32m{lista.index(max(lista))+1}º\033[m')
print(f'\033[1;33m->\033[m Menor valor: \033[34m{min(lista)}\033[m ---- Posição: \033[32m{lista.index(min(lista))+1}º\033[m')

print(f"\033[1;33m{'=' * 73}\033[m")