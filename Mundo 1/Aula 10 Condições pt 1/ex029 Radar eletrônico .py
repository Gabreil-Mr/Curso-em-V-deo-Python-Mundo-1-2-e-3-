print('='*20,'DESAFIO 29','='*20)
vel = float(input('Qual é a velocidade do seu carro? (em km/h) '))
if vel >= 80:
    print(f'Você está multado em R$ {(vel - 80)*7}')
else:
    print('Ótima velocidade, continue assim')