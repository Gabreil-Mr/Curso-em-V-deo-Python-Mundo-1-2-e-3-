print('='*22,'DESAFIO 27','='*22)
nome=str(input('Olá! Qual é o seu nome completo? ')).strip()
nomeS=nome.split()
print(f'Seu primeiro nome é {nomeS[0].title()}')
print(f"Seu último nome é {nome[nome.rfind(' ')+1:].title()}")
#Outra forma:
print(nomeS[-1])


#gabriel moreira rosa
