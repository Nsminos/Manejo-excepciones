class Error(Exception):
    pass
class DimensionError(Error):
    def __init__(self, mensaje:str, dimension:int = None, maximo:int =None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            ret = f"{self.mensaje}"
            
            if self.dimension != None:
                ret += f" Dimension ingresado: {self.dimension}"

            if self.maximo != None:
                ret += f" Dimension maxima es {self.maximo} permitida"

            return ret

