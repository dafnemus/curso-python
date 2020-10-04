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
with open('people.txt', 'r') as f:
    lista_personas = f.readlines()
    f.close()
    
    personas = []
    for i in lista_personas:
         lista = i.split(';')
         dicc = {
             'numero':lista[0],
             'nombre': lista[1],
             'apellido': lista[2],
             'nacimiento': lista[3]
         }
         personas.append(dicc)

    for individuo in personas:
        print(f'{individuo["numero"]}')
        print(f'Nombre y apellido: {individuo["nombre"]} {individuo["apellido"]}')
        print(f'Fecha de nacimiento: {individuo["nacimiento"]}')

