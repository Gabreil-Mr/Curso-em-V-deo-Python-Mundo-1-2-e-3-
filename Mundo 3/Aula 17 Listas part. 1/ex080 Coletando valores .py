print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 79 '}\033[1;33m{'='*30}\033[m")
lista = []
termos = int(input('Quantos termos quer analisar? '))
cont = pos = 0

# coletando os valores
while cont != termos:
    pos = 0
    num = int(input(f'\033[35m{cont + 1})\033[m Digite um número: '))
    for n in lista:
        if n <= num:
            pos += 1
    lista.insert(pos, num)
    print(f'O valor foi adicionado na posição {pos}')
    cont += 1

# printando a lista
print('\033[1;31m->\033[m Lista de valores: \033[34m',end='')
for num in lista:
    print(num, end=' ')
print('')

print(f"\033[1;33m{'=' * 73}\033[m")