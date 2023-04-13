print(f"\033[1;33m{'='*40}\033[1;34m{' DESAFIO 73 '}\033[1;33m{'='*40}\033[m")

times = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio','AthleticoParanaense', 'SãoPaulo',
             'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'VascodaGama',
             'AtléticoMG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

# 1) mostrar a lista de times

print('\033[1;31m-\033[m'*70)
print('\033[1;36m->\033[m Lista de times do campenato:')
for pos,t in enumerate(times):
    if pos == 9:
        print('')
    print(t,end=', ')
print('')
print('\033[1;31m-\033[m'*70)

# 2) Os 5 primeiros colocados

print('\033[1;36m->\033[m Os 5 primeiros colocados:')
for t in times[:5]:
    print(t,end=', ')
print('')
print('\033[1;31m-\033[m'*70)

# 3) Os 4 últimos colocados

print(f'\033[1;36m->\033[m Os 4 últimos colocados:')
for t in times[-4:]:
    print(t,end=', ')
print('')
print('\033[1;31m-\033[m'*70)

# 4) Em ordem alfabética

print('\033[1;36m->\033[m Lista de times em ordem alfabética:')
for pos,t in enumerate(sorted(times)):
    if pos == 9:
        print('')
    print(t,end=', ')
print('')
print('\033[1;31m-\033[m'*70)

# 5) Posição da Chapecoense

print(f"\033[1;36m->\033[m A Chapecoense está em \033[34m{times.index('Chapecoense')}º\033[m lugar")
print('\033[1;31m-\033[m'*70)

print(f"\033[1;33m{'=' * 93}\033[m")