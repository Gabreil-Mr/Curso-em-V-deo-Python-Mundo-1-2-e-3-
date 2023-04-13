print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 79 '}\033[1;33m{'='*30}\033[m")
lista = []
termos = int(input('Quantos termos quer analisar? '))
cont = 0
# coletando os valores
while cont != termos:
    num = input(f'\033[35m{cont+1})\033[m Digite um número: ')
    if num.isnumeric() == True:
        if num not in lista:
            lista.append(num)
            cont += 1
        else:
            print('\033[1;31mXXX\033[m O número já foi digitado!')
    else:
        print('\033[1;31mXXX\033[m Opção inválida! Tente novamente')
# printando a lista
lista.sort()
print('\033[1;31m->\033[m Lista de valores: \033[34m',end='')
for num in lista:
    print(num, end=' ')
print('')

print(f"\033[1;33m{'=' * 73}\033[m")