# 20. Crear un diccionario con 10 estudiantes y sus respectivas notas. Luego crear una función que nos informe los estudiantes aprobados (nota >= 7), los estudiantes desaprobados (4 <= nota < 7) y los estudiantes aplazados (0 <= nota < 4).

estudiante = []
notas = []

dic={}
def listado(estudiante, notas):
    for i in range(len(estudiante)):
        dic_notas = {}
        dic_notas['nombre'] = estudiante[i]
        dic_notas['nota'] = notas[i]
        dic[i] = dic_notas
    return dic
    
print()
def estado_alumnos(dic):
    aprobados = []
    desaprobados = []
    aplazados = []

    for key,value in dic.items():
        if value['nota'] >= 7:
            aprobados.append(value['nombre'])
        elif 4 <= value['nota'] < 7:
            desaprobados.append(value['nombre'])
        elif 0 <= value['nota'] < 4:
            aplazados.append(value['nombre'])

    print("alumnos aprobados \n")
    for i in aprobados:
        print(i)
    print("alumnos desaprobados \n")
    for i in desaprobados:
        print(i)
    print("\nalumnos aplazados \n")
    for i in aplazados:
        print(i)

def ingreso_estudiantes():
    for i in range(10):
        alumno=input('nombre alumno: ')
        nota = int(input('ingrese nota: '))
        estudiante.append(alumno)
        notas.append(nota)
    return estudiante
    return notas

ingreso_estudiantes()
listado(estudiante,notas)
estado_alumnos(dic)
