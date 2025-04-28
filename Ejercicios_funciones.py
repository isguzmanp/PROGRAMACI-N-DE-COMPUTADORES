
from fractions import Fraction
import math

#Volumen sólido 

def volumen_esfera(r1):
    return (4/3) * math.pi * r1**3
def volumen_cono(r2, h):
    return (1/3) * math.pi * r2**2 * h
def volumen_solido(a,b):
    return a + b
a = volumen_esfera(3)
b = volumen_cono(4,9/2)
def volumen_solido2(a,c):
    return a + c
c = volumen_cono(4,9//2)
print(f"El volumen del sólido cuando r1=3cm, r2=4cm y h=9/2cm: {volumen_solido(a,b)} cm^3")
print(f"El volumen del sólido cuando r1=3cm, r2=4cm y h=9//2cm: {volumen_solido(a,c)} cm^3")


#Área lateral de un vagón

def area_rectangulo(d,e):
    return d * e
def area_circulo(f):
    return math.pi * f**2
def area_vagon(d,e,f):
    return area_rectangulo(d,e) + (area_circulo(f) * 2)
print(f"El área l del vagón con un rectángulo 4x2m y ruedas con r=3m es: {area_vagon(4,2,3)} m^2")

#Área lateral de un carro

def area_carro(d,e,f):
    return area_rectangulo(d,e) + area_circulo(f)
print(f"El área l del carro con dos rectángulos (uno 5x2m y otro 7x2m) y dos círculos (uno con r=2m y otro con r=4m) es: {area_carro(5,2,2) + area_carro(7,2,4)} m^2")

#Problema 1 
def cantidad_carne(n,m,k):
    return (n*6) + (m*7) + (k*1)
n = int(input("Número de gallinas: "))
m = int(input("Número de pollos: "))
k = int(input("Número de pollitos: "))
print(f"La cantidad de carne es {cantidad_carne(n,m,k)} kg")

#Problema 2
def vueltas(p,l,h,B):
    return B - ((p*300) + (l*3300) + (h*350))
B = int(input("Mi mamá me dio un billete de: $"))
p = int(input("¿Cuántos panes tengo que comprar?: "))
l = int(input("¿Cuántas bolsas de leche tengo que comprar?: "))
h = int(input("¿Cuántos huevos tengo que comprar?: "))
print(f"Le debo a mi mamá ${vueltas(p,l,h,B)}")

#Problema 3
def prestamo(x):
    return ((x*3) / 100) * 2
x = int(input("Pedí un préstamo para pagarlo en 2 meses de: $"))
print(f"Como el interés es de un 3% mensual, al final debo pagar ${int(prestamo(x))} adicionales")

#Porblema 4
def contagios(C,D):
    return (C*(2**D))
C = int(input("El número de contagios actuales es: "))
D = int(input("¿Después de cuántos días desea saber el número de contagios?: "))
print(f"El número de contagios pasados los {D} días va a ser de {contagios(C,D)}")




              





      


