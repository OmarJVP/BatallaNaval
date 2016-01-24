def print_tablero(tablero):
	for i in range(len(tablero)):
		print "  ".join(tablero[i])

tablero = []
for i in range(0,5):
    tablero.append(["O", "O", "O", "O", "O"])

print_tablero(tablero)