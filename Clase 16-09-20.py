#Introduccion ciclo while
# Mostrar todos los números impares desde 1 hasta el 300.
"""
x = 1
while x <= 300:
    print(f"Este numero es impar {x}")
    x += 2
"""
# Realizar una cuenta regresiva desde 10 hasta 0.
"""
x = 10
while x != -1:
    print(x)
    x -= 1
"""
# Imprimir el promedio de una lista de 100 números.
"""
contador = 1
acumulador = 0
while contador != 101:
    print(contador)
    acumulador += contador
    contador += 1
# print(contador)
promedio = acumulador/100 # promedio = acumulador/(contador-1)
print("La suma de los numeros del 1 al 100 es:",acumulador)
print("El promedio es:",promedio)
"""
#Determine la suma de los números enteros mayores que cero y menores que 10.
"""
x = 1
suma = 0
while x < 10:
    suma = suma + x
    x = x + 1
print(suma)
"""
# Determinar cuántas cifras posee un número ingresado por el usuario.
"""
n = int(input("Ingresa un número: "))
cifras = 1
while n > 9:
    n = n / 10
    cifras = cifras + 1
print ("Tu numero tiene",cifras,"cifras")
"""

n = int(input("Ingrese un numero: "))
if n < 0:
    numero = n * -1
else:
    numero = n
contador = 1
control = 10
while control <= numero:
    contador += 1
    control *= 10
print("Tu numero tiene",contador,"cifras")
