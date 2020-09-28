'''
1. Vamos a crear una clase llamada Person. Sus atributos son: nombre, edad y DNI. construye los siguientes métodos para la clase:

- Un constructor, donde los datos pueden estar vacios.
- mostrar(): Muestra los datos de la persona.
- esMayorDeEdad(): Devuelve un valor lógico si es mayor de edad.
'''
class Persona:
    def __init__(self, nombre,edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrar(self):
        print(f'Usted es {self.nombre}, su edad es {self.edad} años y su DNI es {self.dni}')
    
    def esMayorDeEdad(self):
        if self.edad >= 18:
            print('Ustede es mayor de edad')
        else:
            ('Usted es menor')
'''
2. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular(que es una persona) y canidad(puede tener decimales). El titular es obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

- Un constructor, donde los datos pueden estar vacios.
- El aributo no se puede modificar directamente, solo ingresando o retirando dinero.
- mostrar(): muestra los datos de la cuenta.
- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
'''
class Cuenta(Persona):
    def __init__(self,nombre,edad,dni,cantidad):
        super().__init__(nombre,edad,dni)
        self.cantidad = cantidad
    
    def mostrar_cuenta(self):
        print(f'El titular de la cuenta es {self.nombre}')
        print(f'La cantidad que posee en su cuenta es de ${self.cantidad}')

    def estado_cuenta(self):
        if cantidad > 0:
            print('VERDE: Tiene saldo positivo')
        else:
            print('ROJO: Su saldo es negativo.')
    
    def ingresar(self,ingreso):
        if ingreso > 0:
            self.cantidad += ingreso
    
    def retirar(self,retiro):
            self.cantidad -= retiro
            
'''
3. Definir la clase CuentaJoven que deriva de la anterior. Cuando se crea esta clase, ademas del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Construye los siguientes métodos:

-Un constructor
-Los titulares de esta cuenta tienen que ser mayores de edad. Crear esTitularValido() que devuelve True si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
-Además la retirada de dinero solo se podrá hacer si el titular es válido.
-El método mostrar() ebe devolver el mensaje 'Cuenta Joven' y la bonificación de la cuenta.
Pensar los métodos de la clase madre que hay que reescribir
'''
class CuentaJoven(Cuenta, Persona):
    def __init__(self,nombre,edad,dni,cantidad):
        super().__init__(nombre,edad,dni,cantidad)
    
    def esTitularValido(self):
        if self.edad >= 18 and self.edad <= 25:
            return True
        else:
            return False

    def retirar_dinero(self,retiro):
        if self.esTitularValido():
            self.cantidad -= retiro
            print(self.cantidad)
        else:
            print('Usted no puede realizar esta operación')

    def bonif_cuenta(self):
        if self.esTitularValido():
            porcentaje = 0.05 # 5% de bonificacion 
            self.bonificacion = (self.cantidad * porcentaje) 
    
    def mostrar_cj(self):
        self.total = self.bonificacion + self.cantidad
        print(f'Cuenta Joven su bonificacion es de {self.bonificacion}')
        print(f'Su cuenta es de {self.total}')

PersonaA = Persona('Dafne',22,41194531)
PersonaA.mostrar()
PersonaA.esMayorDeEdad()
print()
CuentaA = Cuenta('Luis',30,33194431,1000)
CuentaA.mostrar_cuenta()
CuentaA.ingresar(300)
CuentaA.mostrar_cuenta()
CuentaA.retirar(200)
CuentaA.mostrar_cuenta()
print()

CuentaB = CuentaJoven('Marta',23,33666589,2000)
CuentaB.esTitularValido()
CuentaB.retirar_dinero(300)
CuentaB.bonif_cuenta()
CuentaB.mostrar_cj()
