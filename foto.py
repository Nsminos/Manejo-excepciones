from error import DimensionError
class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        self.__ancho = ancho
        if ancho <1 or ancho > 2500:
            raise DimensionError(f"El ancho debe ser mayor que 0 y menor de 2500", ancho, 2500)
    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        self.__alto = alto
        if alto <1 or alto > 2500:
            raise DimensionError(f"El alto debe ser mayor que 0 y menor de 2500", alto, 2500)
        
f = Foto(0,0,"cambio")
f.ancho = 2501

