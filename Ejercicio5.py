saldo = int(1000)
print ("¡Bienvenido!")
print ("¿Que transaccion desea realizar?")
print ("1. Deposito")
print ("2. Retiro")
print (" ")
opcion = int (input ("Respuesta: "))
print (" ")

if opcion == 1:
    print ("¿Cuanto desea depositar en su cuenta?")
    depo = int(input ("$"))
    transaccion = saldo + depo
    print (" ")
    print ("Su saldo restante es:",transaccion)
else:
    print ("¿Cuanto desea retirar de su cuenta?")
    reti = int(input("$"))
    transaccion2 = saldo - reti
    print (" ")
    print ("Su saldo restante es:",transaccion2)
