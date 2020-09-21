# Ejercicios de clico for in python
# Importante: Recuerda quitar al inicio y al final de cada script las triples comillas (""") para que deje de ser una cadena de caracteres
# y vuelve a poner las triples comillas una vez termines de probar el script.
# Este script me imprime los numeros del 1 hasta el 5 y despues me muestra la suma de esos numeros.
"""
suma = 0
for i in range (1, 6):
    suma += i
    print(i)
print("la suma es: ", suma)
"""
# Este script me imprime en pantalla todos los numeros impares desde el 1 hasta el 300.
"""
for i in range (1,300):
    if i % 2 != 0:
        print(i)
"""
# Este script me muestra todos los numeros pares del 1 hasta el 300. 
# (Es el mismo script de arriba solo que simplificado por el incremento de 2 en el rango)
"""
suma = 0
for x in range (2,301,2):
    print(x)
    suma += x
print(suma)
"""
# Este script me imprime la suma de los numeros mayores que 0 y menores que 10
"""
suma = 0
for i in range (1,10):
    suma += i # suma = suma + i
print(suma)
"""
# Calcule la suma de los números pares que están entre el 10 y 2, empezando por
# el 10 y sumando sucesivamente 8,6,…, 2.
"""
suma = 0
for i in range (10,1,-2): # Aqui en el rango, vamos de 10 hasta 1 con incremento de -2
    suma += i # Esto es un forma simplificada de poner (suma = suma + i)
print(suma)
"""
#Diseñe un algoritmo para determinar la suma de los números cuya última cifra es
#siete y están comprendidos entre dos números M y N ingresados por el usuario.
"""
print("¡Hola! Queremos hacer la suma de los numeros cuya ultima cifra termina en 7, por favor a continuacion ingresa el rango de estos, por ejemplo, de 10 hasta 50")
M = int(input("Ingresa el primer numero del rango: "))
N = int(input("Ingresa el segundo numero del rango: "))
if M < N:  #Este es un script anti tontos, por lo que esta condicional es para encontrar el numero menor y el mayor
    menor = M
    mayor = N
else:
    menor = N
    mayor = M
suma = 0
for i in range (menor,mayor+1): # Una vez encontrados el numero menor y el mayor, realizamos el rango.
    if i % 10 == 7: # Esta condicion me permite saber si el numero termina en 7
        suma += i # Aqui realizamos la suma de los numeros que terminan en 7
        print("Este numero termina en siete",i)
print("La suma de todos los numeros cuya ultima cifra es siete, es:",suma) 
"""
# Calcule el factorial de un número ingresado por el usuario.
# factorial es multiplicar el numero por todos los numeros anteriores a este ejemplo: 4 factorial = 4x3x2x1 = 24
"""
num = int(input("Ingresa un numero para calcular el factorial del mismo: "))
factorial = 1
for i in range (num,0,-1):
    factorial *= i
    print(i)
print("El factorial de",num,"es",factorial)
"""
#De los primeros 100 números enteros positivos, calcule el promedio de sus
# números pares y el promedio de sus números impares.
"""
sum_numeros_pares = 0
sum_numeros_impares = 0
cont_pares = 0
cont_impares = 0
for i in range (1,101):
    if i % 2 == 0:
        sum_numeros_pares += i
        cont_pares += 1
    else:
        sum_numeros_impares += i
        cont_impares += 1
Promedio_pares = sum_numeros_pares // cont_pares
Promedio_impares = sum_numeros_impares // cont_impares
print("Suma de pares:",sum_numeros_pares)
print("Suma de impares:",sum_numeros_impares)
print("El promedio de numeros pares es:",Promedio_pares)
print("El promedio de numeros impares es:",Promedio_impares)
"""
# Imprimir el promedio de una lista de 100 números.
"""
suma = 0
for i in range (1,101):
    print(i)
    suma += i
print(suma)
promedio = suma/i
print("El promedio es:", promedio)
"""
# Lo mismo de arriba pero sin imprimir i dentro del ciclo.
"""
suma = 0
for i in range (1,101):
    suma += i
promedio = suma/i
print("El promedio es:", promedio)
"""
# Lo mismo de arriba pero con valores ingresados por el usuario
"""
N1 = int(input("Ingrese un valor: "))
N2 = int(input("Ingrese otro valor: "))
if N1 > N2:
    mayor = N1
    menor = N2
else:
    mayor = N2
    menor = N1
suma = 0
cont = 0
for i in range (menor,mayor+1):
    suma += i
    cont += 1
promedio = suma/cont
print("El promedio es:", promedio)
"""
# Determinar si un numero es primo o no.
"""
num = int(input("Ingrese un numero: "))
cont = 0
for i in range (1,num+1):
    print(num%i)
    if num % i == 0:
        cont += 1
if cont > 2:
    print("El numero no es primo")
else:
    print("El numero es primo")
"""
# Determinar el mayor número de una lista arbitraria de números reales.
"""
n = int(input("Ingrese el numero de elementos de la lista: "))
mayor = 0
for i in range (1,n+1):
    num = float(input("Ingrese un numero positivo: "))
    if num > mayor:
        mayor = num
print("El número mayor de la lista es:",mayor)
"""
# Dado el radio de varios círculos, determinar el área y la circunferencia de cada
# uno de ellos y encontrar el círculo de mayor área.
"""
import math
n = int(input("Ingrese el numero de circulos: "))
mayor = 0
for i in range (1,n+1):
    radio = float(input(f"\nIngrese el radio del circulo {i}: "))
    area = math.pi*radio**2
    print("El area del circulo",i,"es:",area)
    circunferencia = 2 * math.pi * radio
    print("La circunferencia del circulo",i,"es:",circunferencia)
    if area > mayor:
        mayor = area
        cir_mayor = i
print("\nEl circulo de mayor area es:",cir_mayor)
"""
# Calcule la suma de los divisores de n distintos de n.
"""
n = int(input("Ingrese un numero: "))
if n < 0:
    n *= -1
suma = 0
for i in range (1,n+1):
    print(i)
    if n % i == 0 and i != n:
        suma += i
print(f"La suma de los divisores de {n} distintos de {n} es: {suma}")
"""