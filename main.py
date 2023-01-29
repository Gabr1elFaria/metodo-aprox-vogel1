import dados_matriz as dados
import heapq as hpq

matriz = []
matriz = dados.matriz()


# calcular necessidade e disponibilidade
def necessidade():
    necessidade = []
    necessidade = dados.necessidade()
    necessidade.append(72) ##adicionando 72 pois é a diferença entre disp e necessidade. --dummy--
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

#def verifica_dummy(): fazer tratamento para adicionar dummy na necessidade depois dos 9999
    dummy = total_necessidade() - total_disp()
    if (dummy != 0):
        a = 0
        for a in range(len(matriz)):
            matriz[a].append(9999)
        return matriz
    else:
        return False

def verifica_dummy():
    for a in range(len(matriz)):
        matriz[a].append(9999)
    return matriz


def add_disponibilidade():
    disp = []
    disp = disponibilidade()
    disp.append(-1)
    for i in range(len(matriz)):
        if(disp[i] >= 0):
            matriz[i].append(disp[i])
    return matriz

def add_necessidade():
    matriz.append(necessidade())
    return matriz



# função que calcula as penalidades das linhas
def penalidades_linha():
    m_penal = []
    for a in range(len(matriz)-1):
        menores_nums = []
        for value in matriz[a][:-1]:
            if value >= 0:
                menores_nums.append(value)
        if len(menores_nums)>1:
            menores_nums = hpq.nsmallest(2, menores_nums)
            m1 = menores_nums[0]
            m2 = menores_nums[1]
            penalidade = m2 - m1
            m_penal.append(penalidade)
    return m_penal


def penalidades_coluna():
    result = []  # lista para armazenar as penalidades das colunas
    for i in range(len(matriz[0])-1):
        col = [linha[i] for linha in matriz[:-1]]  # pega os valores da coluna atual
        two_smallest = hpq.nsmallest(2, col) # pega os dois menores valores
        difference = round(two_smallest[1] - two_smallest[0], 2)
        result.append(difference) 
    return result

def maior_valor_penalidades_linha():
    pen_l = []
    pen_l = penalidades_linha()
    maior_v_lin = max(pen_l)
    return maior_v_lin

def maior_valor_penalidades_coluna():
    pen_c = []
    pen_c = penalidades_coluna()
    maior_v_col = max(pen_c)
    return maior_v_col

def interacao():
    pen_l = []
    pen_l = penalidades_linha()
    pen_c = []
    pen_c = penalidades_coluna()
    maior_v_lin = maior_valor_penalidades_linha()
    maior_v_col = maior_valor_penalidades_coluna()
    index_celula_escolhida_linha = 0
    index_celula_escolhida_coluna = 0

    ##PRECISA VER SE VAI DEIXAR NA FUNCAO OU NAO O CALCULO DOS MAIORES VALORES DAS PENALIDADES
    ##PRECISA ATUALIZAR O VALOR DAS DISPONIBILIDADES E DAS NECESSIDADES
    ##UTILIZAR A VARIAVEL  sub_valor_nec_disp

    if(maior_v_col > maior_v_lin):#se o maior valor está presente na coluna
        index_celula_escolhida_coluna = pen_c.index(maior_v_col)#index do maior valor na coluna
        menor_valor = matriz[0][index_celula_escolhida_coluna]
        for i in range(len(matriz)-1):
            if matriz[i][index_celula_escolhida_coluna] < menor_valor:
                menor_valor = matriz[i][index_celula_escolhida_coluna]
                index_celula_escolhida_linha = i      
    else:#se o maior valor está presente na linha
        index_celula_escolhida_linha = pen_l.index(maior_v_lin)#index do maior valor na linha
        menor_valor = matriz[index_celula_escolhida_linha][0]
        for i in range(len(matriz[index_celula_escolhida_linha])-1):
            if matriz[index_celula_escolhida_linha][i] < menor_valor:
                menor_valor = matriz[index_celula_escolhida_linha][i]
                index_celula_escolhida_coluna = i

    necessidade = matriz[-1][index_celula_escolhida_coluna]
    disponibilidade = matriz[index_celula_escolhida_linha][-1]
    if necessidade < disponibilidade:
        for i in range(len(matriz)-1):
            matriz[i][index_celula_escolhida_coluna] = -1  #coluna escolhida vai ser zerada
        sub_valor_nec_disp = disponibilidade - necessidade
    elif disponibilidade < necessidade:
        for i in range(len(matriz[0])-1):
            matriz[index_celula_escolhida_linha][i] = -1 #linha escolhida vai ser zerada
        sub_valor_nec_disp = disponibilidade - necessidade   

    return matriz



def main():
    verifica_dummy()
    add_necessidade()
    add_disponibilidade()
    penalidades_coluna()
    penalidades_linha()
    print(interacao())
main()