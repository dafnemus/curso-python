# 16. Crear una función que, a partir de un mensaje, nos devuelva una lista con todos los números, si los hay, que aparecen en dicho mensaje.

def encontrar_num():
    mensaje = input('Ingrese un mensaje: ')
    numeros = []
    for i in mensaje:
        if i.isnumeric():
            numeros.append(i)
    print(numeros)

encontrar_num()
