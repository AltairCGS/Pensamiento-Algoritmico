"""
num_integrantes = 0
cont_M = 0
cont_F = 0
cont_personas = 0
cont_menores = 0
menor_armas = 9999999999999999999999999
for i in range(1,5):
    num_in = int(input(f"\nIngrese el numero de integrantes concentrados en la zona {i}: "))
    can_M = int(input(f"Ingrese la cantidad de hombres en la zona {i}: "))
    can_F = int(input(f"Ingrese la cantidad de mujeres en la zona {i}: "))
    can_men = int(input(f"Ingrese la cantidad de menores en la zona {i}: "))
    num_armas = int(input(f"Ingrese el numero de armas que se van a entregar en la zona {i}: "))

    if num_in > num_integrantes:
        num_integrantes = num_in
        zona = i
    
    cont_M = cont_M + can_M
    cont_F = cont_F + can_F
    cont_personas = cont_personas + num_in

    cont_menores = cont_menores + can_men

    if num_armas < menor_armas:
        menor_armas = num_armas
        zona_armas = i

print("\nLa zona con mayor concentracion de integrantes es la zona",zona)
if cont_M > cont_F:
    print("Hay mayor concentracion de hombres en el total de zonas")
else:
    print("Hay mayor concentracion de mujeres en el total de zonas")

porcetanje_hombres = (cont_M/cont_personas)*100
porcetanje_mujeres = (cont_F/cont_personas)*100
if porcetanje_hombres > porcetanje_mujeres:
    print("El porcentaje mayor respecto a los insurgentes es:",porcetanje_hombres,"y es de los hombres")
else:
    print("El porcentaje mayor respecto a los insurgentes es:",porcetanje_mujeres,"y es de las mujeres")

print("El total de menores que hacen parte de las filas de los insurgentes es de:",cont_menores)

print("La zona que entrega el menor numero de armas es la zona", zona_armas)
"""
"""
cont_sedes = 0
poblacion_pig = 0
num_menor_adultos = 999999999999999999999999
acumulador_monto_sedes = 0
cont_sedes_mayor_hembras = 0
acumulador_pig = 0
total_adultos = 0
poblacion_total = 0
for i in range(1,5):
    name = input(f"Ingrese el nombre de la sede {i}: ")
    num_machos_a = int(input(f"Ingrese el numero de machos adultos de la sede {name}: "))
    num_hembras_a = int(input(f"Ingrese el numero de hembras adultas de la sede {name}: "))
    pig_menores = int(input(f"Ingrese el numero de cerditos menores a 6 meses de la sede {i}: "))
    mont_dinero = float(input(f"Ingrese el monto de dinero por la ventas de la sede {name}: "))

    poblacion_pig = poblacion_pig + num_machos_a + num_hembras_a + pig_menores
    if poblacion_pig > 1000:
        poblacion_pig = 0
        if mont_dinero < 250000000:
            cont_sedes = cont_sedes + 1
    else:
        poblacion_pig = 0

    total_adultos = total_adultos + num_machos_a + num_hembras_a
    if total_adultos < num_menor_adultos:
        num_menor_adultos = total_adultos
        sede_menor_adultos = name
        total_adultos = 0
    else:
        total_adultos = 0

    if num_hembras_a > num_machos_a:
        acumulador_monto_sedes = acumulador_monto_sedes + mont_dinero
        cont_sedes_mayor_hembras = cont_sedes_mayor_hembras + 1
    
    acumulador_pig = acumulador_pig + pig_menores
    poblacion_total = poblacion_total + num_machos_a + num_hembras_a + pig_menores

print("La cantidad de sedes que tienen una poblacion mayor a 1000 cerdos pero que tienen ventas anuales menores a 250´000.000 son",cont_sedes,"sedes")
print("La sede que tiene menor numero de animales adultos es la sede",sede_menor_adultos)
Promedio = acumulador_monto_sedes/cont_sedes
print("El promedio de ventas anuales para las sedes que tienen mas hembras que machos es:",Promedio)
porcentaje = (acumulador_pig/poblacion_total)*100
print("El porcentaje total de cerdos con menos de 6 meses con respecto a la poblacion total es:",porcentaje)
"""