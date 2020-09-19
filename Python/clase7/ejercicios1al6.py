# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
email = input('Ingrese su email: ')
def validar(email):
  if email.__contains__('@'):
    print('Su email es valido')
  else:
    print('Email invalido')

validar(email)
print()
# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)
def digitos(numero):
  suma = 0
  while numero != 0:
    # numero = int(input('Ingrese un numero: ')) lo dejo comentado para poder hacer el ejercicio 3.
    digito = numero % 10
    suma = suma + digito
    numero = numero // 10
  return suma
# 3 Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos.
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos.
# Reutilizar la misma función realizada en el ejercicio 2
def suma_total():
  sumatoria = 0
  num = int(input('Ingrese un numero: '))
  while num !=0:
    print('suma', digitos(num))
    sumatoria += num
    num = int(input('Ingrese un numero: '))
  print('Sumatoria', sumatoria)
  print('suma de los digitos del total de la sumatoria', digitos(sumatoria))

suma_total()

print()

# 4 Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.

def ocurrencia():
  entero = int(input('Ingrese un numero de 4 digitos: '))
  digito = int(input('Ingrese 1 digito: '))
  frecuencia = str(entero).count(str(digito))
  print(f'la frecuancia con que aparece {digito} es {frecuencia}')

ocurrencia()
print()

# 5. Escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def factorial(x,n):
  if n > 0:
    x = factorial(x,n-1)
    x = x * n
  elif n < 0:
    x = factorial(x,-n-1) # factoreo de numero negativo
    x = x * n
  else:
    x = 1
  return x

n = int(input("ingresa un numero  \n"))
x = 1
x = factorial(x,n)
print(x)  

print()

# 6.  Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.

def digito_mayor():
  menores = []
  mayor = []
  num = int(input('Ingrese un numero: '))
  while num != 0:
    print('suma', digitos(num))
    mayor.append(digitos(num))
    if num < 10:
      menores.append(digitos(num))
    num = int(input('Ingrese un numero: '))
  print(mayor)
  print(max(mayor))
  print(menores)
  
digito_mayor()

