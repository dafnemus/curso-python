import random
'''
# 11. Crear un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input('Ingrese un número: '))
if numero % 2 == 0:
    print('Es par')
else:
    print('Es impar')

print()
# 12. Crear un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input('Inresa una palabra: ') 
for i in range(10):
    print(palabra)

print()
# 13. Crear una lista con 6 elementos, luego recorrerla e imprimir elemento a elemento en renglones distintos.

lista = ['hola', 150, True, 20, 'flores', 65]
random.shuffle(lista)  # importe Random para usar el metodo shuffle(lista aleatoria)
for i in range(0,len(lista)): # len(extension de la lista)... range: de la posicion 0 hasta el final.
    print(lista[i])  

print()
## 14. Crear un programa que recorra un diccionario previamente creado y muestre por pantalla:
# > clave → valor 

contacto = { 'name': 'Dafne', 'edad': '22', 'pais': 'Argentina'}
for i in contacto:
    valor = contacto[i]
    print('> ', i, '→ ', valor)
'''
print()
# 15. Crear un programa que imprima por pantalla todo lo que el usuario ingresa hasta que ingresa la palabra “salir”.

print('Una palabra a la vez, cuando desee retirarse escriba salir')
usuario = ''
salir = 'salir'
while usuario != salir.lower():
    usuario = input('Ingrese una palabra: ')
    print(usuario)
    if usuario == salir.lower():
        print('Ha terminado por hoy')
