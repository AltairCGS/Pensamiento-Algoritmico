"""
n = int(input("Ingrese el numero de dias a analizar del mes: "))
precio_min = 999999999999999
precio_max = 0
mayor_var = 0
for i in range(1,n+1):
    valor_min = float(input(f"Ingresa el valor minimo del dia {i}: "))
    valor_max = float(input(f"Ingresa el valor maximo del dia {i}: "))
    if valor_min < precio_min:
        precio_min = valor_min
    if valor_max > precio_max:
        precio_max = valor_max
    var = valor_max - valor_min
    if var > mayor_var:
        mayor_var = var
        dia = i
print("El precio minimo de nogociacion del cafe fue de",precio_min)
print("El precio maximo de nogociacion del cafe fue de",precio_max)
print("El día en que se presento la mayor variabilidad fue el dia",dia)
"""
#------------------
"""
n = int(input("Ingresa el numero de encuestas a realizar: "))
cont_si = 0
cont_no = 0
cont_in = 0
cont_joven = 0
cont_adulto = 0
cont_mayor = 0
cont_bogota = 0
cont_medellin = 0
cont_cali = 0
for i in range(1,n+1):
    CC = input("Ingresa numero de cedula de ciudadania: ")
    Genero = input("Ingresa tu genero (M o F): ")
    Ciudad = input("Ingresa tu ciudad de residencia (B, M o C): ")
    Edad = int(input("Ingresa tu edad: "))
    Encuesta = input("¿Esta de acuerdo con el proceso de paz? S/N/I: ")
    if Encuesta == "S":
        cont_si += 1
        if Edad <= 30:
            cont_joven += 1
        elif Edad <= 60:
            cont_adulto += 1
        else:
            cont_mayor += 1
    elif Encuesta == "N":
        cont_no += 1
        if Ciudad == "B":
            cont_bogota += 1
        elif Ciudad == "M":
            cont_medellin += 1
        else:
            cont_cali += 1
    else:
        cont_in += 1
print("\nLa cantidad de ciudadanos que votaron que Si es:",cont_si)
print("La cantidad de ciudadanos que votaron que No es:",cont_no)
print("La cantidad de ciudadanos que votaron indiferente es:",cont_in)
if cont_joven > cont_adulto and cont_joven > cont_mayor:
    print("\nLos jovenes arrojan mayor aceptacion al proceso de paz")
elif cont_adulto > cont_joven and cont_adulto > cont_mayor:
    print("\nLos adultos arrojan mayor aceptacion al proceso de paz")
else:
    print("\nLos mayores arrojan meyor aceptacion al proceso de paz")
if cont_bogota > cont_medellin and cont_bogota > cont_cali:
    print("\nLa ciudad que arroja la menor aceptacion al proceso de paz es Bogota")
elif cont_medellin > cont_bogota and cont_medellin > cont_cali:
    print("\nLa ciudad que arroja la menor aceptacion al proceso de paz es Medellin")
else:
    print("\nLa ciudad que arroja la menor aceptacion al proceso de paz es Cali")
por_si = (cont_si/n)*100
por_no = (cont_no/n)*100
por_in = (cont_in/n)*100
print("\nEl porcentaje de ciudadanos que votaron Si es:",por_si)
print("El porcentaje de ciudadanos que votaron No es:",por_no)
print("El porcentaje de ciudadanos que votaron Indiferente es:",por_in)
"""
#--------------------------
"""
n = int(input("Ingrese el numero de sismos en el año: "))
num_n = 0
num_s = 0
num_c = 0
cont_in = 0
cont_is = 0
cont_ic = 0
suma_intensidades = 0
Mayor_sismo = 0
menor_ph = 999999999999999999999999999999
mayor_pm = 0
for i in range(1,n+1):
    zona = input(f"Ingrese la zona del continente donde se presento el sismo numero {i} (N, S, C): ")
    intensidad = float(input("Ingresa la intensidad del terremoto en escala del 1 al 10: "))
    per_hum = int(input("Ingrese el numero de personas fallesidas: "))
    per_mat = float(input("Ingrese perdidas materiales evaluadas en USD: "))
    suma_intensidades += intensidad
    if zona == "N":
        num_n += 1
        cont_in += intensidad
    elif zona == "S":
        num_s += 1
        cont_is += intensidad
    else:
        num_c += 1
        cont_ic += intensidad
    if intensidad > Mayor_sismo:
        Mayor_sismo = intensidad
        sismo_mayor = i
    if per_hum < menor_ph:
        menor_ph = per_hum
        sismo_menor_ph = i
    if per_mat > mayor_pm:
        mayor_pm = per_mat
        sismo_mayor_pm = i
Prom_N = cont_in/num_n
Prom_S = cont_is/num_s
Prom_C = cont_ic/num_c
Prom_General = suma_intensidades/n
print("\nEl promedio de la intensidad de sismos en la zona Norte es de:",Prom_N)
print("El promedio de la intensidad de sismos en la zona Sur es de:",Prom_S)
print("El promedio de la intensidad de sismos en la zona Central es de:",Prom_C)
print("El promedio de la intensidad de los sismos en todo el continente es de:",Prom_General)
if num_n > num_s and num_n > num_c:
    print("\nEn la zona norte se presentaron mas sismos")
elif num_s > num_n and num_s > num_c:
    print("\nEn la zona sur se presentaron mas sismos")
else:
    print("\nEn la zona central se presentaron mas sismos")
print("\nEl sismo de mayor intensidad fue el sismo numero",sismo_mayor)
print("El sismo que causo menores perdidas humanas fue el sismo numero",sismo_menor_ph)
print("El sismo que causo meyores perdidas materiales fue el sismo numero:",sismo_mayor_pm)
"""