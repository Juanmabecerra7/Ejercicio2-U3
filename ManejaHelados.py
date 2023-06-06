from Helados import Helado
from ManejaSabores import ManejaSabor

class ManejaHelados:
    def __init__ (self):
        self.__lista = []
        
    def agegarHelado (self, unHelado):
        self.__lista.append(unHelado)
        
    def cargar (self, MS):
        gramos = float(input("ingrese los gramos de helado: "))
        precio = float(input("inrese el precio del Helado: "))
        cantidad = int(input("ingrese la cantidad de Sabores: "))
        sabor = input("ingrese un sabor: ")
        unSabor = MS.buscarSabor(sabor)
        indice = 1
        unHelado = Helado(gramos, precio, unSabor, cantidad)
        while indice < cantidad:
            sabor = input("Ingrese un sabor: ")
            unSabor = ManejaSabor.buscarSabor (sabor)
            unHelado.addSabor(unSabor)
            indice += 1
        self.agegarHelado(unHelado)

    def __str__(self):
        indice = 0
        s = ""
        while indice < len(self.__lista):
            s += str(self.__lista[indice]) + "\n"
            indice += 1
        return s 
    
    def buscarSabor(self, nombre):
        indice = 0
        total = 0
        while indice < len(self.__lista):
            total += Helado.getNombreSabor(self.__lista[indice], nombre, total)
            indice += 1
        print(f"El total de Gramos es de: {total}")

    def punto4(self, tipo):
        indice  = 0
        cadena = ""
        while indice < len(self.__lista):
            if tipo == Helado.getGramos(self.__lista[indice]):
                cadena = Helado.mostrarSabores(self.__lista[indice], cadena)
            indice += 1
        print(f"Los sabores son:")
        print(cadena)

    def  importeTotal(self):
        indice = 0
        total= 0
        total1= 0
        total2= 0
        total3= 0
        total4 = 0
        while indice < len(self.__lista):
            if 100 == Helado.getGramos(self.__lista[indice]):
                total += Helado.getPrecio(self.__lista[indice])
            elif 150 == Helado.getGramos(self.__lista[indice]):
                total1 += Helado.getPrecio(self.__lista[indice])
            elif 250 == Helado.getGramos(self.__lista[indice]):
                total2 += Helado.getPrecio(self.__lista[indice])
            elif 500 == Helado.getGramos(self.__lista[indice]):
                total3 += Helado.getPrecio(self.__lista[indice])
            elif 1000 == Helado.getGramos(self.__lista[indice]):
                total4 += Helado.getPrecio(self.__lista[indice])
            indice += 1
        print(f"El total para los 100gr es de: {total}")
        print(f"El total para 150gr es de: {total1}")
        print(f"El total para 250gr es de: {total2}")
        print(f"El total para 500gr es de: {total3}")
        print(f"El total para 100gr es de: {total4}")
    
