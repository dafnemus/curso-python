'''
Crear un script llamado **contador.py** que realice varias tareas sobre un fichero llamado **contador.txt** que almacenará un contador de visitas (será un número):

- Nuestro script trabajará sobre el fichero **contador.txt**. Si el fichero no existe o está vacío lo crearemos con el número 0. Si existe simplemente leeremos el valor del contador.
- Luego a partir de un argumento:
    - Si se envía el argumento **inc**, se incrementará el contador en uno y se mostrará por pantalla.
    - Si se envía el argumento **dec**, se decrementará el contador en uno y se mostrará por pantalla.
    - Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.
- Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.
- Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: **Error: Fichero corrupto. *(¡y tiene que ser en rojo! Nah, mentira, eso lo agregué yo)***
'''
def contador():
    visitas = input('Ingresar inc o dec: ')
    global valor_inicial
    valor_inicial = 0
    while visitas == 'inc' or visitas == 'dec':
        visitas = input('Ingresar inc o dec: ')
        if visitas == 'dec':
            valor_inicial -= 1
            print(valor_inicial)
        elif visitas == 'inc':
            valor_inicial += 1
            print(valor_inicial)
        else:
            print(valor_inicial)

contador()
contador_visitas = str(valor_inicial)

with open('contador.txt','w+') as f:
    f.write(f'visitas totales: {contador_visitas} ')
    print(f.read())
    f.close()
