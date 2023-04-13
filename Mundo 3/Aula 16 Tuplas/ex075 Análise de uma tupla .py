print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 74 '}\033[1;33m{'='*30}\033[m")
# variáveis de base

pares = ''
lista = []
x = 0
# coletando os numeros

for c in range(0,4):
    while True:
        x += 1
        c = input(f'\033[35m{x})\033[m Digite um número: ')
        if c.isnumeric() == True:
            break
        else:
            print('\033[1;31mXXX\033[m Opção inválida! Tente novamente')
            x -= 1
    lista += c

# convertendo

tupla = tuple(lista)

# Resultados finais:

    # noves
print(f"\033[1;32m->\033[m Quantidade de 9: \033[34m{tupla.count('9')}\033[m")
    # tres
if '3' in tupla:
    print(f"\033[1;32m->\033[m Posição do 3: \033[34m{tupla.index('3')+1}\033[m")
else:
    print('\033[1;32m->\033[m Não foi digitado nenhum 3')
    # pares
print(f"\033[1;32m->\033[m Os números pares são: \033[34m", end='')
for num in tupla:
    if float(num) % 2 == 0 and int(num) != 0:
        print(int(num), end=' ')
print('')
print(f"\033[1;33m{'=' * 73}\033[m")

# solução mais enxuta

    # coletando os valores
n1 = tuple(int(input('Digite um número: ')) for n in range(4))
    # Resultados
        # noves
print(f'O valor 9 aparece {n1.count(9)} vezes')
        # tres
if 3 in n1:
    print(f'O valor 3 apareceu pela primeira vez na posição {n1.index(3)+1}')
        # pares
print('Os valores pares digitados são:',end=' ')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')