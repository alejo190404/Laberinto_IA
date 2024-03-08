#importar librerias
import sys

#Definir funciones
#Imprimir matriz
def imprimirMatriz(matriz):
    print("Matriz:")
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end="\t")
        print()

#Generar camino de forma recursiva
def camino(coordenada_actual, visitada, laberinto, tam, lista_vertices, lista_nodos_adyacentes):
    if (visitada[coordenada_actual[0]][coordenada_actual[1]] == 0 and not(tieneCaminosAdyacentes(coordenada_actual, visitada, laberinto, tam))): #Caso base: No es visitado y no tiene caminos adyacentes no visitados
        return
    

#Pasos adyacentes no visitados
def tieneCaminosAdyacentes(coordenada_actual, visitada, laberinto, tam):
    bordeIzq = False
    bordeDer = False
    bordeSup = False
    bordeInf = False
    if (coordenada_actual[0] == 0):#EsBorde?
        bordeIzq = True
    if (coordenada_actual[1] == 0):#EsBorde?
        bordeSup = True
    if (coordenada_actual[0] == tam-1):#EsBorde?
        bordeDer = True
    if (coordenada_actual[1] == tam-1):#EsBorde?
        bordeInf = True

    if (not(bordeIzq) and visitada[coordenada_actual[0]][coordenada_actual[1]-1] == 0 and laberinto[coordenada_actual[0]][coordenada_actual[1]-1] == 0):
        return True
    if (not(bordeSup) and visitada[coordenada_actual[0]-1][coordenada_actual[1]] == 0 and laberinto[coordenada_actual[0]-1][coordenada_actual[1]] == 0):
        return True
    if (not(bordeDer) and visitada[coordenada_actual[0]][coordenada_actual[1]+1] == 0 and laberinto[coordenada_actual[0]][coordenada_actual[1]+1] == 0):
        return True
    if (not(bordeInf) and visitada[coordenada_actual[0]+1][coordenada_actual[1]] == 0 and laberinto[coordenada_actual[0]+1][coordenada_actual[1]] == 0):
        return True
    return False

#Inicio del programa
#Recibir argumentos
if (len(sys.argv) != 5):
    print("Usage: main.py <archivo de matriz> <dimension N de la matriz> <coordenada de salida (x,y)> <coordenada de meta (x,y)>")

n = int(sys.argv[2])

#Cargar archivo de entrada y asignarlo como matriz
with open(sys.argv[1]) as f:
    laberinto = f.readlines()

for i in range(len(laberinto)):
    laberinto[i] = laberinto[i].replace("[", "")
    laberinto[i] = laberinto[i].replace(" ", "")
    laberinto[i] = laberinto[i].replace("]", "")
    laberinto[i] = laberinto[i].split(",")
    for j in range(len(laberinto[i])):
        laberinto[i][j] = int(laberinto[i][j])

imprimirMatriz(laberinto)

#Transformar a grafo
lista_vertices = {}
lista_nodos_adyacentes = {}

#Matriz para saber si ya se visitó la coordenada
visitada = [[0 for j in range(n)] for i in range(n)]
imprimirMatriz(visitada)

#Determinar qué "coordenadas" son vértices
# for i in range(n):
#     for j in range(n):
#         if (laberinto[i][j] != 1):
#             camino([i, j], visitada, laberinto, n, lista_vertices, lista_nodos_adyacentes)

print(tieneCaminosAdyacentes([1, 1], visitada, laberinto, n))