print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 53 '}\033[1;33m{'='*30}\033[m")
# solução do Guanabara
# 1) coletando a frase
frase = str(input('Digite a frase para ver se ela é um Palíndromo: \n\033[1;33m-> \033[m')).strip().replace(' ','').upper()
# 2) cria o inverso dela
inverso = ''
for letra in range(len(frase)-1,-1,-1):
    inverso += frase[letra]
# 3) condição final
if inverso == frase:
    print('\033[1;31m* \033[mA frase é um palíndromo')
else:
    print('\033[1;31m* \033[mA frase não é um palíndromo')

print(f"\033[1;33m{'=' * 73}\033[m")

#solução mais simples

# coletando a frase tratada
#frase = input("Qual a frase? ").strip.upper().replace(" ", "")
# invertendo a frase
#inverso = frase[::-1]
#condição final
#if frase == frase[::-1]:
#    print("A frase é um palíndromo")
#else:
#    print("A frase não é um palíndromo")

# Solução que eu estava tentando, mas não consegui

# coletar a frase tratado
# contar quantas letras tinha a frase
# comparar a posição simétrica de cada letra