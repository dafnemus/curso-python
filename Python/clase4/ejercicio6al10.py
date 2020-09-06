# 6. Crear un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.

n = int(input('Ingrese un número: '))
suma = 0   
# creo la variable suma como contenedor de de los enteros de 1 a n y le  sumo el indice del for         
for i in range(n + 1):  
    print(i)
    suma = suma + i  

print('La suma es', suma)

print()

# 7. Crear un programa que pida al usuario el monto a invertir y calcular cuánto dinero tendrá en su cuenta al cabo de 6 meses si el interés mensual es de 5%. Mostrar el resultado por pantalla.

inversion = float(input('Ingrese el monto a invertir: '))
interes = 0.05 # porcentaje por decimal.
meses = 6
cuenta = (inversion * interes * meses) + inversion
print(cuenta)

# 8. Crear un programa que pida al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input('Ingrese su edad: '))
if edad >= 18:
     print('Usted es mayor de edad')
else:
     print('Usted es menor de edad')

print()
# 9. Crear un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña = 'puerta18'
login = input('Ingrese su contraseña: ')

if contraseña.lower() == login.lower():    # lower() ignora mayúsculas y minúsculas.
    print('Contraseña valida')
else:
    print('Contraseña invalida')

print()
# 10. Crear un programa que pida al usuario dos números y muestre por pantalla el cociente de la división entre ellos siempre que el segundo número sea distinto de 0.

numero1 = int(input('Ingrese un número: '))
numero2 = int(input('Ingrese un número mayor que 0: '))

if numero2 == 0:
    print('error')   # mensaje por si el usuario ingresa por error 0.
else:
    cociente = (numero1 / numero2) 
    print(cociente)
