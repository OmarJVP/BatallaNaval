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
    return randint(0, len(tablero)-1)

def columna_aleatoria(tablero):
    return randint(0, len(tablero)-1)

print_tablero(tablero)

barco_fila = fila_aleatoria(tablero)
barco_col = columna_aleatoria(tablero)

print barco_fila
print barco_col

adivina_fila = int(raw_input("Adivina fila: "))
adivina_columna = int(raw_input("Adivina columna: "))

if (adivina_columna == barco_col) and (adivina_fila== barco_fila):
	print "Felicitaciones!! HUNDICES MI BARCO :C"
elif adivina_fila not in range(5) or adivina_columna not in range(5):
	print "Eso ni siquiera esta en el oceano"
elif adivina_columna=="X" and adivina_fila=="X":
	print "Ya dijiste esas coordenadas"
else:
	print "Intentalo de nuevo, no tocaste mi barco"

adivina_fila = "X"
adivina_columna = "X"