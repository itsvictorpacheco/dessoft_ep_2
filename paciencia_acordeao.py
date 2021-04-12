import random
def cria_baralho(): # Gerar baralho
    espadas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']
    copas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']
    ouros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']
    paus = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']
    i = 0
    while i < 13:
        espadas[i] = espadas[i] + '♠'
        copas[i] = copas[i] + '♥'
        ouros[i] = ouros[i] + '♦'
        paus[i] = paus[i] + '♣'
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
enter = input('Pressione enter para iniciar o jogo: ')
while enter == '' or enter == 's':
    baralho = cria_baralho()
    c = 0
    #pensar numa função para imprimir o baralho, com numeros, colorido etc
    while c < len(baralho):
        print('{}. {}'. format(c + 1, baralho[c]))
        c += 1
    while possui_movimentos_possiveis(baralho) == True:
        i = int(input('Escolha uma carta (Digite um número entre 1 e {}): '.format(len(baralho)))) - 1
        if lista_movimentos_possiveis(baralho, i) == [1, 3]:
            print('1. {}'.format(baralho[i - 1]))
            print('2. {}'.format(baralho[i - 3]))
            escolha = int(input('Em qual das cartas você quer empilhar? '))
            if escolha == 1:
                baralho = empilha(baralho, i, i - 1)
            else:
                baralho = empilha(baralho, i, i - 3)
            print(baralho)
        elif lista_movimentos_possiveis(baralho, i) == [1]:
            baralho = empilha(baralho, i, i - 1)
            print(baralho)
        elif lista_movimentos_possiveis(baralho, i) == [3]:
            baralho = empilha(baralho, i, i - 3)
            print(baralho)
        else:
            print('A carta {} não tem nenhuma jogada possível'.format(baralho[i]))
    if len(baralho) == 1:
        print('Parabéns, você ganhou!')
    else:
        print('Não foi dessa vez! ;-;')
    enter = input('Quer jogar novamente? (s/n): ')
print('obrigado por jogar')