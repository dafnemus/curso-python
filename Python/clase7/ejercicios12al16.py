# 12. Realizar una función llamada **intermedio(a, b)** que a partir de dos números, devuelva su punto intermedio.
a = int(input('Ingrese un numero: '))
b = int(input('Ingrese un numero: '))

def intermedio(a, b):
    return (a + b) / 2

intermedio(a,b)
print()

# 13. Realizar una función **separar(lista)** que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

lista = [1,2,12,11,5,4,8]

def separar(lista):
    par = []
    impar = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            par.append(lista[i])
        else:
            impar.append(lista[i])

    print(f'Los numeros pares son {par}')
    print(f'Los numeros impares son {impar}')

separar(lista)
print()

# 14. Crear una función que, a partir de un dato de entrada que sea en horas, nos informe cuántos minutos y cuántos segundos serían esas horas. Imprimir por pantalla dichos valores.

from datetime import datetime
def convertir():
    formato = "%H:%M"
    hhmmss = input('Introducir hora (hh:mm): ')
    hhmmss = datetime.strptime(hhmmss, formato)
    horas = hhmmss.hour
    minutos = horas * 60
    segundos = (horas * 60) * 60
    print(horas,'en minutos es: ',minutos)
    print(horas,'en segundos es: ',segundos)
    
convertir()
print()

# 15. Crear una función que devuelva una lista con todos los números pares del 0 al 100 inclusive. Imprimir esa lista por pantalla.

def lista_numeros():
    hasta_100 = []
    for i in range(0,101):
        hasta_100.append(i)
    print(hasta_100)
        
lista_numeros()

# 16. Crear una función que, a partir de un mensaje, nos devuelva una lista con todos los números, si los hay, que aparecen en dicho mensaje.

def encontrar_num():
    mensaje = input('Ingrese un mensaje: ')
    lista = mansaje.split()
    numeros = []
    for i in lista:
        if i.isnumeric():
            numeros.append(i)
            print(true)
        else:
            print('No hay numeros en el mensaje')
    print(numeros)

encontrar_num()
