from Sabor import Sabor
class Helado:
    __gramos =float
    __precio = float
    __sabor = list
    
    
    def __init__(self,gramos,precio,Sabor):
        self.__gramos=gramos
        self.__precio=precio
        self.__sabor=[]
        if Sabor != None:
            self.addSabor(Sabor)
            
    def getGramos(self):
        return self.__gramos

    def getPrecio(self):
        return self.__precio
    
    def addSabor(self, sabor):
        self.__sabor.append(sabor)

    def __str__(self):
        cadena = f"Gramos: {self.__gramos}, Precio: {self.__precio}"+"\n"
        for Sabor in self.__sabor:
            cadena += f"Sabor: {Sabor.getNombre()}"+"\n"
        return cadena
    
    def getNombreSabor(self, nombre, total):
        for Sabor in self.__sabor:
            sabor = Sabor.getNombre()
            if nombre in sabor:
                total = self.__gramos + total
        return total
    
    def mostrarSabores(self, cadena):
        for Sabor in self.__sabor:
            if not Sabor.getNombre() in cadena:
                cadena += Sabor.getNombre()+"\n"
        return cadena
