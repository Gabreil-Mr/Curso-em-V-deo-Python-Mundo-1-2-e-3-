print('======================== DESAFIO 11 ======================================')
print('Calculador da quantidade de tinta para a sua parede:')
int=input('Me diga a largura da sua parede, depois a altura, e por fim o rendimento por litro da sua tinta. OK? ')
larg=float(input('A largura: '))
altu=float(input('A altura: '))
p = larg  * altu
rend=float(input('Qual é o rendimento por litro da tinta? '))
sol = p / rend
print(f'Será necessário {sol} litros de tinta para pintar a parede')
