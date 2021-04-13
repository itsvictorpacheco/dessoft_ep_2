import random
def cria_baralho(): # Gerar baralho com cores
    coringa = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']
    espadas = []
    copas = []
    ouros = []
    paus = []
    i = 0
    while i < len(coringa):
        espadas.append('\033[0;34m{}{}\033[m'.format(coringa[i],'♠'))
        copas.append('\033[0;31m{}{}\033[m'.format(coringa[i],'♥'))
        ouros.append('\033[0;35m{}{}\033[m'.format(coringa[i],'♦'))
        paus.append('\033[0;37m{}{}\033[m'.format(coringa[i],'♣'))
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
    c = 0
    while c < len(baralho):
        print('{}. {}'. format(c + 1, baralho[c]))
        c += 1
    return ''

#PRINTAR REGRAS NO INICIO

enter = input('Pressione enter para iniciar o jogo: ') #Iniciar o jogo
while enter == '' or enter == 's': #loop para o jogador poder recomeçar o jogo sem reiniciar o programa
    baralho = cria_baralho()
    printar_baralho(baralho)
    while possui_movimentos_possiveis(baralho) == True: #Loop para o jogo funcionar enquanto o jogador não perdeu
        i = input('Escolha uma carta (Digite um número entre 1 e {}) ou digite "dica" para ser ajudado: '.format(len(baralho)))
        if i == 'dica': #Se a pessoa quiser uma dica de carta a sr usada
            x = 0
            dica = []
            while x < len(baralho):
                if possui_movimentos_possiveis(baralho[x]) == True:
                    dica.append(baralho[x])
                x += 1
            random.shuffle(dica)
            print('{}.{}'.format(baralho.index(dica[0]) + 1, dica[0]))
        elif int(i) > len(baralho): #Se i for um número fora do baralho
            print('Insira um valor válido')
        else:
            i = int(i) - 1
            if lista_movimentos_possiveis(baralho, i) == [1, 3]: #Se o jogador tiver duas jogadas possíveis
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
            else: #Se a carta não puder ser empilhada de acordo com as regras do jogo
                print('A carta {} não tem nenhuma jogada possível'.format(baralho[i]))
    if len(baralho) == 1: #Se só restou um monte ao final do jogo
        print('\nParabéns, você ganhou! :)\n')
    else:
        print('\nNão foi dessa vez! :(\n')
    enter = input('Quer jogar novamente? (digite s ou n): ')
print('Obrigado por jogar')