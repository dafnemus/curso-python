# 1. Crear un programa que muestre por pantalla la cadena de texto “¡Hola Mundo!”

print('Hola Mundo')

print()

# 2. Crear un programa que almacene en una variable la cadena de texto “¡Hola Mundo!” y luego la muestre por pantalla.

saludo = 'Hola Mundo'
print(saludo)

print()

# 3. Crear un programa que pida al usuario su nombre y su edad y luego muestre por pantalla los siguientes mensajes en renglones distintos:
#  > Hola {nombre} 
# Tu edad es {edad} años

nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')

print('Hola', nombre)
print('Tu edad es', edad)

print()

# 4. Crear un programa que pida al usuario su nombre y muestre por pantalla cuántas letras tiene.

print(nombre, 'Su nombre tiene', len(nombre), 'letras') # reutiliso la variable nombre del ejercicio 3 y sumo len que cuenta la extensión del string que le proveo.

print()

# 5. Crear un programa que realice la siguiente operación aritmética (3*8/2)2 y muestre por pantalla el resultado.

print((3*8/2)**2)



