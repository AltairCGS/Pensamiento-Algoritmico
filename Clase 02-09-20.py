"""
suma = 0
for i in range (1, 6):
    suma += i
    print(i)
print("la suma es: ", suma)
"""
"""
for i in range (1,300):
    if i % 2 != 0:
        print(i)
"""
#Lo mismo de arriba pero simplificado por el incremento
"""
suma = 0
for x in range (2,300,2):
    print(x)
    suma += x
print(suma)
"""
"""
suma = 0
for i in range (1,10):
    suma += i # suma = suma + i
print(suma)
"""
#Calcule la suma de los números pares que están entre el 10 y 2, empezando por
#el 10 y sumando sucesivamente 8,6,…, 2.
"""
suma = 0
for i in range (10,1,-2):
    suma += i #suma = suma + i
print(suma)
"""
#Diseñe un algoritmo para determinar la suma de los números cuya última cifra es
#siete y están comprendidos entre dos números M y N ingresados por el usuario.
"""
print("¡Hola! Queremos hacer la suma de los numeros cuya ultima cifra termina en 7, por favor a continuacion ingresa el rango de estos, por ejemplo, de 10 hasta 50")
M = int(input("Ingresa el primer numero del rango: "))
N = int(input("Ingresa el segundo numero del rango: "))
if M < N:
    menor = M
    mayor = N
else:
    menor = N
    mayor = M
suma = 0
for i in range (menor,mayor+1):
    if i % 10 == 7:
        suma += i
        print("Este numero termina en siete",i)
print("La suma de todos los numeros cuya ultima cifra es siete, es:",suma) 
"""
#Calcule el factorial de un número ingresado por el usuario.
"""
num = int(input("Ingresa un numero para calcular el factorial del mismo: "))
factorial = 1
for i in range (num,1,-1):
    factorial *= i
    print(i)
print("El factorial de",num,"es",factorial)
"""
#De los primeros 100 números enteros positivos, calcule el promedio de sus
# números pares y el promedio de sus números impares.
"""
sum_numeros_pares = 0
sum_numeros_impares = 0
for i in range (1,101):
    if i % 2 == 0:
        sum_numeros_pares += i
    else:
        sum_numeros_impares += i
Promedio_pares = sum_numeros_pares // 50
Promedio_impares = sum_numeros_impares // 50
print("Suma de pares:",sum_numeros_pares)
print("Suma de impares:",sum_numeros_impares)
print("El promedio de numeros pares es:",Promedio_pares)
print("El promedio de numeros impares es:",Promedio_impares)
"""

