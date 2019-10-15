fila = int (input ("Inserte el numero de filas: "))
columna = int (input ("Inserte el numero de columnas: "))

for f in range (1, fila+1):
    for c in range (1, columna+1):
        print ("*", end=" ")
    print (" ")