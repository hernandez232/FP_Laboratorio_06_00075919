grados = int (input ("Ingrese los grados de la temperatura: "))
print (" ")
print ("Ingrese el numero de la izquierda segun la operacion que desea realizar")
print ("1. Fahrenheit a Celsius"," ")
print ("2. Celsius a Fahrenheit"," ")
print ("3. Kelvin a Celsius", " ")
print (" ")
opcion = int(input("Respuesta: "))
print (" ")

if opcion == 1:
    conversion = int ((grados - 32)*0.5555555559)
    print ("La coversion de Fahrenheit a Celsius es:",conversion,"grados Celsius"," ")
elif opcion == 2:
    conversion2 = int ((grados*1.8) + 32)
    print ("La coversion de Celsius a Fahrenheit es:",conversion2,"grados Fahrenheit"," ")
elif opcion == 3:
    conversion3 = int (grados - 273.1)
    print ("La coversion de Kelvin a Celsius es:",conversion3,"grados Celsius"," ")
else:
    print ("El valor ingresado es incorrecto")
