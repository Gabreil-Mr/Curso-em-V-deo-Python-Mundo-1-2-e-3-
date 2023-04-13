y = ' Desafio 20 '
print(f'{y:=^50}')
import random
print('A ordem aleatória das pessoas que vão ao banheiro: ')
a = input('Fale um nome: ')
b = input('Agora outro nome: ')
c = input('Mais um nome: ')
d = input('E o último: ')
lista = [a,b,c,d]
random.shuffle(lista)
print(lista)
