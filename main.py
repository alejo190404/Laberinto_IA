#importar librerias
import sys
from grafo import Grafo

#Definir funciones
#Imprimir matriz
def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end="\t")
        print()

def cargar_laberinto(ruta_archivo):
    laberinto = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Convierte cada línea en una lista de enteros
            fila = [int(x) for x in linea.strip().replace('[','').replace(']','').split(',')]
            laberinto.append(fila)
    return laberinto

def procesar_coordenadas(coordenadas_str):
    """Convierte una cadena de coordenadas '(x,y)' en una tupla de enteros (x, y)."""
    x, y = coordenadas_str.strip("()").split(",")
    return int(x), int(y)

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



#Cargar archivo de entrada y asignarlo como matriz

n = int(sys.argv[2])
ruta_archivo = sys.argv[1]

# Cargar el laberinto desde el archivo
laberinto = cargar_laberinto(ruta_archivo)
print("Laberinto: ")
imprimirMatriz(laberinto)

#Transformar a grafo
grafo = Grafo(laberinto)
inicio_str = sys.argv[3]
fin_str = sys.argv[4]
inicio = procesar_coordenadas(inicio_str)
fin = procesar_coordenadas(fin_str)

lista_vertices = {}
lista_nodos_adyacentes = {}

#Matriz para saber si ya se visitó la coordenada
visitada = [[0 for j in range(n)] for i in range(n)]


#Generar camino
caminoProfundidad = grafo.primero_profundidad(inicio, fin)
print("Camino encontrado:", caminoProfundidad)
caminoAnchura = grafo.primero_anchura(inicio, fin)
print("Camino encontrado:", caminoAnchura)
caminoAEstrella = grafo.a_estrella(inicio, fin)
print("Camino encontrado:", caminoAnchura)
