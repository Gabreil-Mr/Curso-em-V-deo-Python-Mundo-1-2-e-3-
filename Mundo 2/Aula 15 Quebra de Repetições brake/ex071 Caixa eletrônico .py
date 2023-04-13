# minha solução

print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 71 '}\033[1;33m{'='*30}\033[m")
nota50 = nota20 = nota10 = nota5 = nota1 = 0
print('Qual o valor do saque?')
valor = input('\033[1;31m * \033[m\033[32mR$: \033[m')
while valor.isnumeric() == False:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m')
    valor = input('Digite novamente \033[1;32mR$:\033[m')
valor = int(valor)

print('\033[1;36m=-\033[m'*15)
resto = valor

while resto >= 50:
    resto -= 50
    nota50 += 1
if nota50 > 0:
    print(f'\033[1;33m->\033[m São {nota50} cédulas de  \033[1;32mR$:\033[m50,00')
while resto >= 20:
    resto -= 20
    nota20 += 1
if nota20 > 0:
    print(f'\033[1;33m->\033[m São {nota20} cédulas de  \033[1;32mR$:\033[m20,00')
while resto >= 10:
    resto -= 10
    nota10 += 1
if nota10 > 0:
    print(f'\033[1;33m->\033[m São {nota10} cédulas de  \033[1;32mR$:\033[m10,00')
while resto >= 5:
    resto -= 5
    nota5 += 1
if nota5 > 0:
    print(f'\033[1;33m->\033[m São {nota5} cédulas de  \033[1;32mR$:\033[m5,00')
while resto >= 1:
    resto -= 1
    nota1 += 1
if nota1 > 0:
    print(f'\033[1;33m->\033[m São {nota1} cédulas de  \033[1;32mR$:\033[m1,00')

print(f"\033[1;33m{'=' * 73}\033[m")

# solução mais enxuta

valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in [50, 20, 10, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')

# Solução matematica

valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")

