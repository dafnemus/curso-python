# 1. Dados dos valores enteros A y B, informar la suma, la resta y el producto.
a = int(input('ingrese un número: '))
b = int(input('Infrese un número: '))

suma = a + b
resta = a - b
producto = a * b

print(f'La suma de {a} + {b} da {suma}')
print(f'La resta de {a} - {b} da {resta}')
print(f'El producto de {a} * {b} da {producto}')

print()
# Dada un número entero de la forma (AAAAMMDD), que representa una fecha válida mostrar el día, mes y año que representa.

numero = input('Ingrese su fecha de nacimiento(AAAAMMDD): ')
dia = numero[6:]
mes = numero[4:-2]  # con los [] extraigo los caracteres que no necesito según la variable.
año = numero[:-4]
if 8 == len(numero):
    print(f'día: {dia}, mes {mes}, año {año}')
else:
    print(f'Error')

print()
'''
3. A partir de un valor entero ingresado por teclado, se pide informar:
a) La quinta parte de dicho valor
b) El resto de la división por 5
c) La séptima parte del resultado del punto a)
'''
valor = int(input('Ingrese un numero: '))

a = valor / 5
b = valor % 5
c = a / 7
print(round(a,2))
print(b)
print(round(c,2))

print()

# 4. Dados dos valores enteros y distintos, emitir una leyenda apropiada que informe cuál es el mayor entre ellos

a = int(input('Ingrese un número: '))
b = int(input('ingrese un número: '))

if a > b:
    print(f'{a} es mayor a {b}')
    if a == b:
        print(f'{a} y {b} son iguales')
else:
    print(f'{a} es menor a {b}')

print()
# 5. Dadas dos fechas informar cual es la más reciente. Determine cuales serían los datos de entrada y las leyendas a informar de acuerdo al proceso solicitado.

from datetime import datetime

formato = "%d/%m/%Y"  # Formato de fecha que quiero que se ingrese.
fecha1 = input('Introducir fecha inicial (dd/mm/aaaa): ')  
fecha2 = input('Introducir fecha inicial (dd/mm/aaaa): ')  
fecha1 = datetime.strptime(fecha1, formato)   
#El strptime() crea un objeto de fecha y hora a partir de la cadena dada.
fecha2 = datetime.strptime(fecha2, formato)

if fecha1 < fecha2:
    print(f'{fecha2} es más reciente')
    if fecha1 == fecha2:
        print('Ambas fechas son iguales')
else:
    print(f'{fecha1} es más reciente')
