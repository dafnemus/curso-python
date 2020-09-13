'''
# 10. Dados N valores informar el mayor, el menor y en que posición del conjunto fueron ingresados.
n = 1
valores = []
while n <= 5:
    valor = int(input('Ingrese un numero: '))
    valores.append(valor)
    n += 1
mayor = valores.index(max(valores))
menor = valores.index(min(valores))

print(f'El mayor de {valores} es {max(valores)} se ingreso en la posicion {mayor}')
print(f'El menor de {valores} es {min(valores)} se ingreso en la posicion {menor}')

# 11. Dado un conjunto de Nombres y Fechas de nacimientos (AAAAMMDD), que finaliza con un Nombre= ‘FIN’, informar el nombre de la persona con mayor edad y el de la más joven.

'''

'''
12. Dado un conjunto de valores, que finaliza con un valor nulo, determinar e imprimir (si hubo valores):
a) El valor máximo negativo
b) El valor mínimo positivo
c) El valor mínimo dentro del rango -17.3 y 26.9
d) El promedio de todos los valores.
'''

conjunto = 1
positivos = []
negativos = []
rango = []
while conjunto <= 5:
    valor = float(input('Ingrese un numero: '))
    conjunto += 1
    if valor < 0:
        negativos.append(valor)
    if valor > 0:
        positivos.append(valor)
    if valor > -17.3 and valor < 26.9:
        rango.append(valor)

promedio_pos = sum(positivos)/len(positivos)
promedio_neg = sum(negativos)/len(negativos)
promedio = promedio_neg + promedio_pos
max_neg = max(negativos)
min_pos = min(positivos)
min_rango = min(rango)

print(promedio)
print(negativos)
print(max_neg)
print(positivos)
print(min_pos)
print(min_rango)
