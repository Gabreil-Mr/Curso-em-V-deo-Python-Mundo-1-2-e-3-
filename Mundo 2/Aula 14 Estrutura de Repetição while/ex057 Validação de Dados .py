print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO XX '}\033[1;33m{'='*30}\033[m")

# coletando dados
print('\033[32m(f - feminino / m - masculino / x - outro)\033[m')
sexo = str(input('\033[1;33m->\033[m Qual é o seu sexo? \033[34m[f/m/x]\033[m ')).lower()
# caso de opção não válida
while sexo not in 'mxf':
    sexo = str(input('\033[1;31mXXX\033[m \nPor favor, digite uma opção válida! \033[34m[f/m/x]\033[m ')).lower()
# colocando o nome completo da variável
if sexo == 'f':
    sexo  = 'feminino'
elif sexo == 'm':
    sexo = 'masculino'
elif sexo == 'x':
    sexo = 'não binário ou trans'
# resultado final
print(f'Muito Obrigado! Sexo \033[1m{sexo}\033[m registrado com sucesso.')
print(f"\033[1;33m{'=' * 73}\033[m")
