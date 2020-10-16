# Un crucero recibe viajeros que quieren dar la vuelta al mundo. El crucero, requiere de un programa que le permita analizar 
# el comportamiento de los viajeros. El programa debe permitir ingresar información para los 20 viajeros analizados y, para cada 
# viajero, debe pedir el nombre, sexo (hombreo mujer), estado civil (soltero, casado o viudo) y su edad. Diseñe un algoritmo que determine:

# 1.       El porcentaje de hombres solteros que están viajando con respecto al total de viajeros hombres.

# 2.       La edad promedio de hombres casados.

# 3.       El porcentaje de mujeres solteras respecto al total de personas solteras.

# 4.       El nombre de la persona con mayor edad.

cont_hombres = 0
cont_MS = 0
cont_MC = 0
edad_p = 0
cont_solteros = 0
cont_FS = 0
edad_Mayor = 0

for i in range(1,21):
    name = input(f"\nIngrese el nombre del viajero {i}: ")
    sexo = input(f"ingrese el sexo del viajero {i} (M/F): ")
    civil = input(f"ingrese el estado civil del viajero {1} (S/C/V): ")
    edad = int(input(f"Ingrese la edad del viajero {i}: "))

    if sexo == "M":
        cont_hombres = cont_hombres + 1
        if civil == "S":
            cont_MS = cont_MS + 1
        if civil == "C":
            cont_MC = cont_MC + 1
            edad_p = edad_p + edad

    if civil == "S":
        cont_solteros = cont_solteros + 1
        if sexo == "F":
            cont_FS = cont_FS + 1
    
    if edad > edad_Mayor:
        edad_Mayor = edad
        nombre = name


por_MS = (cont_MS/cont_hombres)*100
promedioMC = edad_p/cont_MC
por_FS = (cont_FS/cont_solteros)*100
print("\nEl porcentaje de hombres solteros que están viajando con respecto al total de viajeros hombres es:",por_MS)
print("La edad promedio de hombres casados es:",promedioMC)
print("El porcentaje de mujeres solteras respecto al total de personas solteras es:",por_FS)
print("El nombre de la persona con mayor edad es:",nombre)

#scrip resuelto por Jhan Carlos Galvis Sayas y Mariana Maldonado Betancur - Pensamiento Algoritmico - Grupo 406