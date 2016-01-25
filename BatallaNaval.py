from random import randint 

tablero = []

#LLENAR EL TABLERO CON "0"
for x in range(0, 5):
    tablero.append(["O"] * 5)

#FUNCION PARA IMPRIMIR TABLERO
def print_tablero(tablero):
    for fila in tablero:
        print " ".join(fila)

#FUNCIONES PARA DEFINIR LA POSICION DEL BARCO DE FORMA ALEATORIA
def fila_aleatoria(tablero):
    barco_fila = randint(0, len(tablero)-1)
def columna_aleatoria(tablero):
    barco_col = randint(0, len(tablero)-1)

print_tablero(tablero)