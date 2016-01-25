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
    return randint(1, len(tablero))

def columna_aleatoria(tablero):
    return randint(1, len(tablero))

print "Juguemos batalla naval"
print "INTENTA HUNDIR MI BARCO"
print_tablero(tablero)

barco_fila = fila_aleatoria(tablero) 
barco_col = columna_aleatoria(tablero) 

print barco_fila
print barco_col

for turno in range(1,5):
	print 
	print "TURNO: " + str(turno)
	adivina_fila = int(raw_input("Adivina fila: ")) 
	adivina_columna = int(raw_input("Adivina columna: "))

	if (adivina_columna == barco_col) and (adivina_fila== barco_fila):
		print "Felicitaciones!! HUNDISTE MI BARCO :C"
		break
	#CONDICIONES QUE MARCAN ERROR
	elif (adivina_fila <= 0 or adivina_fila > 5 or adivina_columna <= 0  or adivina_columna > 5):
		print "Eso ni siquiera esta en el oceano"
	elif (tablero[adivina_fila-1][adivina_columna-1]=="X"):
		print "Ya dijiste esas coordenadas"
	else:
		print "Intentalo de nuevo, no tocaste mi barco"
		tablero[adivina_fila-1][adivina_columna-1] = "X"
	print_tablero(tablero)
	if turno == 4:
		print
		print "Se acabaron las oportunidades"
		print "Fin del juego"

