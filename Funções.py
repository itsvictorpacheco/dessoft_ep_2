import random
# Gerar baralho
def cria_baralho():
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

# Extrai naipe da carta
def extrai_naipe(c):
    return c[-1]

# Extrai valor da carta
def extrai_valor(c):
    return c[:-1]

# Retorna possibilidades da carta
def lista_movimentos_possiveis(baralho, i):
    x = []
    if i != 0:
        if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i - 1]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i - 1]):
            x.append(1)
        if i >= 4:
            if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i - 3]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i - 3]):
                x.append(3)
    return x

# Atualiza o baralho
def empilha(baralho, o, d):
    baralho[d] = baralho[o]
    baralho.pop(o)
    return baralho

#
def possui_movimentos_possiveis(baralho):
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