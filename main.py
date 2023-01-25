import dados_matriz as dados
import heapq as hpq

matriz = []
matriz = dados.matriz()


# calcular necessidade e disponibilidade
def necessidade():
    necessidade = []
    necessidade = dados.necessidade()
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
    dummy = total_necessidade() - total_disp()
    if (dummy != 0):
        a = 0
        for a in range(len(matriz)):
                matriz[a].append(9999)
        return matriz
    else:
        return False

def add_disponibilidade():
    disp = []
    disp = disponibilidade()
    for i in range(len(matriz)):
        matriz[i].append(disp[i])
    return matriz

def add_necessidade():
    matriz.append(necessidade())
    return matriz



# função que calcula as penalidades
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


#print(penalidades_linha())

def penalidades_coluna():
    result = []  # lista para armazenar as penalidades das colunas
    for i in range(len(matriz[0])):
        col = [linha[i] for linha in matriz]  # pega os valores da coluna atual
        two_smallest = hpq.nsmallest(2, col) # pega os dois menores valores
        difference = round(two_smallest[1] - two_smallest[0], 2)
        result.append(difference) 

    return result


#print(penalidades_coluna())


def main():
    verifica_dummy()
    add_disponibilidade()
    add_necessidade()
    print(matriz)

main()