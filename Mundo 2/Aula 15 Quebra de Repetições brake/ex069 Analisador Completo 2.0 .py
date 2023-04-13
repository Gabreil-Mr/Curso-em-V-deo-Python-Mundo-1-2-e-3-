print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 69 '}\033[1;33m{'='*30}\033[m")
lista_idade = []
lista_sexo = []
mais18 = homens = mulher20 =  pessoa =0
while True:
    pessoa += 1
    print('\033[1;36m=-\033[m'* 15)
    print(f'Cadastre a \033[32m{pessoa}º\033[m pessoa')
# idade
    idade = input('\033[1;31m * \033[mIdade: ')
    while idade.isnumeric() == False:
        print('\033[1;31mXXX\033[m Opção não válida!')
        idade = input('Digite novamente: ')
    idade = int(idade)
    lista_idade += [idade]
# sexo
    sexo = input('\033[1;31m * \033[mSexo: \033[1;35m[F/M/X]\033[m ').lower()
    while sexo not in 'FfmMxX':
        print('\033[1;31mXXX\033[m Opção não válida!')
        sexo = input('Digite novamente: ')
    sexo = str(sexo)
    lista_sexo += [sexo]

# pessoas com mais de 18
    if idade > 18:
        mais18 += 1
# quantidade de homens
    if sexo == 'm':
        homens += 1
# quantidade de mulheres com menos de 20 anos
    if sexo == 'f' and idade < 20:
        mulher20 += 1

    print('\033[1;36m=-\033[m' * 15)
# continuar
    cont = str(input('Gostaria de continuar? \033[1;34m[s/n]\033[m ')).lower()
    while cont not in 'sn':
        print('\033[1;31mXXX\033[m Digite uma opção válida! ')
        cont = str(input('Gostaria de continuar? \033[1;34m[s/n]\033[m ')).lower()
    if cont == 's':
        print('Okay!')
        n = 1
    elif cont == 'n':
        print(f'\033[35m\U0001F625 \033[m Então você não gosta de mim \033[35m\U0001F625 \033[m')
        break

# resultados finais
print(f"\033[1;32m{'*=' * 15}\033[m")
print('\033[1;31mRESULTADOS FINAIS\033[m')
print(f'\033[1;33m->\033[m Pessoas com mais de 18 anos: \033[1;34m{mais18}\033[m')
print(f'\033[1;33m->\033[m Quantidade de homens: \033[1;34m{homens}\033[m')
print((f'\033[1;33m->\033[m Mulheres com menos de 20 anos: \033[1;34m{mulher20}\033[m'))
print(f"\033[1;32m{'*=' * 15}\033[m")

print(f"\033[1;33m{'=' * 73}\033[m")