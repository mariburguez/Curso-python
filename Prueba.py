# items 4
precio=0
suma=0
nomProducto = (input ("Ingrese el nombre del producto, finalice con nompre de producto fin"))
while nomProducto != "fin":
    precio = float(input ("Ingrese el precio del producto:"))
    suma= suma + precio
    nomProducto = (input ("Ingrese el nombre del producto, finalice con nompre de producto fin"))
else:
    print ("Finalizo")
    print("el importe total eses: ", suma)