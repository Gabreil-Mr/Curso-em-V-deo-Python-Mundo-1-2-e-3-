print('='*20,'Desafio 03','='*20)
print('Olá! Eu sou o maior calculador de todos os tempos! Me dê 2 números, e eu calcularei!')
n1 = int(input('Me fale o primeiro: '))
n2 = int(input('Me fale o segundo: '))
s = n1 + n2
m = n1*n2
p = n1**n2
dif = n1-n2
div = n1/n2
print(f'A soma vale {s}, multiplicação vale {m}, potência vale {p}', end=' ~~~ ')
print(f'A diferença vale {dif}, a divisão vale {div}')
