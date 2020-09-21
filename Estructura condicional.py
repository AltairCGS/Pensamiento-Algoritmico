# Ejercicios con estructura condicional if (Este archivo esta incompleto, mas adelante subire la actualizacion)
# Importante: Recuerda quitar al inicio y al final de cada script las triples comillas (""") para que deje de ser una cadena de caracteres
# y vuelve a poner las triples comillas una vez termines de probar el script.
#determinar si un numero es divisor de otro.
"""
N1 = int(input("Ingrese un número: "))
N2 = int(input("Ingrese otro número: "))

if N1 > N2:
    mayor = N1
    menor = N2
else:
    mayor = N2
    menor = N1
if mayor % menor == 0:
    print("El numero ",menor,"es divisor de ",mayor)
else:
     print("El numero ",menor,"no es divisor de ",mayor)
"""
#Diseñe un algoritmo que lea tres números enteros, determine el promedio
#de los números e indique cuál es el número más cercano al promedio.
"""
Num1 = int(input("Ingresa el primer número: "))
Num2 = int(input("Ingresa el segundo número: ")) 
Num3 = int(input("Ingresa el tercer número: "))

Promedio = int(((Num1+Num2+Num3)/3))

Distancia1 = abs(Promedio - Num1)
Distancia2 = abs(Promedio - Num2)
Distancia3 = abs(Promedio - Num3)

if Distancia1 < Distancia2 and Distancia1 < Distancia3:
    print("El número mas cercano al promedio:",Promedio,"Es el número:",Num1)
elif Distancia2 < Distancia1 and Distancia2 < Distancia3:
    print("El número mas cercano al promedio:",Promedio,"Es el número:",Num2)
else:
    print("El número mas cercano al promedio:",Promedio,"Es el número:",Num3)
"""
"""
A = int(input("\nIngrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))
Y = int(input("Ingrese el valor de Y: "))
if Y < A and A < B and B < C:
    X = 0
    print("\nEl valor de X es:",X)
elif A <= Y and Y < B:
    X = 1
    print("\nEl valor de X es:",X)
elif B <= Y and Y < C:
    X = 2
    print("\nEl valor de X es:",X)
elif C <= Y:
    X = 3
    print("\nEl valor de X es:",X)
else:
    X = 4
    print("\nEl valor de X es:",X)
"""
"""
#Caso 2 defines las variables sin preguntarle al usuario. 
A,B,C = 50 #Aqui estan las 3 esferas con el mismo valor
D = 28 #Aqui esta la esfera con el valor diferente
if D > A: #Condicional, si el numero que contiene D es mayor que A entonces me imprimes D es de mayor peso que el resto de esferas
    print(D,"Es de mayor peso que el resto de esferas")
else: #Si lo anterior no se cumple es porque D es menor y me imprimes D es de menor peso que el resto de las esferas. 
    print(D,"Es de menor peso que el resto de esferas")
"""
#Un almacén efectúa una promoción en la cual se hace un descuento sobre el
#valor de la compra total, según el color de la bolita que el cliente saque al
#pagar en caja. Si la bolita es blanca no se le hará descuento alguno, si es
#verde se le hará un 10% de descuento, si es amarilla un 25%, si es azul un
#50% y si es roja un 100%. Hacer un algoritmo para determinar la cantidad
#final que un cliente deberá pagar por su compra.

"""
PrecioA = 20000
PrecioB = 30000
PrecioC = 40000

Blanca = 100
Verde = 90 
Amarilla = 75
Azul = 50
Roja = 0

Producto = str(input("Ingresa el producto de deseas (A,B o C) Solo puedes elegir 1 producto: "))
Cantidad = int(input("Ingresa las unidades que vas a llevar del producto: "))

if Producto.capitalize() == "A":
    Costo = Cantidad * PrecioA
elif Producto.capitalize() == "B":
    Costo = Cantidad * PrecioB
elif Producto.capitalize() == "C":
    Costo = Cantidad * PrecioC
else:
    print("ERROR, Ingresaste un dato invalido")

ColorBola = str(input("Ingresa el color de la bola (Blanca, Verde, Amarilla, Azul o Roja): "))

if ColorBola.capitalize() == "Blanca":
    print("No obtuviste ningun descuento 😔 el total a pagar es:",Costo)
elif ColorBola.capitalize() == "Verde":
    TotalDescuento = (Verde * Costo)/100 #esto es lo mismo que Costo * 0.9
    print("Felicidades, obtuviste un descuento del 10% en tu compra, El total a pagar es:",TotalDescuento)
elif ColorBola.capitalize() == "Amarilla":
    TotalDescuento = (Amarilla * Costo)/100 
    print("Felicidades, obtuviste un descuento del 25% en tu compra, El total a pagar es:",TotalDescuento)
elif ColorBola.capitalize() == "Azul":
    TotalDescuento = (Azul * Costo)/100
    print("Felicidades, obtuviste un descuento del 50% en tu compra, El total a pagar es:",TotalDescuento)
elif ColorBola.capitalize() == "Roja":
    TotalDescuento = (Roja * Costo)/100
    print("Felicidades, obtuviste un descuento del 100% en tu compra, El total a pagar es:",TotalDescuento)
else:
    print("ERROR, Ingresaste un dato invalido, recuerda ingresar los datos tal y como te los piden, las demostraciones salen entre parentisis ()")
"""
"""
A,B,C = 100
D = 2
if D < A:
    print("La esfera D tiene menor peso")
elif D > A:
    print("La esfera D tiene meyor peso")
"""
"""
Categoria = int(input("Ingresa la categoria en la que te encuentras: "))
Unidades = input("¿Cuantas unidades produces?: ")
Salario = int(input("¿Cual es tu salario?: "))
if Categoria == 1 and Unidades > "50":
    X = (105 * Salario)/100
elif Categoria == 2 and Unidades > "50":
    X = (107 * Salario)/100
elif Categoria == 3 and Unidades > "50":
    X = (110 * Salario)/100
elif Categoria == 4 and Unidades > "50":
    X = (115 * Salario)/100
print("Su salario devengado es: ",X)
"""
"""
Salario = 900000
Departamento1 = int(input("Departamento 1 ingrese el total de ventas: "))
Departamento2 = int(input("Departamento 2 Ingrese el total de ventas: "))
Departamento3 = int(input("Departamento 3 ingrese el total de ventas: "))
Total_Ventas = Departamento1 + Departamento2 + Departamento3
Porcentaje33 = (Total_Ventas * 33)/100
Aumento = (Salario * 120)/100
if Departamento1 > Porcentaje33 and Departamento2 > Porcentaje33 and Departamento3 > Porcentaje33:
    print("Felicidades Departamento 1,2 y 3 recibieron un aumento del 20% su nuevo salario es: ",Aumento)
elif Departamento1 > Porcentaje33 and Departamento2 > Porcentaje33:
    print("Felicidades Departamento 1 y 2 recibieron un aumento del 20% su nuevo salario es: ",Aumento)
elif Departamento1 > Porcentaje33 and Departamento3 > Porcentaje33:
    print("Felicidades Departamento 1 y 3 recibieron un aumento del 20% su nuevo salario es: ",Aumento)
elif Departamento2 > Porcentaje33 and Departamento3 > Porcentaje33:
    print("Felicidades Departamento 2 y 3 recibieron un aumento del 20% su nuevo salario es: ",Aumento)
elif Departamento1 > Porcentaje33:
    print("Felicidades Departamento 1 recibieron un aumento del 20% su nuevo salario es: ",Aumento)
elif Departamento2 > Porcentaje33:
    print("Felicidades Departamento 2 recibieron un aumento del 20% su nuevo salario es: ",Aumento)
elif Departamento3 > Porcentaje33:
    print("Felicidades Departamento 3 recibieron un aumento del 20% su nuevo salario es: ",Aumento)
"""