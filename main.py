def saber_vizinhos(i,j):
  vizinhos = [
      [i-1,j-1],[i-1,j],[i-1,j+1],
      [i  ,j-1],[i  ,j],[i  ,j+1],
      [i+1,j-1],[i+1,j],[i+1,j+1]
  ]
  return vizinhos

def identificando_linha_coluna_elem(matriz_atual):
  dicio=dict()
  for i, linha in enumerate(matriz_atual):
    for j, elem in enumerate(linha):
      dicio[f'{i,j}'] = elem
  return dicio

def saber_vizinhos_todos(dicio):
  dicio_ = dict()
  for chave in dicio.keys():
    i, j = int(chave[1]), int(chave[4])
    dicio_[f'{i,j}'] = saber_vizinhos(i,j)
  return dicio_

def saber_elem_vizinhos(dicio_todos, Qi):
  dicio_ = dict()
  for chave_pivo in dicio_todos.keys():
    dicio_[chave_pivo] = []
    for coord_vizinhos in dicio_todos[chave_pivo]:
      i_viz, j_viz = coord_vizinhos
      if i_viz >=0 and j_viz >=0 and i_viz <= 4 and j_viz <= 4:
        if (int(chave_pivo[1]), int(chave_pivo[4])) != (i_viz, j_viz):
          vizinho = Qi[i_viz][j_viz]
          dicio_[chave_pivo].append(vizinho)

  return dicio_

def rodada(dicio_elem, dicio_vizinhos, N):
  Qf = [[0 for x in range(N)] for x in range(N)]
  for coord, elem in zip(dicio_elem.keys(),dicio_elem.values()):
    if elem == 0:
      if sum(dicio_vizinhos[coord]) == 3:
        Qf[int(coord[1])][int(coord[4])] = 1
      else:
        Qf[int(coord[1])][int(coord[4])] = 0
    else:
      if sum(dicio_vizinhos[coord]) == 3 or sum(dicio_vizinhos[coord]) == 2:
        Qf[int(coord[1])][int(coord[4])] = 1
      elif sum(dicio_vizinhos[coord]) < 2:
        Qf[int(coord[1])][int(coord[4])] = 0
      else:
        Qf[int(coord[1])][int(coord[4])] = 0
  return Qf

def main(Qi, n):
  for i in range(n):
    dicio = identificando_linha_coluna_elem(Qi)
    dicio_todos = saber_vizinhos_todos(dicio)
    dicio_vizinhos_todos = saber_elem_vizinhos(dicio_todos, Qi)
    Qf = rodada(dicio, dicio_vizinhos_todos, len(Qi))
    Qi = Qf.copy()
  return Qf

Qi = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
]

main(Qi,3)
