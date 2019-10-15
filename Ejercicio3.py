print ("CUENTA PARES")
contador = 0

opcion = 1
while opcion == 1:
    n = int(input ("Ingrese un numero par: "))
    if n%2 == 0:
        contador += 1
        print ("¿Quiere ingresar otro numero par?")
        print ("1. Si")
        print ("2. No")
        print (" ")
        opcion = int (input("Respuesta: "))
        print (" ")
        if opcion == 2:
            print ("Ha escrito:", contador, "numeros pares")
        elif opcion >2:
            ("El valor ingresado es incorrecto")
    elif n%2 != 0:
        print ("El numero ingresado no es un par")
        print ("¿Quiere ingresar un numero par?")
        print ("1. Si")
        print ("2. No")
        print (" ")
        opcion = int(input ("Respuesta: "))
        print (" ")
        if opcion == 2:
            print ("Ha escrito:", contador, "numeros pares")
        elif opcion < 1 or opcion >2:
            ("El valor ingresado es incorrecto")

