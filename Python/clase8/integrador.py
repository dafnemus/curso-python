import math

class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        puntos = '(' + str(self.x) + ',' + str(self.y) + ')'
        print(puntos)
    print()
    def cuadrante(self):
        x = self.x
        y = self.y

        if x == 0 and y == 0:
            print('Origen')
        elif x != 0 and y == 0:
            print('Eje X')
        elif x == 0 and y != 0:
            print('Eje Y')
        elif x > 0 and y > 0:
            print('Cuadrante 1')
        elif x < 0 and y > 0:
            print('Cuadrante 2')
        elif x < 0 and y < 0:
            print('Cuadrante 3')
        elif x > 0 and y < 0:
            print('Cuadrante 4')
    print()
    def vector(self, punto):
        x = punto.x - self.x
        y = punto.y - self.y
        print(f'vector de ({str(self.x)},{str(self.y)}) y ({str(punto.x)},{str(punto.y)})')
        print(f'es ({str(x)},{str(y)})')
    print()
    def distancia(self, punto):
        d = math.sqrt(((punto.x - self.x)**2) + ((punto.y - self.y)**2))
        print(f'La distancia entre ({str(self.x)},{str(self.y)}) y ({str(punto.x)},{str(punto.y)}')
        print(f'es de {d}')
    print()

class Rectangulo:
    def __init__(self, inicial = Punto(), final = Punto()):
        self.inicial = inicial
        self.final = final
    
    def base_rectangulo(self):
        final, inicial = self.final.x, self.inicial.x
        base = abs(final - inicial)
        print(base)
        return base
    print()
    def altura_rectangulo(self):
        final, inicial = self.final.y, self.inicial.y
        altura = abs(final - inicial)
        print(altura)
        return altura
    print()
    def area_rectangulo(self):
        base = self.base_rectangulo()
        altura = self.altura_rectangulo()
        print(f'el area del rectangulo es de {base * altura}')

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

A.cuadrante()
B.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)

R = Rectangulo(A,B)
R.base_rectangulo()
R.altura_rectangulo()
R.area_rectangulo()
