import numpy as np
from Clase import Tablero

jugador = Tablero()
ordenador = Tablero()
for i in range(1):
    jugador.colocar_barco(4)
    ordenador.colocar_barco(4)
for i in range(2):
    jugador.colocar_barco(3)
    ordenador.colocar_barco(3)
for i in range(3):
    jugador.colocar_barco(2)
    ordenador.colocar_barco(2)
for i in range(4): 
    jugador.colocar_barco(1)
    ordenador.colocar_barco(1)

    
def rango_de_coordenadas(x, y):
    return x >= 0 and x < 10 and y >= 0 and y < 10 # Para que no se salga del rango de las coordenadas del tablero

def preguntar_por_coordenadas():
    while True:
        fila = int(input("Elige la fila donde quieres disparar "))
        if rango_de_coordenadas(fila-1, 0):
            fila -= 1
            break
        else:
            print("Número invalido, elige uno entre 1 y 10")
    while True:
        columna = int(input("Elige la columna donde quieres disparar "))
        if rango_de_coordenadas(0, columna -1):
            columna -= 1
            break
        else:
            print("Número invalido, elige uno entre 1 y 10")
    return fila, columna

# Creamos un método para que si en las coordenadas elegidas por el usuario hay un barco lo cambie por un X y si hay agua por un -.
def caida_bomba_jugador():
    fila, columna = preguntar_por_coordenadas()
    if ordenador.tablero1[fila][columna] == "O":
        print("Has acertado.")
        ordenador.tablero1[fila][columna] = "X"
        jugador.tablero2[fila][columna] = "X"
        print("Tablero de ataque jugador \n", jugador.tablero2)
        caida_bomba_jugador()
    elif ordenador.tablero1[fila][columna] == "X" or ordenador.tablero1[fila][columna] == "-":
        print("¡Ya has disparado a esta coordenada", (fila, columna), "!")
        print("Tablero de ataque jugador \n", jugador.tablero2)
        caida_bomba_jugador()
    elif ordenador.tablero1[fila][columna] == " ":
        print("¡Agua!")
        ordenador.tablero1[fila][columna] = "-"
        jugador.tablero2[fila][columna] = "-"
        print("Tablero de ataque jugador \n", jugador.tablero2)
                
            
def caida_bomba_ordenador():
    coordenada_random_fila = np.random.randint(0,10)
    coordenada_random_columna = np.random.randint(0,10)
    
    if jugador.tablero1[coordenada_random_fila][coordenada_random_columna] == "O":
        jugador.tablero1[coordenada_random_fila][coordenada_random_columna] = "X"
        ordenador.tablero2[coordenada_random_fila][coordenada_random_columna] = "X"
        print("Tablero barcos jugador \n", jugador.tablero1)
        caida_bomba_ordenador()
        
    elif jugador.tablero1[coordenada_random_fila][coordenada_random_columna] == "X" or jugador.tablero1[coordenada_random_fila][coordenada_random_columna] == "-":
        caida_bomba_ordenador()
                
    elif jugador.tablero1[coordenada_random_fila][coordenada_random_columna] == " ":
        jugador.tablero1[coordenada_random_fila][coordenada_random_columna] = "-"
        ordenador.tablero2[coordenada_random_fila][coordenada_random_columna] = "-"
        print("Tablero barcos jugador \n", jugador.tablero1)