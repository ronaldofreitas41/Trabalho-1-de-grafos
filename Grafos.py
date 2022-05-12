class Grafo:

  #Função Construtora do Grafo
  def __init__(self, num_vert = 0, lista_adj = None, mat_adj = None , arestas = None):

    self.num_vert = num_vert

    #Verificações acerca das srestas e Lista de Adjacencias
    #-------------------------------------------------------------------------------
    if lista_adj == None:
      self.lista_adj = [[]for _ in range(num_vert)]
    else: 
      self.lista_adj = lista_adj

    if arestas == None:
      self.arestas = [[]for _ in range(num_vert)]
    else:
      self.arestas = arestas
    #-------------------------------------------------------------------------------

  #Função criada para adicionar aresta com valor default (1) do vértice u ao vértice v
  #-------------------------------------------------------------------------------
  def add_aresta(self, u, v, w = 1):

    self.num_arestas += 1

    if u < self.num_vert and v < self.num_vert:

      self.arestas.append((u, v, w))
      self.lista_adj[u].append((v, w)) 

    else:
      print("Aresta inválida!")
  #-------------------------------------------------------------------------------

  #Função criada para remover uma aresta do vértice u ao vértice v (caso exista)
  #-------------------------------------------------------------------------------
  def remove_aresta(self, u, v):

    if u < self.num_vert and v < self.num_vert:

      if self.mat_adj[u][v] != 0:

        self.num_arestas += 1
        self.mat_adj[u][v] = 0

        for (v2, w2) in self.lista_adj[u]:

          if v2 == v:
            self.lista_adj[u].remove((v2, w2))
            break

      else:
        print("Aresta inexistente!")

    else:
      print("Aresta invalida!")
  #-------------------------------------------------------------------------------

  #Função criada para ler um arquivo no formato DIMACS
  #-------------------------------------------------------------------------------
  def ler_arquivo(self, nome_arq):

    try:
        arq = open(nome_arq)

        #Leitura do cabeçalho
        #-------------------------------------------------------------------------------
        str = arq.readline()
        str = str.split(" ")
        self.num_vert = int(str[0])
        self.num_arestas = int(str[1])
        #-------------------------------------------------------------------------------


        #Inicialização da Estrutura de Dados
        #-------------------------------------------------------------------------------
        self.lista_adj = [[] for _ in range(self.num_vert)]

        for _ in range(0,self.num_arestas):
            str = arq.readline()
            str = str.split(" ")

            u = int(str[0])
            v = int(str[1])
            w = int(str[2])

            self.add_aresta(u, v, w)
        #-------------------------------------------------------------------------------
    
    except IOError:
        print("Nao foi possivel encontrar ou ler o arquivo!")
  #-------------------------------------------------------------------------------

  #Função criada para encontrar valor mínimo para distância
  #-------------------------------------------------------------------------------
  def valorMinimo(self, dist, lista):

      k = None
      min = float("inf")

      for i in lista:
          if(dist[i] < min):
              min = dist[i]
              k = i

      return k
  #-------------------------------------------------------------------------------

  #Função criada para inicializar a variável Q e preenchê-la com os vértices
  #-------------------------------------------------------------------------------
  def preencheQ(self):

      Q = [None for _ in range(self.num_vert)]

      for i in range(self.num_vert):
          Q[i] = i

      return Q 
  #-------------------------------------------------------------------------------

  #Algoritmo de Dijkstra
  #-------------------------------------------------------------------------------
  def dijkstra(self, s, e):

      dist = [ float("inf") for _ in range(len(self.lista_adj)) ]
      pred = [None for _ in range(len(self.lista_adj))]

      dist[s] = 0
      Q = self.preencheQ()
      u = None

      while len(Q) != 0:

          u = self.valorMinimo(dist, Q)

          #Verificação da chegada ao vértice de Destino
          #-------------------------------------------------------------------------------
          if(u == e):
            break
          #-------------------------------------------------------------------------------

          Q.remove(u)

          for i in self.lista_adj[u]:

              if dist[i[0]] >  dist[u]+i[1]:
                  dist[i[0]] = dist[u]+i[1]
                  pred[i[0]] = u  

      return dist, pred
  #-------------------------------------------------------------------------------
  
  #Algoritmo de Bellman-Ford
  #-------------------------------------------------------------------------------
  def bellmanFord(self, s):

    dist = [ float("inf") for _ in range(len(self.lista_adj)) ]
    pred = [None for _ in range(len(self.lista_adj))]

    dist[s] = 0
    
    for _ in range(self.num_vert - 1):

      trocou = False

      for (u,v,w) in self.arestas:

        if dist[v] >  dist[u]+w:
          dist[v] = dist[u]+w
          pred[v] = u
          trocou = True
      
      #Otimização do algoritmo para evitar descobertas desnecessárias
      #-------------------------------------------------------------------------------
      if(trocou == False):
        break
      #-------------------------------------------------------------------------------

    return dist,pred
  #-------------------------------------------------------------------------------

  #Algoritmo de Busca em Largura
  #-------------------------------------------------------------------------------
  def buscaLarguraCaminhos(self, s, t):

      dist = [ float("inf") for _ in range(len(self.lista_adj)) ]
      pred = [None for _ in range(len(self.lista_adj))]

      Q = [s]
      dist[s] = 0

      while len(Q) != 0:

          u = Q.pop()

          for (v, w) in self.lista_adj[u]:

              if dist[v] == float("inf"):
                  Q.append(v)
                  dist[v] = dist[u]+1
                  pred[v] = u

              if (pred[t]!= None):
                  break

      return dist,pred
#-------------------------------------------------------------------------------      