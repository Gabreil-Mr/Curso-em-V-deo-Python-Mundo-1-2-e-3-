print('='*22,'DESAFIO 34','='*22)
sal = int(input('Qual é o seu salário? '))
if sal <= 1250:
    print(f'O seu salário com aumento fica: {sal + (sal * 3 / 20)}')
else:
    print(f'O seu salário com aumento fica {sal + sal/10}')
