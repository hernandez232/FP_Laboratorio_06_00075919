print ("¡Bienvenido!")
x = float(input("Ingrese el valor de la pelicula: $"))
y = float(input("Ingrese el valor de la pelicula: $"))
z = float(input("Ingrese el valor de la pelicula: $"))
print (" ")

if x<y and y<z:
    t = x+y
    print ("Total a pagar:","$" + str(t))
elif x<z and z<y:
    t2 = x+z
    print ("Total a pagar:","$" + str(t2))
elif y<x and x<z:
    t3 = y+x
    print ("Total a pagar:","$" + str(t3))
elif y<z and z<x:
    t4 = y+z
    print ("Total a pagar:","$" + str(t4))
elif z<x and x<y:
    t5 = z+x
    print ("Total a pagar:","$" + str(t5))
elif z<y and y<x:
    t6 = z+y
    print ("Total a pagar:","$" + str(t6))
elif x==y:
    t7 = x+y
    print ("Total a pagar:","$" + str(t7))
elif x==z:
    t8 = x+z
    print ("Total a pagar:","$" + str(t8))
elif y==z:
    t9 = y+z
    print ("Total a pagar:","$" + str(t9))
elif x==y and y==z:
    t10 = x+y
    print ("Total a pagar:","$" + str(t6))
    