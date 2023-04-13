print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 77 '}\033[1;33m{'='*30}\033[m")
lista = []
x = 0
while True:
    termos = input("Quantidade de palavras: ")
    if termos.isnumeric() == True:
        break
    else:
        print('\033[1;31mXXX\033[m Opção inválida! Tente novamente')
termos = int(termos)
# 3 formas de coletar a tupla:
    # 1)
#    while True:
#        x += 1
#        c = input(f'\033[35m{x})\033[m Digite uma palavra: ')
#        if c.isalpha() == True:
#            break
#        else:
#            input(f'\033[35m{c+1})\033[m Digite um número: ')
#            x -= 1
#    lista += c
#conjunto = (lista)
    # 2)
conjunto = tuple(input(f'\033[35m{c+1})\033[m Digite uma palavra: ').lower() for c in range(0,termos))
    # 3)
#conjunto = ('a','vida','e','curta','demais','para','empecilhos','onomatopeiaquadrada')

todasvogais = ('a','e','i','o','u')
apoio = -1
print('\033[1;31m * \033[mLista de Palavras: ')
for c in conjunto:
    apoio += 1
    if apoio == len(conjunto) - 1:
        print(c)
    else:
        print(c, end=' - ')
print('\033[1;32m=-\033[m'*26)
print('\033[1;31m * \033[mVogais de cada palavra:')
print('\033[1;32m=-\033[m'*26)
for palavra in conjunto:
    print( f'\033[35m{palavra}\033[m','-'*(24-len(palavra)),' possui as vogais: ', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'\033[34m{letra}\033[m', end=' ')
    print('')

print('\033[1;32m=-\033[m'*26)

print(f"\033[1;33m{'=' * 73}\033[m")