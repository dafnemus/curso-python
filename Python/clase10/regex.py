import re

texto = 'Mi nombre es Magali y tengo 28 años'
buscar = 'nombre'

if re.search(buscar,texto):
    print(f'la cadena contiene {buscar} entre sus caracteres')
else:
    print(f'la cadena no contiene {buscar} entre sus caracteres')

texto_encontrado = re.search(buscar,texto)

print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span())

cadena = 'Me gusta la programacion, estudie programacion'
buscar = 'programacion'

print(re.findall(buscar,cadena))
print(len(re.findall(buscar,cadena)))
