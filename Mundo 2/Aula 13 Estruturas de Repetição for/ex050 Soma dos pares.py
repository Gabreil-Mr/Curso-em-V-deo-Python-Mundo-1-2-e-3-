print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 50 '}\033[1;33m{'='*30}\033[m")
print('Digite 6 números inteiros abaixo para soma')
#soma
p=0
i=0
#coletar os números
for c in range(1,7):
    n = input(f'\033[1;31m * \033[m{c}º número: ')
    isn = n.isnumeric()
    if isn == True:
        n=int(n)
        if n % 2 == 0:
            p += n
        elif n % 2 !=0:
            i += n
    else:
        print(f'\033[1;34m {n}\033[m não é um \033[4mnúmero inteiro\033[m')

print(f'A soma dos \033[1;34mpares\033[m é {p}')
print(f'A soma dos \033[1;34mímpares\033[m é {i}')

print(f"\033[1;33m{'=' * 73}\033[m")
