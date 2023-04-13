print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 61 '}\033[1;33m{'='*30}\033[m")
p = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
termos = 10
while termos != 0:
    a = p
    ult = p + (termos * r)
    print(f'\033[1;31m * \033[m {p} \033[1;33m->\033[m ', end='')
    while a != ult:
        a += r
        if a != ult:
            print(a,end=' \033[1;33m->\033[m ')
        else:
            print(f'\033[1;35m{a}\033[m')
    print(f"\033[1;33m{'=' * 73}\033[m")
    cont = 'a'
    while cont not in 'sn':
        cont = str(input('Gostaria de mudar a quantidade de termos? \033[1;34m[s/n]\033[m '))
        if cont == 's':
            termos = int(input('Quantidade de Termos: '))
        elif cont == 'n':
            termos = 0
            print('\033[35m\U0001F625 \033[mEntão quer dizer que você não gosta de mim \033[35m\U0001F625 \033[m')
        else:
            print('Opção não válida, tente novamente')
