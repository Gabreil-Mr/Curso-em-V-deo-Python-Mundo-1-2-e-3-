print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 85 '}\033[1;33m{'='*30}\033[m")
num = ''
lista = [[],[]]
# quantidade de termos com erro
while True:
    termos = input('Quantidade de números: ')
    if termos.isnumeric() == True:
        termos = int(termos)
        break
    else:
        print('\033[1;31mXXX\033[m Digite uma opção válida!')
# coletar os valores
for c in range(0,termos):
    while True:
        num = input(f'\033[1;31m*\033[35m {c+1})\033[m ')
        if num.isnumeric() == True:
            num = int(num)
            break
        else:
            print('\033[1;31mXXX\033[m Digite uma opção válida!')

    # se for par
    if num % 2 == 0:
        lista[0].append(num)
    # se for impar
    else:
        lista[1].append(num)
# ordenar as duas
lista[1].sort()
lista[0].sort()
# resultados finais
print('\033[1m-\033[m'*60)
    # par
print('\033[1;33m->\033[m Números pares: \033[34m',end='')
for n in lista[0]:
    print(n,end=' ')
print('')
    # impar
print('\033[1;33m->\033[m Números impares: \033[34m',end='')
for n in lista[1]:
    print(n,end=' ')
print('')
print(f"\033[1;33m{'=' * 73}\033[m")