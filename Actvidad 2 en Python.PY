#1-	Determine el valor de verdad de cada expresión:
#A = 10, B = 3
#a-	(A > B) or (B > A)
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 10
B = 3
X = A > B or B > A
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#b-	(A > B) and (B > A)
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 10
B = 3
X = A > B and B > A
print("Resultado es: " ,X) 
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#A = 23, B = 3, C = 18
#c-	NOT((A >= B) or (B < A)) and (C + B > A)
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 23
B = 3
C = 18
X = not(A >= B or B < A) and C + B + A
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#A = 4, B = 5, C = 1, L = V
#d-	A > B and ¬ L or C < 30
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 4
B = 5
C = 1
L = True
X = A > B and not(L) or C < 30
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#e- B <= 100 and ¬(A > C) and C == 1
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 4
B = 5
C = 1
X = B <= 100 and not(A > C) and C == 1
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#f- B == 5 or C == 30 and ¬L
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
B = 5
C = 1
L = True
X = B == 5 or C == 30 and not(L)
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#g- B + 20 > C - 1 or A + 5 <= 50
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 4
B = 5
C = 1
X = B + 20 > C - 1 or A + 5 <= 50
print("Resultado es: " ,X) 
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#2-	Determinar el valor de X:
#Y = 8, Z = 10, W = 3
#a-	X = (Y MOD W) + (Z DIV W)
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
Y = 8
Z = 10
W = 3
X = Y % W + (Z // W)
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#A = 40, B = 15
#b-	X = (A MOD 5) / (B DIV 3)
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 40
B = 15
X = (A % 5) / (B // 3)
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)

#c-	X = ((A + B) MOD 5)
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 40
B = 15
X = ((A + B) % 5)
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#d-	X = ((A – B) * 3 – (A + B))
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 40
B = 15
X = ((A - B) * 3 - (A + B))
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#e-	X = ((A – B) * 3 – (A DIV B))
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 40
B = 15
X = ((A - B) * 3 - (A // B))
print("Resultado es: " ,X)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#3-	Determine los valores de las variables al ejecutar el siguiente pseudocódigo
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
#Inicio
a = 10
b = 3
c = (a + b) % 2
a = c + b
print("El resultado de c es: ", c)
print("El resultado de a es: ", a)
#Fin
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)


#4-	Encontrar los valores finales de las variables A, B, C después de ejecutar el siguiente grupo de instrucciones:
#Variables Entero: A, B, C
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
A = 163 % 2 + 17
B = (A / 3**(A-16)) + 54  
C = B - 4 + A
A = A * (C // 30)
B = A * 2/3 
B = C - B
print("La ultima operacion es B: ", int(B))
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)
#5-	Conceptos de programación. Preguntas de falso y verdadero y selección múltiple con única respuesta.
#print(" ")
print("\na- Un programa es una lista bien definida, ordenada y finita de operaciones que permite hallar la solución a un problema." )
#print(" ")
while True: 
    X =  input('\nResponda: Verdadero o Falso: ')
    if X.capitalize() == "Falso":
        #print(" ")
        print ('\nRespuesta correcta')
        break
    elif X.capitalize() == "Verdadero":
        #print(" ") 
        print("\nRespuesta incorrecta")
        break
    else:
        #print(" ") 
        print("\nERROR. Recuerda que solo puedes ingresar Verdadero o Falso")