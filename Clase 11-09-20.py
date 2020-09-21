# Imprimir el promedio de una lista de 100 números.

suma = 0
for i in range (1,101):
    print(i)
    suma += i
print(suma)
print(i)
promedio = suma/i
print("El promedio es:", promedio)

# suma = 0
# for i in range (1,102):
#     suma += i
# promedio = suma/i
# print("El promedio es:", promedio)

# N1 = int(input("Ingrese un valor: "))
# N2 = int(input("Ingrese otro valor: "))
# suma = 0
# cont = 0
# for i in range (N1,N2+1):
#     suma += i
#     cont += 1
# promedio = suma/cont
# print("El promedio es:", promedio)

# numero primo

# num = int(input("Ingrese un numero: "))
# cont = 0
# for i in range (1,num+1):
#     if num % i == 0:
#         cont += 1
# if cont > 2:
#     print("El numero no es primo")
# else:
#     print("El numero es primo")