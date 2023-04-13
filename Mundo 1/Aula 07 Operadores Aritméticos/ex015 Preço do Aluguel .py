print('='*20,'Desafio 14', '='*20)
print('CALCULADORA DE PREÇOS DE ALUGUEL DE CARROS')
km=float(input('Quantos Km foram percorridos? '))
dias=float(input('Por quantos dias foi alugado? '))
conta= dias * 60 + km * 0.15
print(f'O valor de pagamento equivale a RS: {conta}')