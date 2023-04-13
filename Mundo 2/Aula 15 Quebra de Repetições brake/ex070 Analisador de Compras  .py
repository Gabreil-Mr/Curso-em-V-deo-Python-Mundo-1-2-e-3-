print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 70 '}\033[1;33m{'='*30}\033[m")
nome = maisbarato = ''
valor = mais1000 = 0
lista_valores = []
print('                         \033[1mLOJA SUPER BARATÃO\033[m')
while True:
    print('\033[1;36m=-\033[m'*15)
    nome = input('Nome: ')
    valor = input('Valor: \033[1;32mR$\033[m ')
    while valor.isnumeric() == False:
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        valor = input('Digite novamente: \033[1;32mR$\033[m ')
    valor = float(valor)
    lista_valores += [valor]
    print('\033[1;36m=-\033[m'*15)
    if valor == min(lista_valores):
        maisbarato = nome
    if valor > 1000:
        mais1000 += 1

    cont = str(input('Gostaria de continuar? \033[1;35m[s/n]\033[m ')).lower()
    while cont not in 'sn':
        print('\033[1;31mXXX\033[m Digite uma opção válida! ')
        cont = str(input('Gostaria de continuar? \033[1;34m[s/n]\033[m ')).lower()
    if cont == 's':
        print('Okay!')
        n = 1
    elif cont == 'n':
        break
print('\033[1;35m=-\033[m'*20)
print('\033[1;31mRESULTADO FINAL\033[m')
# 1
print(f'\n\033[1;33m->\033[m Valor Total: \033[34m{sum(lista_valores):.2f}\033[m')
# 2
print(f'\033[1;33m->\033[m Produtos R$+1000: \033[34m{mais1000}\033[m')
# 3
print(f'\033[1;33m->\033[m O produto +barato foi: \033[34m{maisbarato}\033[m')
print(f"\033[1;33m{'=' * 73}\033[m")