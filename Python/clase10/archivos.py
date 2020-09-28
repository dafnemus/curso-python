data = '''Este archivo es el contenido de mi
primer archivo'''

with open('archivo.txt','w+') as f:
    f.write(data) # escritura
    f.seek(0) # donde se posiciona el cursor
    print(f.read()) # lee el archivo
    print(f.tell()) # cuenta los caracteres
    f.close() # cerrar siempre


