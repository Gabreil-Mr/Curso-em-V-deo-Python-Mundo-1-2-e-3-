print('='*20,'DESAFIO 31','='*20)
dis = float(input('Qual foi a distância da viajem em Km? '))
print(f'Você viajou {dis} Km')
if dis <=200:
    print(f'O valor da viajem foi {dis * 0.5}')
else:
    print(f'O valor da viajem foi {dis * 0.45}')