"""
    Modelar: un auto 

        atributos: 
            - una velocidad, al iniciar esta parado

        puede:
            - puede ver su velocidad
            - puede acelerar una determinada velocidad
            - puede detenerse 
            - pude saber si esta en movimiento
"""

class Auto(object):
    """ 
        Clase Auto
        
        Mensajes: 
            ✅ velocidad: devuelve la velocidad del auto
            ✅ acelerar(una_velocidad): incrementar la velocidad
            ✅ deterner: pone la velocidad en 0
            ✅ enMovimiento: responde True si esta en moviento
    """
    def __init__(self) -> None:
        self.__velocidad = 0
        
    @property
    def velocidad(self): return self.__velocidad
    
    @velocidad.setter
    def velocidad(self, una_velocidad): 
        self.__velocidad = una_velocidad
        
    def acelerar(self, una_velocidad: int) -> None:
        """ Incrementa la velocidad del auto """
        self.velocidad += una_velocidad
    
    def detener(self) -> None:
        """ Vuelve a 0 la velocidad """
        self.velocidad = 0

    def enMovimiento(self) -> bool:
        """ responde True si esta en moviento """
        return self.velocidad > 0 
       
        
        
    
        
    


if __name__ == '__main__':
    pass
    # auto1 = Auto()
    
    # print(auto1.velocidad)
    
    # auto1.acelerar(100)
        
    # print(auto1.velocidad)
