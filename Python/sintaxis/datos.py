print("hola mundo")

hola_mundo = "Hola Mundo"

print(hola_mundo)

holaMundo = "hola mundo"
print(holaMundo)

print(5)

print(5.58)

print(5 + 10)

suma = 5 + 10
print(suma)

print(5+10)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
print(nombre + " " + apellido + " " + edad)

print("Ingrese 4 números por teclado:")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

print(num1 + num2)
print(num3 - num4)

nombre = "Magali"
apellido = "Dominguez Lalli"

# Formas de incluir una variable en un string 

print(f"Mi nombre es {nombre} y mi apellido es {apellido}")
print("Mi nombre es {} y mi apellido es {}".format(nombre, apellido))
print("Mi nombre es", nombre, " y mi apellido es", apellido)
print("Mi nombre es " + str(nombre) + " y mi apellido es " + str(apellido)) # recordar que el dato alojado en la variable debe ser str o debo convertirlo

print("Cálculos")
num1 = 10
num2 = 5
num3 = 2

print(f"Realizar la suma entre {num1} y {num2}")
suma = num1 + num2
print(f"La suma entre {num1} y {num2} es {suma}")
print()
print()
print(num1 == num2)  # pregunto si num1 es exactamente igual a num2 --> booleano
print(num1 != num3)  # pregunto si num1 es distinto de num3 --> booleano
print()
comparacion1 = num1 == num2
comparacion2 = num1 != num3
comparacion3 = comparacion1 and comparacion2
comparacion4 = comparacion1 or comparacion2
negacion = not comparacion1
print(comparacion3)
print(comparacion4)
print(negacion)

num1 = float(input("Ingrese un número: "))
print(num1)
num2 = float(input("Ingrese un número: "))
num3 = float(input("Ingrese un número: "))
num4 = float(input("Ingrese un número: "))

suma = num1 + num2 + num3 + num4
resta = num1 - num2 - num3 - num4
prod = num1 * num2 * num3 * num4

print(type(suma))
print(type(resta))
print(type(prod))


