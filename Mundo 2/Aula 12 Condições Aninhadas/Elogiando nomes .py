print(f"\033[1;31m{'!*'*10}\033[1;35m EXEMPLO \033[m\033[1;31m{'!*'*10}\033[m")
nome = str(input('Qual é o seu nome? ')).title()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Ana' or nome == 'Sabrina':
    print('Belo nome feminino')
elif nome in 'Matheus Samuel Gabriel Lucas':
    print('Olha! Seu nome é bíblico')
else:
    print('Que nome feio')
print('Tenha um bom dia!')
print(f"\033[1;31m{'-'*56}\033[m")
