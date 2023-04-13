print('='*20 , 'DESAFIO 22' , '='*20)
nomec = str(input('Olá!!! Poderia me dizer seu nome completo? ')).strip()
print(f'---> Seu nome todo MAIÚSCULO é: {nomec.upper()}')
print(f'---> Seu nome todo minúsculo é: {nomec.lower()}')
print('---> E também tem {} letras'.format(len(nomec) - nomec.count(' ')))
nomecS = nomec.split()
print(f'---> Seu primeiro nome é {nomecS[0]} e possui {len(nomecS[0])} letras') ,
# Extra:
if nomecS[1:] != []:
    print('<> E também achei seu sobrenome {} muito bonito!'.format(' '.join(nomecS[1:]).title()))