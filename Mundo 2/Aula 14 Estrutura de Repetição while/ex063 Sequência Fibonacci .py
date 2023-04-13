print(f"\033[1;33m{'='*28}\033[1;34m{' DESAFIO 63 '}\033[1;33m{'='*30}\033[m")
termos = int(input('Termos: '))
cont = 0

primeiro = 1
anterior = 0

ilustrativo = 0
while cont < termos:
    if cont == termos-1:
        print(ilustrativo)
    else:
        print(ilustrativo, end='\033[1;35m ->\033[m ')
    ilustrativo = primeiro
    proximo = primeiro + anterior
    anterior = primeiro
    primeiro = proximo
    cont += 1

print(f"\033[1;33m{'=' * 73}\033[m")
