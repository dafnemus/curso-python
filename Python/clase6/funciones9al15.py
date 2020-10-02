# 9. Crear un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def password():
    contraseña = 'puerta18'
    login = input('Ingrese su contraseña: ')
    if contraseña.lower() == login.lower():    # lower() ignora mayúsculas y minúsculas.
        print('Contraseña valida')
    else:
        print('Contraseña invalida')

password()

print()
# 10. Crear un programa que pida al usuario dos números y muestre por pantalla el cociente de la división entre ellos siempre que el segundo número sea distinto de 0.

numero1 = int(input('Ingrese un número: '))
numero2 = int(input('Ingrese un número mayor que 0: '))

def division(numero1, numero2):
    if numero2 == 0:
        print('error')   # mensaje por si el usuario ingresa por error 0.
    else:
        cociente = (numero1 / numero2) 
        print(f'el cociente de {numero1}/{numero2} es {round(cociente,2)}')

division(numero1,numero2)

print()
# 11. Crear un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input('Ingrese un número: '))

def par(numero):
    if numero % 2 == 0:
        print('Es par')
    else:
        print('Es impar')

par(numero)

print()

# 12. Crear un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input('Ingresa una palabra: ') 

def repeticion(palabra):
    for i in range(10):
        print(palabra)

repeticion(palabra)

print()

# 13. Crear una lista con 6 elementos, luego recorrerla e imprimir elemento a elemento en renglones distintos.
# import random

lista = ['hola', 150, True, 20, 'flores', 65]

def aleatorio(lista):
    # random.shuffle(lista)  # importe Random para usar el metodo shuffle(lista aleatoria)
    for i in range(0,len(lista)): # len(extension de la lista)... range: de la posicion 0 hasta elfinal.
        print(lista[i])  

aleatorio(lista)

print()

## 14. Crear un programa que recorra un diccionario previamente creado y muestre por pantalla:
# > clave → valor 

contacto = { 'name': 'Dafne', 'edad': '22', 'pais': 'Argentina'}
def diccionario(contacto):
    for i in contacto:
        valor = contacto[i]
        print('> ', i, '→ ', valor)

diccionario(contacto)
print()

# 15. Crear un programa que imprima por pantalla todo lo que el usuario ingresa hasta que ingresa la palabra “salir”.

print('Juegos de palabras, ingrese de a una')
print('Si dese terminar el juego ingrese: SALIR')

def juego():
    jugador = ''
    salir = 'salir'
    while jugador != salir.lower():
        if jugador == salir.lower():
            print('Ha terminado por hoy')
        jugador = input('Ingrese una palabra: ')
        print(jugador)

juego()

