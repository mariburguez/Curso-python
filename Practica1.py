""" Practica
1. Declarar variables de tipo int, float, string, bool y None.
2. Mostrar el contenido de las variables declaradas en el punto anterior, y además
mostrar por pantalla el tipo de dato usando la función type()
3. Mostrar por pantalla un cartel que diga “Hola Mundo”
4. Ingresar por teclado tu nombre, y mostrar por pantalla un saludo. Por ej.:
“Hola Juan, como estas?”
5. Ingresar por teclado números y mostrar por pantalla que tipo de dato es, usando
type(), si el dato es string utilizar la conversión de tipo.
6. Utilizar operadores aritméticos, relaciones y lógicos combinados. Mostrar por pantalla
el resultado de dichas comparaciones. Por ej.: """

#int
x=3
print(type(x))

#string
x="Hola"
print(type(x))

#float
x=3.5
print(type(x))

#bool
x=True
print(type(x))

#None
x=None
print(type(x))
#Prueba de git ”
#Mostrar por pantalla un cartel que diga “Hola Mundo”
x="Hola"
y="Mundo"
#concatenarcadenas
valor=x+y
print(type(valor))
print(type(x+y))

#Ingresar por teclado tu nombre, y mostrar por pantalla un saludo. 
nombre = input ("ingresa nombre")
print ("Hola", nombre, "como estas?")

#Ingresar por teclado números y mostrar por pantalla que tipo de dato es, usando type(), si el dato es string utilizar la conversión de tipo.
edad=input("Dime tu edad: ")
print("tu edad es: ", edad)
print("tipo de dato de edad", type(edad))
#castear (puede ser con int o float)
edad=int(input("Dime tu edad:"))
print("tu edad", edad)
print("tipo de dato de edad", type(edad))

#Utilizar operadores aritméticos, relaciones y lógicos combinados.
b=3
print("b=", b)
c= 2
print("c=", c)
print((b<c)and(10==0))



