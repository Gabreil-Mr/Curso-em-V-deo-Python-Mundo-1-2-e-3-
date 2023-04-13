print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 82 '}\033[1;33m{'='*30}\033[m")
lista = []
termos = int(input('Quantos termos quer analisar? '))
cont = 0
# coletando os valores
while cont != termos:
    num = input(f'\033[35m{cont+1})\033[m Digite um número: ')
    if num.isnumeric() == True:
        num = int(num)
        lista.append(num)
        cont += 1
    else:
        print('\033[1;31mXXX\033[m Opção inválida! Tente novamente')
print('\033[1m-\033[m'*50)

# lista par
listaimpar = []
listapar = []
for numero in lista:
    # par
    if numero % 2 == 0:
        listapar.append(numero)
    # impar
    elif numero % 2 == 1:
        listaimpar.append(numero)

# ordenando as listas:
lista.sort()
listapar.sort()
listaimpar.sort()

# Resultado final
a = 0
todaslistas = [lista,listapar,listaimpar]
tipo = ['Todos os valores','Valores Par', 'Valores impar']

for listas in todaslistas:
    print(f'\033[1;33m->\033[m {tipo[a]}: \033[34m',end='')
    for numero in listas:
        print(numero,end=' ')
    print('')
    a += 1

print(f"\033[1;33m{'=' * 73}\033[m")