import random
# Gerar baralho
def cria_baralho():
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