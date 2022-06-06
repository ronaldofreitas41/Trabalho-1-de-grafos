import Grafos
import time

g1 = Grafos.Grafo()
i = []

nome = input("Informe o arquivo: ")

start = int(input("Origem: "))
end = int(input("Destino: "))

g1.ler_arquivo(nome)

#Começa a contar o tempo de execução do algoritmo   
inicio = time.time()

#Execução do algoritmo
match nome:
    case "facebook_combined.txt":
        print("Algoritimo utilizado: Busca Largura Caminhos")
        retornos = g1.buscaLarguraCaminhos(start,end)
    case "rome99c.txt":
        print("Algoritimo utilizado: Bellman Ford")
        retornos = g1.bellmanFord(start)
    case "rg300_4730.txt":
        print("Algoritimo utilizado: Dijkstra")
        retornos = g1.dijkstra(start,end)
    case "toy.txt":
        print("Algoritimo utilizado: Bellman Ford")
        retornos = g1.bellmanFord(start)
    case "USA-road-dt.DC.txt":
        print("Algoritimo utilizado: Bellman Ford")
        retornos = g1.bellmanFord(start)
    case "USA-road-dt.NY.txt":
        print("Algoritimo utilizado: Bellman Ford")
        retornos = g1.bellmanFord(start)
    case "web-Google.txt":
        print("Algoritimo utilizado: Busca Largura Caminhos")
        retornos = g1.buscaLarguraCaminhos(start,end)

#Encontrar caminho percorrido da Origem até o Destino
print("Custo: ", retornos[0][end])
v = retornos[1][end]
i.append(v)

while(v != None):
    v = retornos[1][v]
    if(v == None):
        break
    i.append(v)

i = list(reversed(i))
i.append(end)

print("Caminho: ", i)

#Fim da contagem de tempo de execução do algoritmo
fim = time.time()
tempo = fim - inicio

print("Tempo: ", tempo)
