print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 61 '}\033[1;33m{'='*30}\033[m")
p = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
termos = int(input('Quantidade de termos: '))
a = p
ult = p+(termos*r)
print(f'\033[1;31m * \033[m {p} \033[1;33m->\033[m ',end='')

while a != ult:
    a += r
    if a != ult:
        print(a,end=' \033[1;33m->\033[m ')
    else:
        print(f'\033[1;35m{a}\033[m')
print(f"\033[1;33m{'=' * 73}\033[m")