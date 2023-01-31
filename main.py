import dados_matriz as dados
import heapq as hpq

matriz = []
matriz = dados.matriz()
pen_l = []
pen_c = []


def necessidade():
    necessidade = []
    necessidade = dados.necessidade()
    # adicionando 72 pois é a diferença entre disp e necessidade. --dummy--
    necessidade.append(72)
    return necessidade


def disponibilidade():
    disp = []
    disp = dados.capacidade()
    return disp


def total_necessidade():
    total = 0
    total = sum(necessidade())
    return total


def total_disp():
    total = 0
    total = sum(disponibilidade())
    return total


def verifica_dummy():
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
    m_penal = []
    for a in range(len(matriz)-1):
        linha = matriz[a][:-1]
        for i in range(len(linha)):
            if linha[i] < 0:
                linha[i] = 99999
        menores_nums = 0
        menores_nums = hpq.nsmallest(2, linha)
        m1 = menores_nums[0]
        m2 = menores_nums[1]
        penalidade = m2 - m1
        m_penal.append(penalidade)

    print("PENALIDADE LINHA", m_penal)
    return m_penal


def penalidades_coluna():
    result = []  # lista para armazenar as penalidades das colunas
    for i in range(len(matriz[0])-1):
        col = [linha[i] for linha in matriz[:-1]]
        for i in range(len(col)):
            if col[i] < 0:
                col[i] = 99999
        two_smallest = hpq.nsmallest(2, col)
        difference = round(two_smallest[1] - two_smallest[0], 2)
        result.append(difference)

    print("PENALIDADE COLUNA", result)
    return result


def maior_valor_penalidades_linha(pen_l):
    maior_v_lin = max(pen_l)
    return maior_v_lin


def maior_valor_penalidades_coluna(pen_c):
    maior_v_col = max(pen_c)
    return maior_v_col


def interacao():
    pen_l = penalidades_linha()  # VARIAVEL GLOBAL
    pen_c = penalidades_coluna()  # VARIAVEL GLOBAL
    maior_v_lin = maior_valor_penalidades_linha(pen_l)
    maior_v_col = maior_valor_penalidades_coluna(pen_c)
    print("maior valor pen coluna", maior_v_col)
    print("maior valor pen linha", maior_v_lin)
    index_celula_escolhida_linha = 0
    index_celula_escolhida_coluna = 0

    # FAZER LOGICA PARA RODAR TODAS AS INTERAÇÕES:
    # USAR WHILE? USAR FOR? FAZER RECURSIVIDADE ATÉ QUE TODAS AS CELULAS SEJAM -1(MENOS DISP E NEC)?

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
    print("index coluna", index_celula_escolhida_coluna)
    print("index linha", index_celula_escolhida_linha)
    # print("necessidade", necessidade)
    # print("disponibilidade", disponibilidade)
    # print("valor atribuido", valor_atribuido)

    # if (necessidade == 0):
    #     for i in range(len(matriz[0])-1):
    #         matriz[index_celula_escolhida_linha][i] = - \
    #             1  # linha escolhida vai ser zerada
    #     matriz[index_celula_escolhida_linha][-1] = matriz[index_celula_escolhida_linha][-1] - disponibilidade
    #     print("necessidade = 0")
    # elif (disponibilidade == 0):
    #     for i in range(len(matriz)-1):
    #         matriz[i][index_celula_escolhida_coluna] = -1  # coluna escolhida vai ser zerada
    #     matriz[-1][index_celula_escolhida_coluna] = matriz[-1][index_celula_escolhida_coluna] - necessidade
    #     print("disponibilidade = 0")
    if (necessidade == 0) | (disponibilidade == 0):
        if (disponibilidade == 0):
            for i in range(len(matriz)-1):
                matriz[i][index_celula_escolhida_coluna] = - \
                1  # coluna escolhida vai ser zerada
            matriz[-1][index_celula_escolhida_coluna] = matriz[-1][index_celula_escolhida_coluna] - necessidade
            print("disponibilidade = 0")
        elif (necessidade == 0):
            for i in range(len(matriz[0])-1):
                matriz[index_celula_escolhida_linha][i] = - \
                    1  # linha escolhida vai ser zerada
            matriz[index_celula_escolhida_linha][-1] = matriz[index_celula_escolhida_linha][-1] - disponibilidade
            print("necessidade = 0")
    elif necessidade < disponibilidade:
        for i in range(len(matriz)-1):
            matriz[i][index_celula_escolhida_coluna] = - \
                1  # coluna escolhida vai ser zerada
        matriz[-1][index_celula_escolhida_coluna] = matriz[-1][index_celula_escolhida_coluna] - valor_atribuido
        #print("necessidade < disponibilidade")
    elif disponibilidade < necessidade:
        for i in range(len(matriz[0])-1):
            matriz[index_celula_escolhida_linha][i] = - \
                1  # linha escolhida vai ser zerada
        matriz[index_celula_escolhida_linha][-1] = matriz[index_celula_escolhida_linha][-1] - valor_atribuido
        #print("disponibilidade < necessidade")
    return matriz


def main():
    verifica_dummy()
    add_necessidade()
    add_disponibilidade()
    x = 0
    while x <= 31:
        interacao()
        print(matriz)
        x = x + 1
        print("x", x)
    ##QUADRO NÃO ESTÁ ZERANDO, TEM QUE ZERAR
    ##ESTÁ SOBRANDO O DUMMY NA NECESSIDADE

main()
