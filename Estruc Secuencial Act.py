#.Determine la temperatura en grados Fahrenheit a partir del valor en grados
#centígrados. Dado por la siguiente ecuación:

"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
Cent = int(input("\nIngrese los grados Centigrados a convertir en grados Fahrenheit: "))
Faren = (Cent * 9/5) + 32
(print("\nSon",int(Faren),"grados Fahrenheit "))
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)

#Se posee un monto de dinero de $120, se gasta en supermercado $49,5 y
#luego en verdulería12,10. Mostrar el saldo.

"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
Saldo_Inicial = 120
Mercado = Saldo_Inicial - 49.5 - 12.10
print("El saldo final es: ",Mercado)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)

#Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre
#su salario anterior.

"""#(<-Quitar triples comillas para comprobar el algoritmo)
#-----------------------------------------
Salario_Inicial = int(input("\nTendras un aumento del 25% en tu salario, ingresa tu salario actual: "))
Nuevo_Salario = (125 * Salario_Inicial) / 100
print("\nSu nuevo salario es de:",Nuevo_Salario)
#-----------------------------------------
"""#(<-Quitar triples comillas para comprobar el algoritmo)

#Una institución educativa ha recibido una donación especial que será
#repartida entre las carreras de telecomunicaciones, sistemas, administración
#y contabilidad de la siguiente forma:
#Telecomunicaciones: 20% de sistemas
#Sistemas: 15% de administración
#Administración: 30% de la donación
#Diseñe un algoritmo que determine cuanto recibirá cada carrera. 
"""
print("\nDeterminare el valor de la donacion como un valor definido, el cual sera: 20 millones de pesos\n")
Donacion = 20000000
Por_Admin = Donacion * 0.30
Por_Sistemas = Por_Admin * 0.15
Por_Teleco = Por_Sistemas * 0.20

PorFinal_Admin = Por_Admin * 0.85
PorFinal_Sistemas = Por_Sistemas * 0.80
print("Administracion recibira:",PorFinal_Admin)
print("Sistemas recibira:",PorFinal_Sistemas)
print("Telecomunicacion recibira:",Por_Teleco)
"""

HorasLab = int(input("Ingrese las horas laboradas: "))
Pago = HorasLab * 22200
Pago_semanal = (90 * Pago)/100
print(Pago_semanal)