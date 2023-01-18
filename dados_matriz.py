def origem():
  origem = ['Brasil', 'Canadá', 'França', 'Japão', 'Singapura', 'Zimbabue']
    # primeira linha //precisa deixar a primeira posição vazia, pois não há valor para ela - matriz[0,0]
  return origem

def destino():
  destino = ['Afeganistão',
               'Argélia',
               'Brasil',
               'Canadá',
               'França',
               'Gana',
               'Hungria',
               'Indonésia',
               'Japão',
               'Líbano',
               'Malásia',
               'Marrocos',
               'México',
               'Nepal',
               'Paquistão',
               'Peru',
               'Portugal',
               'Quênia',
               'Romênia',
               'Ruanda',
               'Samoa',
               'Singapura',
               'Tunísia',
               'Uruguai',
               'Zimbabue ']
    # primeira coluna//precisa deixar a primeira posição vazia, pois não há valor para ela - matriz[0,0]
  return destino

  
def matriz():
  matriz = [[6.69, 9.55, 0.00, 8.28, 5.10, 5.41, 5.73, 7.96, 7.64, 8.92, 4.78, 5.10, 3.82, 8.28, 8.60, 8.92,
               3.50, 4.78, 6.69, 4.78, 4.14, 3.18, 4.14, 6.37, 4.46],
              [8.92, 5.41, 3.50, 0.00, 8.60, 7.64, 4.14, 7.96, 8.92, 9.55, 5.73, 7.96, 5.73, 8.60, 9.55, 4.14,
               4.14, 7.01, 7.96, 6.69, 3.50, 7.96, 4.14, 7.32, 7.01],
              [5.73, 6.05, 6.69, 3.50, 0.00, 3.50, 7.01, 8.92, 4.14, 9.55, 8.28, 6.05, 8.28, 8.60, 9.24, 8.28, 3.18,
               4.78, 5.73, 8.92, 5.41, 7.64, 6.69, 4.14, 5.41],
              [6.05, 6.69, 3.18, 7.01, 6.37, 9.55, 5.73, 6.37, 0.00, 6.05, 8.60, 7.32, 7.96, 3.50, 6.37, 9.24, 3.18,
               3.18, 4.14, 4.14, 6.05, 5.10, 4.46, 9.55, 7.32],
              [5.41, 4.46, 6.05, 9.55, 4.78, 8.92, 5.10, 8.60, 4.14, 8.92, 4.14, 4.78, 4.14, 6.37, 3.18, 3.50, 6.05, 5.10,
               5.73, 3.50, 7.64, 0.00, 6.69, 4.78, 4.78],
              [7.96, 3.82, 5.41, 9.55, 6.69, 9.24, 7.96, 6.37, 7.96, 3.50, 8.28, 5.73, 9.55, 5.73, 9.24, 5.73, 6.05, 8.60,
               7.64, 3.18, 7.64, 6.37, 7.96, 9.55, 0.00]
              ]
  return matriz

def capacidade():
  capacidade = [7500,
                  8100,
                  4900,
                  5300,
                  3900,
                  3600]
    # ultima linha
  return capacidade


def necessidade():
  necessidade = [1673,
                   963,
                   1444,
                   1282,
                   2193,
                   782,
                   683,
                   906,
                   1195,
                   962,
                   1782,
                   1147,
                   1711,
                   1441,
                   1878,
                   1172,
                   1254,
                   548,
                   643,
                   1986,
                   929,
                   2173,
                   1907,
                   1908,
                   666]
    # ultima coluna
  return necessidade

