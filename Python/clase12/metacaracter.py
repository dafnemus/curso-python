import re
# ancla
patron = 'hola$'
cadena = 'buenos dias, hola, hehe'

if re.search(patron,cadena):
    print(True)

patron2 = '^mi nombre'
cadena2 = 'he mi nombre es dafne'

if re.search(patron2,cadena2):
    print(True)

print()
 # clases
patron3 = '[AR]'
lista_vuelos = [
    'AR2606',
    'AR2607',
    'IB1304'
]

for vuelo in lista_vuelos:
    if re.findall(patron3,vuelo):
        print(f'El vuelo {vuelo} ')

print()
# rangos
vuelos_ar = [
    'AR1133',
    'AR1305',
    'AR1293',
    'AR1371'
    'AR1303',
    'AR2709',
    'AR2701',
    'AR2601'
]

for i in vuelos_ar:
    if re.findall('AR[1300-1800]', i):
        print(f'El vuelo {i} es internacional')
    else:
        print(f'El vulo {i} es de cabotaje')

print()
# universal
patron4 = '.hola'
cadena4 = '$%%$%%$%$%%$hola'

if re.findall(patron4, cadena4):
    print(True)

patron5 = 'hola+'
cadena5 = 'hola buenos dias hola'

if re.findall(patron5,cadena5):
    print('True')

print()
# cuantificador
patron6 = 'hola{1,5}'
cadena6 = 'hola'

if re.findall(patron6, cadena6):
    print(True)
