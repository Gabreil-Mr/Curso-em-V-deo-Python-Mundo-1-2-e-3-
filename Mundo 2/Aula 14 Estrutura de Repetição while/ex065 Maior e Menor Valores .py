print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 64 '}\033[1;33m{'='*30}\033[m")
print('\033[35m<------> Avaliando vários valores <------>\033[m')
print('Digite -\033[1;36m x\033[m - se quiser encerar')
lista = []
n = 0
quant = 0
cont = 's'
while cont in 'Ss':
    while n != 'x':
        n = str(input('\033[1;31m* \033[m'))
        if n != 'x':
            while n.isnumeric() == False:
                print("\033[1;31mXXX\033[m opção inválida, digite novamente:")
                n = input('\033[1;31m* \033[m')
            n = float(n)
            lista += [n]
            quant += 1
        else:
            print('\033[1;36m=-\033[m'*30)
# média
    media = sum(lista)/quant
    print(f'\033[1;33m->\033[m Média: \033[1;34m{media:.2f}\033[m')
# maior
    print(f'\033[1;33m->\033[m Maior: \033[1;34m{max(lista)}\033[m')
# menor
    print(f'\033[1;33m->\033[m Menor: \033[1;34m{min(lista)}\033[m')

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