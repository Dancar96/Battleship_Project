import numpy as np 

class Tablero:
    def __init__(self):
        self.tablero1 = np.full((10, 10), " ") #SE MODIFICA
        self.tablero2 = np.full((10, 10), " ") #SE QUEDA EN BLANCO
    # Método para colocar un barco en el tablero
    def colocar_barco(self, longitud):
        while True:
            # Generamos posición inicial aleatoria
            fila = np.random.randint(0, 11 - longitud)
            columna = np.random.randint(0, 11 - longitud)
            # Comprobamos si hay suficiente espacio en la fila/columna seleccionada para que se genere el barco
            if np.count_nonzero(self.tablero1[fila, columna:columna+longitud] == 'O') == 0 and np.count_nonzero(self.tablero1[fila:fila+longitud, columna] == 'O') == 0:
                # Colocamos el barco en horizontal o vertical si es 0 o 1 el número aleatorio
                if np.random.randint(0, 2) == 0:
                    # Generamos el barco horizontalmente
                    self.tablero1[fila, columna:columna+longitud] = 'O'
                else:
                    # Generamos el barco verticalmente
                    self.tablero1[fila:fila+longitud, columna] = 'O' 
                break
