# 7. El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?
# def maximo(a,b):
def maximo(x,y):
  if x>y:
    return x
  else:
    return y

 
#def minimo(a,b):  hay que pasarle por paramtros las funciones del programa principal
def minimo(x,y):
  if x<y:
    return x
  else:
    return y

 
#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

print()

# 8. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def documento():
    dni = int(input('Ingrese su DNI: '))
    if len(str(dni)) == 8 or len(str(dni)) == 7:
        print('DNI válido')
    else:
        print('DNI inválido')
        
documento()
print()
# 9. Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.

def ultima_palabra():
    oracion = input('Ingrese una oración \n')
    for i in range(0,len(oracion)):
        print(len(oracion[-1]))

ultima_palabra()
