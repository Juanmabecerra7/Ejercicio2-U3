from ManejaSabores import ManejaSabor
from ManejaHelados import ManejaHelados
if __name__=="__main__":
    MS = ManejaSabor(3)
    MH =ManejaHelados()
    MS.test()
    print(str(MS))
    while 1 != 0:
        print("1: Registrar un Helado")
        print("2: Mostrar los 5 sabores mas vendidos")
        print("3: Segun el nombre de un sabor estimar el total de gramos vendidos")
        print("4: Segun un tipo de Helado, mostrar los sabores mas vendidos")
        print("5: Para cada tipo de Helado mostrar el total de importe recaudado")
        print("6: Salir")
        opcion = int(input("Ingrese la opcion deseada: "))
        if opcion == 1:
            MH.cargar(MS)
        elif opcion == 2:
            pass
        elif opcion == 3:
            nombre =input("Ingrese el nombre del sabor: ")
            MH.buscarSabor(nombre)
        elif opcion == 4:
            tipo = float(input("Ingrese el tipo de Helado: 100gr, 150gr, 250gr, 500gr, 1000gr "))
            MH.punto4(tipo)
        elif opcion == 5:
            MH.importeTotal()
        elif opcion == 6:
            exit()
        else:
            print("Opcion Incorrecta")
