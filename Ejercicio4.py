from random import*

y = randrange (1,10)
contador=0
x = 11

while x != y:
    x = int (input("Ingrese un numero entero: "))
    print (" ")
    if x<y:
        print ("El numero ingresado es menor")
        contador = contador + 1
    elif x>y:
        print ("El numero ingresado es mayor")
        contador = contador + 1

print ("¡Adivino el numero!")
contador = contador + 1
print ("Numero de intentos: " + str(contador) )
