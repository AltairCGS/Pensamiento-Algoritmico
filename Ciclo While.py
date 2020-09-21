# Ejercicios de clico for in python
# Importante: Recuerda quitar al inicio y al final de cada script las triples comillas (""") para que deje de ser una cadena de caracteres
# y vuelve a poner las triples comillas una vez termines de probar el script.
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
cont = 0
while contador <= 100:
    print(contador)
    acumulador += contador
    contador += 1
    cont += 1
print("cantidad de numeros es :",cont)
promedio = acumulador/100 # promedio = acumulador/(contador-1)
print("La suma de los numeros del 1 al 100 es:",acumulador)
print("El promedio es:",promedio)
"""
# Lo mismo de arriba pero con datos mas pequeños, del 3 al 9, para comprobar el codigo.
"""
contador = 3
acumulador = 0
cont = 0
while contador <= 9:
    print(contador)
    acumulador += contador
    contador += 1
    cont += 1
print("La cantidad de numeros es:",cont)
promedio = acumulador/(cont) # promedio = acumulador/(contador-1)
print(f"La suma de los numeros del 3 al 9 es: {acumulador}")
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
# Determinar cuántas cifras posee un número ingresado por el usuario,
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
"""
# hay formas mas faciles de hacer el script de arriba en python, solo que estamos viendo ciclo while
# y hay que aplicarlo, la forma mas sencilla de hacer esto en python es con la funsion len()
# que devuelve como resultado la cantidad de caracteres que tiene un str
"""
n = int(input("Ingresa un numero: "))
x = len(str(n)) #aqui llamamos a la funcion len() y dentro de ella convertimos la variable n en un str.
print(f"Tú numero tiene {x} cifras.")
"""
# Calcular la suma de los valores de una lista de números enteros, la
# cantidad de valores negativos, positivos, iguales a cero y el total de los
# números en la lista.
"""
lista = int(input("Ingrese el numero de elementos de la lista: "))
suma = 0
cont_pos = 0
cont_neg = 0
cont_cero = 0
cant_total = 0
while lista > 0:
    num = int(input("Ingrese un numero: "))
    suma += num
    cant_total += 1
    if num > 0:
        cont_pos += 1
    elif num < 0:
        cont_neg += 1
    else:
        cont_cero += 1
    lista -= 1
print('La suma de los numeros de la lista es:',suma)
print('El total de numeros positivos es:',cont_pos)
print('El total de numeros negativos es:',cont_neg)
print('El total de numeros cero es:',cont_cero)
print('El total de numeros en la lista es:',cant_total)
"""
# Determinar el mayor número de una lista arbitraria de números reales.
"""
Lista = int(input('Ingrese el numero de elementos de la lista: '))
mayor = -999999999999999999999
while Lista > 0:
    num = float(input('Ingrese un numero: '))
    if num > mayor:
        mayor = num
    Lista -= 1
print('El numero mayor de la lista es el',mayor)
"""
# Diseñe un algoritmo para determinar la suma de los números cuya última
# cifra es cinco y están comprendidos entre dos números M y N ingresados por
# el usuario.
"""
M = int(input('ingrese un numero: '))
N = int(input('ingrese un numero: '))
if M > N:
    mayor = M
    menor = N
else:
    mayor = N
    menor = M
suma = 0
while menor <= mayor:
    if menor % 10 == 5:
        suma += menor
        print('Este numero termina en cinco:',menor)
    menor += 1
print("La suma de los numeros cuya ultima cifra es cinco es:",suma)
"""
# Calcule la suma de los números pares que están entre el 10 y 2, empezando
# por el 10 y sumando sucesivamente 8,6,…, 2.
"""
control = 10
suma = 0
while control >= 2:
    if control % 2 == 0:
        suma += control
        print('Este numero es par:',control)
    control -= 1
print('La suma de los numeros pares del 10 al 2 es:',suma)
"""