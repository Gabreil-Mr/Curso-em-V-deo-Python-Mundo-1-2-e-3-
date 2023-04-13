print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 55 '}\033[1;33m{'='*30}\033[m")
# variavel base para mulheres com menos de 20 anos
mulheres = 0
# variavel base de homem + velho
maximo = 0
homemmaisvelho = ''
# variavel base de média
media = 0
# coletando os dados
for c in range(1,2):
    print('\033[1;35m-'*7,f'{c}º PESSOA','-'*7,'\033[m')
    nome = input(f'Nome: ').strip()
    idade = int(input('Idade: '))
    media += idade
    sexo = input('Sexo: (M/F/X)  ').lower().strip()
    # definindo o homem + velho
    if sexo == 'm' and idade > maximo:
        maximo = idade
        homemmaisvelho = nome
    # contando o número de mulheres - 20 anos
    if sexo == 'f' and idade < 20:
        mulheres += 1
print('\033[1;35m-\033[m'*19)
# resultado final
print(f'\033[1;33m->\033[m A média de idade é \033[34m{media/2}\033[m')
print(f'\033[1;33m->\033[m O homem mais velho é \033[34m{homemmaisvelho}\033[m, e ele tem \033[1m{maximo}\033[m anos')
print(f'\033[1;33m->\033[m Ao todo são \033[34m{mulheres}\033[m mulheres com menos de 20 anos')

print(f"\033[1;33m{'=' * 73}\033[m")

# ideias: se a pessoa escrever algum dado errado o programar pedir pra ele digitar denovo
