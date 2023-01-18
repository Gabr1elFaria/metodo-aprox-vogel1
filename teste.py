def segMenor(numeros):
    #variaveis recebem valor infinito
     m1, m2 = float('inf'), float('inf')
     for x in numeros:
         if x <= m1:
             m1, m2 = x, m1
         elif x < m2:
             m2 = x
     return m2


