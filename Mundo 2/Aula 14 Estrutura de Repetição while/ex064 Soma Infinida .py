print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 64 '}\033[1;33m{'='*30}\033[m")
print(f"\033[1;36m{'=~'*8} Soma infinida \033[1;36m{'=~'*8}\033[m")
print('Digite 999 para parar')
n = 0
soma = 0
vezes = 0
while n != 999:
    n = float(input('\033[1;31m* \033[m'))
    if n == 999:
        print('\033[35m\U0001F625 \033[mPor que você parou? \033[35m\U0001F625 \033[m')
    else:
        soma += n
        vezes += 1
if soma > 0:
    print(f'\033[1;33m->\033[m Quantidade de números digitados: \033[34m{vezes}\n\033[1;33m->\033[m Soma total: \033[34m{soma}\033[m')
print(f"\033[1;33m{'=' * 73}\033[m")