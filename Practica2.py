# items 1

mayores=0
menores=0
edad=0
edad = int((input ("Ingrese edad")))
while edad > -1: # hay edaddes con cero
    if edad>=18:
        print("es mayor de edad")
        mayores += 1
    else:
        print("es menor de edad")
        menores += 1
    edad = int((input ("Ingrese edad (finalice con -1)")))
else:
    print ("Termino!")
    print("menores= ", menores)
    print("mayores= ", mayores)

# items 2
a = float(input ("Ingrese números A"))

b = float(input ("Ingrese números B"))

if a>b:
    print("A es mayor que B (A>B)")
elif b>a:
    print("B es mayor que A (B>A)")
elif b==a:
    print("A y B son iguales (A=B)")

# items 3
promedio=0
sueldo=0
suma=0
canEmpleados = int(input ("Ingrese cantidad de empleados"))
for i in range (canEmpleados): #va desde el cero hasta la cant 
    sueldo = float(input ("Ingrese ingrese sueldo del empleado numero"))
    suma = suma + sueldo #suma += sueldo 
promedio=suma/canEmpleados
print("el promedio es: ", promedio)

# items 4
precio=0
suma=0
nomProducto = (input ("Ingrese el nombre del producto, finalice con nompre de producto fin"))
while nomProducto != "fin":
    precio = float(input ("Ingrese el precio del producto")) #precio = float(input ("Ingrese el precio del producto:", nomProducto))
    suma= suma + precio
    nomProducto = (input ("Ingrese el nombre del producto, finalice con nompre de producto fin"))
else:
    print ("Finalizo")
    print("el importe total eses: ", suma)