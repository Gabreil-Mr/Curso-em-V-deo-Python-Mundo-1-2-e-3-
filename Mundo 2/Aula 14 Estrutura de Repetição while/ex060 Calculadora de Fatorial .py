print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 60 '}\033[1;33m{'='*30}\033[m")
print('\033[35m=~= Calculadora de Fatorial =~=\033[m')
n = int(input('Digite o número: '))
c = n + 1
fat = 1
print(f'\033[1;31m* \033[m{n}! = ',end='')
while c != 1:
    c -= 1
    fat *= c
    if c == 1:
        print(c, end=' = ')
    else:
        print(c, end=' x ',)
print("\033[1;34m{:,}\033[m".format(fat).replace(',','.'))
print(f"\033[1;33m{'=' * 73}\033[m")