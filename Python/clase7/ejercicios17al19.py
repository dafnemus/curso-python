
# 17. Crear una función que devuelva True si los parámetros ingresados son todos números, False si hay al menos uno de los parámetros ingresados que no es un número, y None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla.

def todos_numeros():
    mensaje = input('Ingrese parametros: ')
    if mensaje.isnumeric(): # son todos numeros
        print(True) 
    elif mensaje.isalpha(): # son todas letras
        print(None)
    elif mensaje.isalnum(): # alfanumerico.
        print(False)
            
todos_numeros()
    
print()
# 18. Crear una función que verifique si una palabra es un palíndromo o no. En caso de que lo sea devolver por pantalla "La palabra es un palíndromo", en caso contrario, devolver "La palabra no es un palíndromo".

def palindromo():
    palabra = input('Ingreses una palabra: ')
    verificar = palabra[::-1]  # obtener una cadena al reves.
    if palabra.lower() == verificar:
        print('Es un palidromo')
    else:
        print('No es un palindromo')

palindromo()


# 19. Crear una función que calcule cuántos litros de nafta gasta un auto que consume 2 litros x 100km, en un viaje ida y vuelta MdP-Bue si la distancia es de 400km. Luego crear una función que, a partir de esos datos, devuelva cuánto significa eso en pesos si el litro de nafta está 60$.

def nafta_total():
    viaje_ida = 400
    viaje_vuelta = 400
    viaje = viaje_ida + viaje_vuelta
    litros_consumo = 2
    cada_100 = 100
    litros_totales = (viaje * litros_consumo)/ cada_100
    return litros_totales

def gasto_nafta():
    precio = 60
    gasto = precio * nafta_total()
    print('El gasto es de ', gasto)

gasto_nafta()





