import random

def buscaSequencial (dados, buscado):
    achou = 0
    i = 0

    while (((i < len(dados))) and (achou == 0)):
        if (dados[i] == buscado):
            achou = 1
        else:
            i = i + 1
    if (achou == 0):
        return -1
    else:
        return i + 1

#programa principal 

#gerando 10 valores dentro de um intervalo de 0 até 9
dados = random.sample(range(10), 10)

print(dados)

buscado = int(input('Digite o valor que deseja buscar: '))
achou = buscaSequencial(dados, buscado)

if (achou == -1):
    print('Valor não encontrado.')
else:
    print('Valor encontrado na posição {}'.format(achou))