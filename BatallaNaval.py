from random import randint 

tablero = []

print "Juguemos batalla naval"
print "INTENTA HUNDIR MI BARCO"
print "Solo tendras 4 oportunidades"
#PREGUNTA AL USUARIO CUANTOS BARCOS QUIERE ENCONTRAR
barcos = int(raw_input("Cuantos barcos deseas tratar de hundir:  "))

#LLENAR EL TABLERO CON "0" DEL TAMAnO DETERMINADO
tamano = barcos*4
for x in range(tamano):
    tablero.append(["O"] * tamano)

#FUNCION PARA IMPRIMIR TABLERO
def print_tablero(tablero):
    for fila in tablero:
        print " ".join(fila)

#FUNCIONES PARA DEFINIR LA POSICION DEL BARCO DE FORMA ALEATORIA
def fila_aleatoria(tablero):
    return randint(1, len(tablero))

def columna_aleatoria(tablero):
    return randint(1, len(tablero))

print_tablero(tablero)
barco_fila = []
barco_col = []

for i in range(barcos):
	barco_fila.append(fila_aleatoria(tablero))
	barco_col.append(columna_aleatoria(tablero))

print barco_fila
print barco_col

for turno in range(1,5):
	print 
	print "TURNO: " + str(turno)
	adivina_fila = int(raw_input("Adivina fila: ")) 
	adivina_columna = int(raw_input("Adivina columna: "))
	for i in range(barcos):
		if (adivina_columna == barco_col[i]) and (adivina_fila== barco_fila[i]):
			print "Felicitaciones!! HUNDISTE MI BARCO :C"
			break
		#CONDICIONES QUE MARCAN ERROR
		elif (adivina_fila <= 0 or adivina_fila > tamano or adivina_columna <= 0  or adivina_columna > tamano):
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

