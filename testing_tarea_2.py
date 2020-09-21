def main():
    import random
    tecla = input(f"Ingrese cualquier tecla para inciar o @ para terminar: ")
    # Clientes=["Lina", "Ana", "Felipe", "Tola", "Carola", "Catalina", "Héctor", "Luis", "Lorena", "Tere", "Juan"]
    # DocId=["101710901", "101659391", "102716941", "1017406052", "101510302", "101314941", "101780988", "101315971", "101799909", "101510505"]
    totalClientes = 0
    # n = 0
    sumaResultados = 0
    # for n in range (1,11):
    #     datosClientes=Clientes[n] + DocId[n]

    while tecla != "@":
        Clientes=["Lina", "Ana", "Felipe", "Tola", "Carola", "Catalina", "Héctor", "Luis", "Lorena", "Tere", "Juan"]
        DocId=["101710901", "101659391", "102716941", "1017406052", "101510302", "101314941", "101780988", "101315971", "101799909", "101510505"]
        X = random.choice(Clientes)
        Y = random.choice(DocId)
        
        cantidadA = random.randint(1,100) #cantidad aleatoria
        precioA = random.randint(50000,90000) #precio aleatorio
        cantidadB = random.randint(1,100)
        precioB = random.randint(50000,90000)
        cantidadC = random.randint(1,100)
        precioC = random.randint(50000,90000)
        # ivaA = 6
        # ivaB = 10
        # ivaC = 12
        # descuentoA1 = 4/100
        # descuentoA1 = 8/100
        # descuentoA1 = 12/100
        # descuentoB1 = 5/100
        # descuentoB2 = 15/100
        # descuentoC1 = 10/100
        # descuentoC2 = 20/100
        # descuentoC3 = 30/100

        resultadoA = cantidadA * precioA
        totalIvaA = resultadoA * 6/100
        valorBrutoA = resultadoA + totalIvaA
        if cantidadA <= 20:
            descuentoTotalA = valorBrutoA * 4/100
        elif cantidadA > 20 and cantidadA < 30:
            descuentoTotalA = valorBrutoA * 8/100
        elif cantidadA > 30:
            descuentoTotalA = valorBrutoA * 12/100
        pagoNetoA = valorBrutoA - descuentoTotalA
        print("-----------------------------------------")
        print(f"Unidades del articulo A: {cantidadA}")
        print(f"Precio: {precioA}")
        print(f"Pago Neto A: {pagoNetoA}")
        print(f"Valor Bruto A: {valorBrutoA}")
        print(f"Descuento total A: {descuentoTotalA}")
        print(f"Total IVA A: {totalIvaA}")
        print("-----------------------------------------")

        resultadoB = cantidadB * precioB
        totalIvaB = resultadoB * 10/100
        valorBrutoB = resultadoB + totalIvaB
        if cantidadB < 36:
            descuentoTotalB = valorBrutoB * 5/100
        elif cantidadB >= 36:
            descuentoTotalB = valorBrutoB * 15/100
        pagoNetoB = valorBrutoB - descuentoTotalB
        print("------------------------------------------")
        print(f"Unidades del articulo B: {cantidadB}")
        print(f"Precio: {precioB}")
        print(f"pago Neto B: {pagoNetoB}")
        print(f"valor Bruto B: {valorBrutoB}")
        print(f"descuento Total B: {descuentoTotalB}")
        print(f"total Iva B: {totalIvaB}")
        print(f"-----------------------------------------")

        resultadoC = cantidadC + precioC
        totalIvaC = resultadoC * 12/100
        valorBrutoC = resultadoC + totalIvaC
        if cantidadC < 50:
            descuentoTotalC = valorBrutoC * 10/100
        elif cantidadC >= 50 and cantidadC < 100:
            descuentoTotalC = valorBrutoC * 20/100
        elif cantidadC >= 100:
            descuentoTotalC = valorBrutoC * 30/100
        pagoNetoC = valorBrutoC - descuentoTotalC
        print("-----------------------------------------")
        print("Articulo \t Precio($) \t Valor Bruto($) \t Total IVA($) \t Total descuento($) \t Pago neto($)")
        print(f"C                {precioC}            {valorBrutoC}                {totalIvaC}                {descuentoTotalC}                {pagoNetoC}")
        # print(f"Unidades del articulo C: {cantidadC}")
        # print(f"Precio: {precioC}")
        # print(f"Pago Neto C: {pagoNetoC}")
        # print(f"Valor Bruto C: {valorBrutoC}")
        # print(f"Descuento Total c: {descuentoTotalC}")
        # print(f"Total Iva C: {totalIvaC}")
        print("------------------------------------------")

        if cantidadA > 0 and cantidadB > 0 and cantidadC > 0:
            resultado = resultadoA + resultadoB + resultadoC
            resultado = resultado - (resultado * 6/100)
        else:
            resultado = resultadoA + resultadoB + resultadoC

        print(X+"",Y)
        print(f"Resultado: {resultado}")

        totalClientes = totalClientes + 1
        sumaResultados = sumaResultados + resultado

        tecla = input(f"Ingrese cualquier tecla para inciar o @ para terminar: ")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("-----------------------------------------")
    print(f"El total de personas que compraron en el madrugon fueron {totalClientes}")
    print(f"El total global de las ventas del madrugon fue {sumaResultados}")
    print("-----------------------------------------")
main()
