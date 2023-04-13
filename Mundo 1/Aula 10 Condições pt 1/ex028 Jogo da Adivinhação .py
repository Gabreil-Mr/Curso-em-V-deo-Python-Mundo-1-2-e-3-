import random

print('='*20,'DESAFIO 28','='*20)
n = int(input('Digite um número inteiro entre 0 a 5 vamos ver se você acerta!!! '))
r = random.randint(0,1)
print(f''' O número que você digitou foi {n}
 E o número certo é {r}''')
if n == r:
    print('Parabéns, você acertou!')
else:
    print('HAHAHA!!! Você errou seu Otairo!')