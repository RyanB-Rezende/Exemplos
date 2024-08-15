import random

nomes=[]

while True:
    nome = input('Digite Um Nome (DIgite -1 Para parar): ')

    if nome == '-1':
        break
    else:
        nomes.append (nome)

print(f'Nome Das Pessoas {len(nomes)}')
print(f'Lista De Nomes: {nomes}')
Nomesord = sorted(nomes)
print(f'Lista de Nomes em ordem: {Nomesord}')

print(f'O terceiro nome informado: {nomes[2]}')

random.seed
sorteado = random.randint(0, len(nomes)-1)
print(f'O sorteado é {nomes[sorteado]}')

