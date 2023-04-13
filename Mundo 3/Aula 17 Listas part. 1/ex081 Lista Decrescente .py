print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 81 '}\033[1;33m{'='*30}\033[m")

lista = []
cont = quant = pos = 0

print('Digite ( \033[31mx\033[m ) para encerrar o contador')
while True:
    num = input(f'\033[35m{cont+1}) \033[mDigite um número: ')
    if num == 'x':
        break
    if num.isnumeric()==True:
        num = int(num)
        lista.append(num)
        cont += 1
    else:
        print('\033[1;31mXXX\033[m Opção inválida! Tente novamente')
print('\033[1m-'*40)
lista.sort(reverse=True)
print(f'\033[1;33m->\033[m Quantidade de números digitados: \033[34m{cont}\033[m')
print('\033[1;33m->\033[m Lista Decrescente: \033[34m',end='')
for n in lista:
    print(n,end=' ')
print('')
print('\033[1;33m->\033[m Se o valor 5 foi digitado: ',end='')
if 5 in lista:
    print(f'É o \033[34m{lista.index(5)}º\033[m valor da lista')
else:
    print('\033[34mNão')

print(f"\033[1;33m{'=' * 73}\033[m")