import random
def cria_baralho(): # Gerar baralho com cores
    coringa = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']
    espadas = []
    copas = []
    ouros = []
    paus = []
    i = 0
    while i < len(coringa):
        espadas.append('{}{}'.format(coringa[i],'♠'))
        copas.append('{}{}'.format(coringa[i],'♥'))
        ouros.append('{}{}'.format(coringa[i],'♦'))
        paus.append('{}{}'.format(coringa[i],'♣'))
        i += 1
    baralho =  espadas + copas + ouros + paus
    random.shuffle(baralho)
    return baralho
def extrai_naipe(c):# Extrai naipe da carta
    return c[-1]
def extrai_valor(c):# Extrai valor da carta
    return c[:-1]
def lista_movimentos_possiveis(baralho, i):# Retorna possibilidades da carta
    x = []
    if i != 0:
        if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i - 1]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i - 1]):
            x.append(1)
        if i >= 4:
            if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i - 3]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i - 3]):
                x.append(3)
    return x
def empilha(baralho, o, d):# Atualiza o baralho
    baralho[d] = baralho[o]
    baralho.pop(o)
    return baralho
def possui_movimentos_possiveis(baralho):# Retorna se existem movimentos possíveis
    i = 0
    c = 0
    while i < len(baralho):
        if len(lista_movimentos_possiveis(baralho, i)) != 0:
            c += 1
        i += 1
    if c != 0:
        return True
    else:
        return False
def printar_baralho(baralho): #printa baralho com numero antes daas cartas *FALTA CORES*
    j = 0
    while j < len(baralho):
        if baralho[j][-1] == '♠':
            print(j + 1, '\033[0;34m{}\033[m'.format(baralho[j]))
        elif baralho[j][-1] == '♥':
            print(j + 1, '\033[0;31m{}\033[m'.format(baralho[j]))
        elif baralho[j][-1] == '♦':
            print(j + 1,'\033[0;35m{}\033[m'.format(baralho[j]))
        elif baralho[j][-1] == '♣':
            print(j + 1, '\033[0;37m{}\033[m'.format(baralho[j]))
        j += 1
    return ''

# PENSAR NA IMPLEMENTAÇÃO DE DICA
# ADICIONAR COMENTÁRIOS DE EXPLICAÇÃO

enter = input('Pressione enter para iniciar o jogo: ')
while enter == '' or enter == 's':
    baralho = cria_baralho()
    printar_baralho(baralho)
    while possui_movimentos_possiveis(baralho) == True:
        i = int(input('Escolha uma carta (Digite um número entre 1 e {}): '.format(len(baralho)))) - 1
        if i > len(baralho):
            print('Insira um valor válido')
        else:
            if lista_movimentos_possiveis(baralho, i) == [1, 3]:
                print('1. {}'.format(baralho[i - 1]))
                print('2. {}'.format(baralho[i - 3]))
                escolha = int(input('Em qual das cartas você quer empilhar? '))
                if escolha == 1:
                    baralho = empilha(baralho, i, i - 1)
                elif escolha == 2:
                    baralho = empilha(baralho, i, i - 3)
                printar_baralho(baralho)
            elif lista_movimentos_possiveis(baralho, i) == [1]:
                baralho = empilha(baralho, i, i - 1)
                printar_baralho(baralho)
            elif lista_movimentos_possiveis(baralho, i) == [3]:
                baralho = empilha(baralho, i, i - 3)
                printar_baralho(baralho)
            else:
                if baralho[i][-1] == '♠':
                    print('A carta', '\033[0;34m{}\033[m'.format(baralho[i]), 'não tem nenhuma jogada possível')
                elif baralho[i][-1] == '♥':
                    print('A carta', '\033[0;31m{}\033[m'.format(baralho[i]), 'não tem nenhuma jogada possível')
                elif baralho[i][-1] == '♦':
                    print('A carta', '\033[0;35m{}\033[m'.format(baralho[i]), 'não tem nenhuma jogada possível')
                elif baralho[i][-1] == '♣':
                    print('A carta', '\033[0;37m{}\033[m'.format(baralho[i]), 'não tem nenhuma jogada possível') 
    if len(baralho) == 1:
        print('Parabéns, você ganhou! :)')
    else:
        print('')
        print('Não foi dessa vez! :(')
        print('')
    enter = input('Quer jogar novamente? (digite s ou n): ')
print('Obrigado por jogar')