n = int(input ("Ingrese un numero entero: "))
i = 1

print ("Los multiplos de",n,"(en el rango del 1-100) son:")
for i in range (1,101):
    if i%n == 0:
        print (i, end=" ")