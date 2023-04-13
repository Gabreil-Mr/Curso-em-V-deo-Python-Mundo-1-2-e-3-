print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 55 '}\033[1;33m{'='*30}\033[m")

lista = ['0','1','2','3','4']
for c in range(0,4+1):
    peso = int(input(f'\033[1;35m{c+1})\033[m Digite o peso: \033[1;31mKG\033[m '))
    lista[c] = peso
if min(lista) == max(lista):
    print('Todos os pesos são iguais')
else:
    print(f'\n\033[1;31m* \033[mO \033[1mmenor\033[m peso é \033[34m{min(lista):.2f}\033[m Kg')
    print(f'\033[1;31m* \033[mO \033[1mmaior\033[m peso é \033[34m{max(lista):.2f}\033[m Kg')

print(f"\033[1;33m{'=' * 73}\033[m")
# outra forma de resolver esse exercicio
minimo= 1000000
maximo = 0
for c in range(1,5):
    num = int(input('Digite um número'))
    if num < minimo:
        minimo = num
    elif num > maximo:
        maximo = num
if maximo == minimo:
    print('Todos os números são iguais')
else:
    print(f'menor: {minimo}')
    print(f'maior: {maximo}')