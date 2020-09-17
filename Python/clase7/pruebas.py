def digitos(numero):
  suma = 0
  while numero != 0:
    # numero = int(input('Ingrese un numero: ')) lo dejo comentado para poder hacer el ejercicio 3.
    digito = numero % 10
    suma = suma + digito
    numero = numero // 10
  return suma

def digito_mayor():
  menores = []
  mayor = []
  num = int(input('Ingrese un numero: '))
  while num != 0:
    print('suma', digitos(num))
    mayor.append(digitos(num))
    if digitos(num) < 10:
      menores.append(digitos(num))
    num = int(input('Ingrese un numero: '))
  print(mayor)
  print(max(mayor))
  print(menores)
  
digito_mayor()

