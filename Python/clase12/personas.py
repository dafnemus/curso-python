'''
Crear un script llamado **personas.py** que lea los datos de un fichero de texto, que transforme cada fila en un diccionario y lo añada a una lista llamada personas. Luego recorre las personas de la lista y para cada una muestra de forma amigable todos sus campos.

El fichero de texto se denominará **personas.txt** y tendrá el siguiente contenido en texto plano (créalo previamente):

1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006

Los campos del diccionario serán por orden:

**id**, **nombre, apellido** y **nacimiento**.
'''
data = {
    '1':{
        'nombre': 'Carlos',
        'apellido': 'Perez',
        'nacimiento': '05/01/1989'
    },
    '2':{
        'nombre': 'Manuel',
        'apellido': 'Heredia',
        'nacimiento': '26/12/1973'
    },
    '3':{
        'nombre': 'Rosa',
        'apellido': 'Campos',
        'nacimiento': '12/06/1961'
    },
    '4':{
        'nombre': 'David',
        'apellido': 'Garcia',
        'nacimiento': '25/07/2006'
    }
}

def datos(data):
    global fichero
    fichero = []
    for key in data:
        valor = data[key]
        lista = f'{key}{valor}'
        fichero.append(lista)

datos(data)

cadena = "\n".join(fichero)

persona = cadena.replace('{','-').replace('}','.')

with open('personas.txt', 'w+') as f:
    f.write(persona)
    print(f.read())
    f.close()
