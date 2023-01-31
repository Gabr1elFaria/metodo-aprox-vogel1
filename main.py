import dados_matriz as dados
import heapq as hpq

matriz = []
matriz = dados.matriz()
resultado = dados.matriz()
origem = dados.origem()
destino = dados.destino()


def necessidade():
    necessidade = []
    necessidade = dados.necessidade()
    # adicionando 72 pois é a diferença entre disp e necessidade. --dummy--
    # necessidade.append(72)
    return necessidade


def disponibilidade():
    disp = []
    disp = dados.capacidade()
    return disp


def verifica_dummy():
    total_necessidade = sum(necessidade())
    total_disponibilidade = sum(disponibilidade())
    diff = total_necessidade - total_disponibilidade
    if (diff != 0):
        for a in range(len(matriz)):
            matriz[a].append(9999)
    return matriz


def add_disponibilidade():
    disp = []
    disp = disponibilidade()
    disp.append(-1)
    for i in range(len(matriz)):
        if (disp[i] >= 0):
            matriz[i].append(disp[i])
    return matriz


def add_necessidade():
    matriz.append(necessidade())
    return matriz


# função que calcula as penalidades das linhas
def penalidades_linha():
    penalidades_linha = []
    for a in range(len(matriz)-1):
        linha = matriz[a][:-1]
        for i in range(len(linha)):
            if linha[i] < 0:
                linha[i] = 99999
        menores_nums = 0
        menores_nums = hpq.nsmallest(2, linha)
        diff = round(menores_nums[1] - menores_nums[0], 2)
        penalidades_linha.append(diff)
    return penalidades_linha


def penalidades_coluna():
    penalidades_coluna = []  # lista para armazenar as penalidades das colunas
    for i in range(len(matriz[0])-1):
        col = [linha[i] for linha in matriz[:-1]]
        for i in range(len(col)):
            if col[i] < 0:
                col[i] = 99999
        two_smallest = hpq.nsmallest(2, col)
        difference = round(two_smallest[1] - two_smallest[0], 2)
        penalidades_coluna.append(difference)
    return penalidades_coluna


def interacao():
    pen_l = penalidades_linha()
    pen_c = penalidades_coluna()
    maior_v_lin = maior_v_lin = max(pen_l)
    maior_v_col = maior_v_col = max(pen_c)
    index_celula_escolhida_linha = 0
    index_celula_escolhida_coluna = 0

    if (maior_v_col > maior_v_lin):  # se o maior valor está presente na coluna
        index_celula_escolhida_coluna = pen_c.index(
            maior_v_col)  # index do maior valor na coluna
        menor_valor = matriz[0][index_celula_escolhida_coluna]
        for i in range(len(matriz)-1):
            if matriz[i][index_celula_escolhida_coluna] < menor_valor:
                menor_valor = matriz[i][index_celula_escolhida_coluna]
                index_celula_escolhida_linha = i
    else:  # se o maior valor está presente na linha
        index_celula_escolhida_linha = pen_l.index(
            maior_v_lin)  # index do maior valor na linha
        menor_valor = matriz[index_celula_escolhida_linha][0]
        for i in range(len(matriz[index_celula_escolhida_linha])-1):
            if matriz[index_celula_escolhida_linha][i] < menor_valor:
                menor_valor = matriz[index_celula_escolhida_linha][i]
                index_celula_escolhida_coluna = i

    necessidade = matriz[-1][index_celula_escolhida_coluna]
    disponibilidade = matriz[index_celula_escolhida_linha][-1]
    valor_atribuido = min(necessidade, disponibilidade)

    print(origem[index_celula_escolhida_linha] + "  ->  " + destino[index_celula_escolhida_coluna] + "  = ",
          resultado[index_celula_escolhida_linha][index_celula_escolhida_coluna] * valor_atribuido)  # = custo * valor transportado

    if (necessidade == 0) | (disponibilidade == 0):
        if (disponibilidade == 0):
            for i in range(len(matriz)-1):
                matriz[i][index_celula_escolhida_coluna] = - \
                    1  # coluna escolhida vai ser zerada
            matriz[-1][index_celula_escolhida_coluna] = matriz[-1][index_celula_escolhida_coluna] - necessidade
        elif (necessidade == 0):
            for i in range(len(matriz[0])-1):
                matriz[index_celula_escolhida_linha][i] = - \
                    1  # linha escolhida vai ser zerada
            matriz[index_celula_escolhida_linha][-1] = matriz[index_celula_escolhida_linha][-1] - disponibilidade
    elif necessidade < disponibilidade:
        for i in range(len(matriz)-1):
            matriz[i][index_celula_escolhida_coluna] = - \
                1  # coluna escolhida vai ser zerada
        matriz[-1][index_celula_escolhida_coluna] = matriz[-1][index_celula_escolhida_coluna] - valor_atribuido
    elif disponibilidade < necessidade:
        for i in range(len(matriz[0])-1):
            matriz[index_celula_escolhida_linha][i] = - \
                1  # linha escolhida vai ser zerada
        matriz[index_celula_escolhida_linha][-1] = matriz[index_celula_escolhida_linha][-1] - valor_atribuido
    return matriz, pen_l, pen_c


def main():
    verifica_dummy()
    add_necessidade()
    add_disponibilidade()
    soma = 1
    while soma > 0:
        interacao()
        matriz, pen_l, pen_c = interacao()
        soma_linhas = sum(pen_l)
        soma_colunas = sum(pen_c)
        soma = soma_linhas + soma_colunas
    print(matriz)


main()
