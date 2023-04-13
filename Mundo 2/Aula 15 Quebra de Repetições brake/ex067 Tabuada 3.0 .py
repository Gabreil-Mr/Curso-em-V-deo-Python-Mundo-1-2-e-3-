print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 67 '}\033[1;33m{'='*30}\033[m")

#coletar a váriavel
print('\033[1;31mTABUADA 3.0\033[m')
while True:
    n = input('Digite um número inteiro: ')
# reiniciar o programa se o número digitado não for int
    while n.isnumeric() == False:
        print('\033[1;31mXXX\033[m Opção não válida!')
        n = input('Digite novamente: ')

    n= int(n)

#fazer a estrutura da tabuada
    print('\033[1;35m=-=-\033[m'*6)
    for c in range(1,11):
        print("\033[31m    {}\033[33m * \033[31m{}\033[m = \033[34m{:0>2}\033[m".format(c,n,c*n))
    print('\033[1;35m=-=-\033[m'*6)

    print(f"\033[1;33m{'=' * 73}\033[m")
    cont = str(input('Gostaria de continuar? \033[1;34m[s/n]\033[m ')).lower()
    while cont not in 'sn':
        print('\033[1;31mXXX\033[m Digite uma opção válida! ')
        cont = str(input('Gostaria de continuar? \033[1;34m[s/n]\033[m ')).lower()
    if cont == 's':
        print('Okay!')
        n = 1
    elif cont == 'n':
        print(f'\033[35m\U0001F625 \033[m Então você não gosta de mim \033[35m\U0001F625 \033[m')
        break