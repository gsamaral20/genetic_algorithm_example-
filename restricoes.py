# Funções de restrições para o algoritmo

# Importando a lista de itens
from item import itens

# Retringir gênero

def restringir_item_genero(pontos, genero_viajante, individuo, itens):
    """
    Restringe a seleção de itens incompatíveis com o gênero do viajante.
    
    Se o gênero do viajante for "masculino" e o indivíduo selecionar algum item de gênero "feminino",
    a função retorna 0, indicando que a solução é inválida para o algoritmo genético.
    Caso contrário, retorna os pontos originais.

    Parâmetros:
    - pontos (float): valor da fitness calculada para o indivíduo.
    - genero_viajante (str): gênero do viajante, por exemplo, "masculino" ou "feminino".
    - individuo (list[int]): lista representando a seleção dos itens (quantidade de cada item).
    - itens (list[obj]): lista de objetos que possuem o atributo 'genero' indicando o gênero do item.

    Retorno:
    - float: retorna 0 se houver conflito de gênero, caso contrário retorna os pontos originais.
    """
    for indice, selecao in enumerate(individuo):
        if genero_viajante == "masculino":
            if selecao != 0:
                if itens[indice].genero == "feminino":
                    return 0
    return pontos



# Capacidade da mochila

def restringir_capacidade_mochila(pontos, capacidade_mochila, individuo, itens):
    """
    Calcula o peso total de um indivíduo (lista de seleções) e verifica 
    se está dentro da capacidade da mochila.

    Parâmetros:
    - pontos (float): pontos calculados pela fitness do indíviduo
    - capacidade_mochila (float): limite máximo de peso que a mochila suporta.
    - individuo (list[int]): lista binária representando a seleção de itens (1 = selecionado, 0 = não selecionado).
    - itens (list[object]): lista de objetos contendo o atributo 'peso' para cada item possível.

    Retorno:
    - float: pontos se o peso total do indivíduo estiver dentro da capacidade; 
             0 caso ultrapasse a capacidade.
    """

    peso_total_individuo = 0

    for indice, selecao in enumerate(individuo):
        if selecao != 0:
            peso_total_individuo += itens[indice].peso * selecao

    print(round(peso_total_individuo, 2))

    if peso_total_individuo <= capacidade_mochila:
        return pontos
    else:
        return 0

# Volume da mochila

def restringir_volume_mochila(pontos, volume_mochila, individuo, itens):
    """
    Calcula o volume total dos itens selecionados e verifica se está dentro da capacidade da mochila.

    Parâmetros:
    - pontos (float): pontuação atual do indivíduo.
    - volume_mochila (float): limite máximo de volume que a mochila suporta.
    - individuo (list[int]): lista de quantidades selecionadas para cada item (0 significa não selecionado).
    - itens (list[object]): lista de objetos contendo o atributo 'volume' para cada item.

    Retorno:
    - float: retorna os pontos originais se o volume total estiver dentro da capacidade;
             retorna 0 caso ultrapasse o limite (penalização máxima).
    """

    volume_total_individuo = 0

    for indice, selecao in enumerate(individuo):
        if selecao != 0:
            volume_total_individuo += itens[indice].volume * selecao

    print(round(volume_total_individuo, 2))

    if volume_total_individuo <= volume_mochila:
        return pontos
    else:
        return 0


# Número de peças íntimas

def restringir_peca_intimas(pontos, numero_dias_viagem, individuo, itens):
    """
    Aplica penalizações acumuladas na pontuação para cada item de roupa íntima
    cuja quantidade selecionada seja menor que o número de dias da viagem.

    Parâmetros:
    - pontos (float): pontuação atual do indivíduo.
    - numero_dias_viagem (int): número mínimo ideal de peças de roupa íntima (equivale aos dias de viagem).
    - individuo (list[int]): lista onde cada posição indica a quantidade selecionada de um item.
    - itens (list[obj]): lista de objetos contendo informações dos itens, incluindo a categoria.

    Retorna:
    - float: pontos ajustados subtraindo 10 para cada item de roupa íntima que não cumpre a quantidade mínima.
    """
    penalizacao = 0
    qtd_ideal_roupa_intima = numero_dias_viagem

    for indice, selecao in enumerate(individuo):
        # Verifica se o item foi selecionado (quantidade maior que zero)
        if selecao != 0:
            # Verifica se o item pertence à categoria "roupa íntima"
            if itens[indice].categoria == "roupa íntima":
                # Se a quantidade selecionada for menor que o ideal, aplica penalidade
                if selecao < qtd_ideal_roupa_intima:
                    penalizacao += 5

    # Caso todas as quantidades estejam dentro do esperado, retorna os pontos originais
    return pontos - penalizacao

def restringir_itens_estacao(pontos, estacao, individuo, itens):
    """
    Aplica penalidades na pontuação com base na incompatibilidade entre
    a estação da viagem e a estação do item selecionado.

    Parâmetros:
    - pontos (int): pontuação atual do indivíduo.
    - estacao (str): estação da viagem (ex: "verao", "inverno").
    - individuo (list): lista com as quantidades selecionadas para cada item.
    - itens (list): lista de objetos Item, cada um com atributo 'estacao'.

    Retorna:
    - pontos ajustados, com penalidades somadas para itens incompatíveis.
    """

    # Normaliza a estação para minúsculas para facilitar a comparação
    estacao = estacao.lower()
    penalizacao = 0  # acumula penalizações totais

    # Percorre todos os itens junto com a quantidade selecionada
    for indice, selecao in enumerate(individuo):
        # Só verifica itens que foram selecionados (quantidade > 0)
        if selecao != 0:
            # Obtém a estação do item, cuidando se for None
            item_estacao = itens[indice].estacao.lower() if itens[indice].estacao else ""

            # Se a estação da viagem for verão:
            if estacao == "verao":
                # Penaliza fortemente itens que são de inverno (muito incompatíveis)
                if item_estacao == "inverno":
                    penalizacao += 20
                # Penaliza menos itens de outono (menos incompatíveis)
                elif item_estacao == "outono":
                    penalizacao += 5

            # Se a estação da viagem for inverno:
            elif estacao == "inverno":
                # Penaliza fortemente itens de verão (muito incompatíveis)
                if item_estacao == "verao":
                    penalizacao += 20
                # Penaliza menos itens de primavera (menos incompatíveis)
                elif item_estacao == "primavera":
                    penalizacao += 5

    # Retorna a pontuação original menos a penalização total acumulada
    return pontos - penalizacao


def restringir_item_obrigatorio(pontos, individuo, itens):
    recompensar = 0
    # Percorre cada item selecionado pelo indivíduo
    for indice, selecao in enumerate(individuo):
        # Verifica se o item foi selecionado (quantidade maior que zero)
        if selecao != 0:
            # Verifica se o item é obrigatório
            if itens[indice].obrigatorio == True:
                # Acumula 10 pontos para cada item obrigatório selecionado
                recompensar += 5
    # Retorna a pontuação original somada à recompensa total
    return pontos + recompensar


def restringir_item_unitario(pontos, individuo, itens):
    recompensar = 0
    # Percorre cada item selecionado pelo indivíduo
    for indice, selecao in enumerate(individuo):
        # Verifica se o item foi selecionado (quantidade maior que zero)
        if selecao != 0:
            # Verifica se o item é obrigatório
            if itens[indice].categoria == "higiene" and selecao == 1:
                # Acumula 5 pontos para cada item obrigatório selecionado
                recompensar += 5
            if itens[indice].categoria == "calçado" and selecao == 1:
                # Acumula 5 pontos para cada item obrigatório selecionado
                recompensar += 5
            if itens[indice].categoria == "documento" and selecao == 1:
                # Acumula 5 pontos para cada item obrigatório selecionado
                recompensar += 15
            if itens[indice].categoria == "eletrônico" and selecao == 1:
                # Acumula 5 pontos para cada item obrigatório selecionado
                recompensar += 5   
            if itens[indice].categoria == "roupa íntima":
                # Acumula 5 pontos para cada item obrigatório selecionado
                recompensar += 10    
    # Retorna a pontuação original somada à recompensa total
    return pontos + recompensar

def recompensar_peca_intimas(pontos, numero_dias_viagem, individuo, itens):
    recompensar = 0
    qtd_ideal_roupa_intima = numero_dias_viagem

    for indice, selecao in enumerate(individuo):
        # Verifica se o item foi selecionado (quantidade maior que zero)
        if selecao != 0:
            # Verifica se o item pertence à categoria "roupa íntima"
            if itens[indice].categoria == "roupa íntima":
                # Se a quantidade selecionada for menor que o ideal, aplica penalidade
                if selecao == qtd_ideal_roupa_intima:
                    recompensar += 10

    # Caso todas as quantidades estejam dentro do esperado, retorna os pontos originais
    return pontos + recompensar
            
""" 
individuo = [
    1, 0, 0, 1,  # chinelo, tênis, bota de trilha, bota
    1, 0, 1, 0,  # meia, calça jeans, calça chino, calça trilha
    0, 1, 0, 1,  # shorts, shorts esporte, calção de banho, cueca
    1, 0, 0, 1,  # camiseta, camisa esporte, camisa manga longa, camisa manga curta
    0, 1, 1, 0,  # jaqueta corta vento, jaqueta jeans, suéter, moletom
    0, 1, 0, 1,  # sobretudo, gorro, luva, cachecol
    0, 1, 0, 1,  # toalha rápida, shampoo 100ml, condicionador 100ml, perfume 100ml
    1, 0, 1, 0,  # desodorante rollon, protetor solar, pasta de dente, escova de dente
    1, 0, 1, 0,  # celular, carregador, power bank, passaporte
    1, 0, 1, 0,  # colírio, sabonete, máscara para dormir, travesseiro de pescoço
    0, 1, 0, 1,  # fone de ouvido, pijama, calcinha, sutiã
    1, 0, 1, 0,  # vestido, blusa regata, saia, casaco leve
    1, 0, 1, 0,  # jaqueta de couro, chapéu, bijuterias, maquiagem básica
    1, 0, 1, 0,  # absorventes, escova de cabelo, secador portátil, creme hidratante
    1, 0, 1, 0,  # perfume extra, legging, roupão
]
"""

#print(restringir_capacidade_mochila(10, individuo, itens))



