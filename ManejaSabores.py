from Sabor import Sabor
import numpy as np
import csv

class ManejaSabor:
    __dimension = 0
    __cantidad = 0
    __incremento = 5
    
    def __init__(self,dimension,incremento=5):
        self.__sabor = np.empty (dimension,dtype=Sabor)
        self.__dimension=dimension
        self.__cantidad=0
        
    def agregarSabor (self, unSabor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__sabor.resize(self.__dimension)
        self.__sabor[self.__cantidad] = unSabor
        self.__cantidad += 1
        
    def test (self):
        file = open("sabores.csv")
        reader = csv.reader(file,delimiter=",")
        for fila in reader:
            idSabor = fila[0]
            ingredientes = fila[1]
            nombreSabor = fila[2]
            unSabor = Sabor(idSabor, ingredientes, nombreSabor)
            self.agregarSabor(unSabor)
        file.close()
        
    def __str__ (self):
        indice = 0
        s = ""
        while indice < self.__cantidad:
            s += str(self.__sabor[indice]) + "\n"
            indice += 1
        return s
    
    def buscarSabor(self, sabor):
        indice = 0
        bandera = False
        while bandera ==False and indice < self.__cantidad:
            if str(sabor) in Sabor.getNombre(self.__sabor[indice]):
                print("Se encontro")
                unSabor = self.__sabor[indice]
                bandera = False
            indice += 1
        return unSabor
