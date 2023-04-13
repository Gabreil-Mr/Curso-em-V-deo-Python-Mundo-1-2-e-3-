print('='*20,'DESAFIO 25','='*20)
nome = str(input('Será que você tem SILVA no nome? Escreva-o e descubra: ')).title()
print(f"Seu nome tem Silva? {nome.find('Silva') >= 0}")

#extra:
nomeB = bool(nome.find('Silva') >= 0)
if nomeB == True :
    print('Você tem Silva no nome!')
else:
    print('Você não tem Silva no nome')
