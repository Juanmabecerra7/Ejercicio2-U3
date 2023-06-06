class Sabor:
    __idSabor = int
    __ingredientes = str
    __nombreSabor = str
    
    def __init__ (self,idSabor,ingredientes,nombreSabor):
        self.__idSabor = idSabor
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombreSabor
    
    def getNombre (self):
        return str(self.__nombreSabor)
    
    def __str__(self):
        cadena = f"Nombre: {self.__nombreSabor}"+"\n"
        cadena += f"IdSabor: {self.__idSabor}"+" "+f"Ingredientes: {self.__ingredientes}"
        return cadena
