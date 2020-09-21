# Este es el script del ultimo punto del primer examen de la materia.
#Desarrolle un programa en Python que resuelva el siguiente problema,
#adjunte el archivo .py guardado con su nombre, por ejemplo, Juanito Acosta.py
#Se tiene cuatro esferas (A, B, C, D), las cuales se sabe que tres son de igual peso y una diferente.
#Determine cuál es la esfera diferente y si es de mayor o menor peso.
"""
Esferas_AByC = 50 #Como se sabe que 3 esferas son de igual peso, determinare las esferas A,B y C con el mismo valor. (Este valor se le puede pedir a usuario tambien)
Esfera_D = int(input("Ingresa el peso de la esfera D, (Esta sera comparada con el peso de las esferas A,B y C y te diremos si pesa más o menos que estas): ")) #Este valor en lugar de pedirselo al usuario, tambien se puede determinar un valor fijo para la variable

if Esfera_D > Esferas_AByC:
    print("La esfera D tiene mayor peso que el resto de las esferas A,B y C")
elif Esfera_D < Esferas_AByC:
    print("La esfera D tiene menor peso que el resto de las esferas A,B y C")
elif Esfera_D == Esferas_AByC:
    print("La esfera D tiene el mismo peso que el resto de las esferas A,B y C") #Pongo esta condicional, porque al pedircela al usuario puede ingresar un valor igual al de las esferas A,B y C
#El ejercicio me pide determinar cual es la esfera diferente que tiene un peso diferente a las otras 3 que tienen el mismo peso,
#no imprimi en las condicinales diciendo que la esfera D es diferente a las demas,
#ya que al decir que esta es de mayor o menor peso, sabemos que es diferente
"""
#Forma correcta de hacerlo quitando limitaciones
A = int(input('ingrese el peso de A: '))
B = int(input('ingrese el peso de B: '))
C = int(input('ingrese el peso de C: '))
D = int(input('ingrese el peso de D: '))
if A == B and A == C:
    if D > A:
        print('La esfera diferente es D y es de mayor peso')
    else:
        print('La esfera diferente es D y es de menor peso')
elif A == B and A == D:
    if C > A:
        print('La esfera diferente es C y es de mayor peso')
    else:
        print('La esfera diferente es C y es de menor peso')
elif A == C and A == D:
    if B > A:
        print('La esfera diferente es B y es de mayor peso')
    else:
        print('La esfera diferente es B y es de menor peso')
else:
    if A > B:
        print('La esfera diferente es A y es de mayor peso')
    else:
        print('La esfera diferente es A y es de menor peso')


