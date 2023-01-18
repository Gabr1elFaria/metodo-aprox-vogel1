import dados_matriz as dados
import heapq as hpq

matriz = []
matriz = dados.matriz()


#calcular necessidade e disponibilidade
def necessidade():
    total = 0
    necessidade = []
    necessidade = dados.necessidade()
    total = sum(necessidade)
    return total


#####print("necessidade = ", necessidade())

def disponibilidade():
    total = 0
    disp = []
    disp = dados.capacidade()
    total = sum(disp)
    return total

#####print("disponibilidade = ", disponibilidade())

#verificar necessidade do dummy
def verifica_necessidade_dummy():
    dummy = necessidade() - disponibilidade()
    if(dummy != 0):
        return True
    else:
        return False

#####print(verifica_necessidade_dummy())


#função que insere dummy
def dummy():
    if (verifica_necessidade_dummy()):
        a = 0
        for a in range(len(matriz)):
            matriz[a].append(9999)
    return matriz


#função que calcula as penalidades
def penalidades_linha():
    m_penal = []
    for a in range(len(matriz)):
        menores_nums = 0
        menores_nums = hpq.nsmallest(2, matriz[a])
        m1 = menores_nums[0]
        m2 = menores_nums[1]
        penalidade = m2 - m1
        lista = [penalidade]
        m_penal.append(lista)
    return m_penal


#####print(penalidades_linha())


#precisa pegar penalidades das colunas, iterar sobre cada coluna, e de cada coluna, os valores de todas as linhas
def penalidades_coluna():
    m_penal = []
    l_nums_colunas = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            l_nums_colunas[j].append(matriz[i][j])

    print(l_nums_colunas)

    for a in range(len(matriz)):
        menores_nums = 0
        menores_nums = hpq.nsmallest(2, matriz[a][a])
        m1 = menores_nums[0]
        m2 = menores_nums[1]
        penalidade = m2 - m1
        m_penal.append(penalidade)
    return m_penal


penalidades_coluna()