'''
6. Se ingresa una edad, mostrar por pantalla alguna de las siguientes leyendas:
    ‘menor’ si la edad es menor o igual a 12
    ‘cadete’ si la edad está comprendida entre 13 y 18
    ‘juvenil’ si la edad es mayor que 18 y no supera los 26
    ‘mayor’ en el caso que no cumpla ninguna de las condiciones anteriores.
'''
edad = int(input('Ingese su edad: '))

if edad <= 12:
    print('Menor')
elif edad >= 13 and edad <=18:
    print('Cadete')
elif edad > 18 and edad < 26:
    print('Juvenil')
else:
    print('Mayor')

print()

# 7. Informar los primeros 100 números naturales y su sumatoria
n = 100
suma = 0  
for i in range(n + 1):  
    suma = suma + i  

print('La suma es', suma)

print()

# 8. Dados 50 números enteros, informar el promedio de los mayores que 100 y la suma de los menores que –10.
repeticion = 1
mas_100 = []
menor = []
while repeticion <= 10:
    valor = int(input('Ingrese un numero: '))
    repeticion += 1
    if valor > 100:
        mas_100.append(valor) # agrega el valor a una lista.
    if valor < (-10):
        menor.append(valor)

promedio_mas_100 = sum(mas_100) / len(mas_100) 
sumatoria = sum(menor)  # sum suma los valores de una lista     

print(f'el promedio de los mayores de 100 {mas_100} es {promedio_mas_100}')
print(f'la sumatoria de los -10 {menor} es {sumatoria}')
print()

# 9. Dados 10 valores informar el mayor
n = 1
lista = []
while n <= 10:
    valor = int(input('Ingrese un numero: '))
    lista.append(valor)
    n += 1
mayor = max(lista)
print(f'El mayor de {lista} es {mayor}')

print()
