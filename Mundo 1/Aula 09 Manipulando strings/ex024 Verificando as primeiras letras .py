print('='*20,'DESAFIO 24','='*20)
nome = str(input('''Será que a sua cidade tem Santo no inicio do nome?
Me dê o nome dela e descubra: ''')).split()
nomeB = (nome[0].title() == 'Santo')
print(nomeB)
#extra:
if nomeB == bool('True'):
    print('Olha!!! Ela tem sim')
else:
    print('nossa, não tem não')
