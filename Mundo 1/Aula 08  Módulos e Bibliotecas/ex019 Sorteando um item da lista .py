print('='*20,'Desafio 19', '='*20)
print('Sorteio de um aluno para apagar o quadro, digite o nome dos alunos: ')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro alundo: ')
a4 = input('Quarto aluno: ')
lista = [a1,a2,a3,a4]
import random
print(f'O aluno escolhido será {random.choice(lista)}')