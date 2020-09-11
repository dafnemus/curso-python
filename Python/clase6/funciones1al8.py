# 1. Crear un programa que muestre por pantalla la cadena de texto “¡Hola Mundo!”

def saludo():
    print('Hola Mundo')

saludo()

print()

# 2. Crear un programa que almacene en una variable la cadena de texto “¡Hola Mundo!” y luego la muestre por pantalla.

def saludo2():
    saludo = 'Hola Mundo'
    print(saludo)

saludo2()

# 3. Crear un programa que pida al usuario su nombre y su edad y luego muestre por pantalla los siguientes mensajes en renglones distintos:
#  > Hola {nombre} 
# Tu edad es {edad} años

nombre = input('Ingrese su nombre: ') # Creo la variable de forma global para poder usarlo en otras funciones.
edad = input('Ingrese su edad: ')
def usuario():
    print(f'Hola, {nombre}')
    print(f'Tu edad es {edad}')

usuario()

print()
# 4. Crear un programa que pida al usuario su nombre y muestre por pantalla cuántas letras tiene.

def caracteres():
    name = len(nombre)
    print(nombre, 'Su nombre tiene', name, 'letras') 

caracteres()

print()
# 5. Crear un programa que realice la siguiente operación aritmética (3*8/2)2 y muestre por pantalla el resultado.

def calculo():
    a = 3
    b = 8
    c = 2
    print(f'La operacion ({a}*{b}/{c}){c} es igaul a {(a*b/c)**c}')

calculo()

print()
# 6. Crear un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.

def sumatoria():
    n = int(input('Ingrese un número: '))
    suma = 0
    for i in range(n + 1):
        print(i) # imprime los numeros a sumar
        suma = suma + i
    print(f'La suma de todos los enteros de 1 hasta {n} es {suma}')

sumatoria()

print()

# 7. Crear un programa que pida al usuario el monto a invertir y calcular cuánto dinero tendrá en su cuenta al cabo de 6 meses si el interés mensual es de 5%. Mostrar el resultado por pantall

def cuenta():
    inversion = float(input('Ingrese el monto a invertir: '))
    interes = 0.05 # porcentaje por decimal.
    meses = 6
    cuenta_total = (inversion * interes * meses) + inversion
    print(f'Su cuenta seria de ${cuenta_total} en {meses} meses')

cuenta()

print()

# 8. Crear un programa que pida al usuario su edad y muestre por pantalla si es mayor de edad o no.

def mayor_edad():
    edad = int(input('Ingrese su edad: '))
    if edad >= 18:
        print('Usted es mayor de edad')
    else:
        print('Usted es menor de edad')

mayor_edad()

print()

