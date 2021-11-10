import unittest
from auto import Auto

class TestAuto(unittest.TestCase):
    def setUp(self) -> None:
        self.auto = Auto()
    
    def test_alInstanciarUnAutoSuVelocidadEsCero(self):
        """ Cuando se instancia un auto su velocidad es cero """
        # setup
        # auto = Auto()
        
        # precondición ? opcional 
        # ---- No tiene
        
        # Ejercitación del comportamiento  Post condición - Objetivo
        self.assertEqual(self.auto.velocidad, 0)
        
    def test_elAutoPuedeAcelerar(self):
        """ El auto puede variar la velocidad  """
        # setup
        # auto = Auto()

        # precondicion 
        self.assertEqual(self.auto.velocidad, 0)

        # Ejercitacion 
        self.auto.acelerar(20)
        
        # post condicion
        self.assertEqual(self.auto.velocidad, 20)   

    def test_elAutoFrenaYVuelveAVelocidadCero(self):
        """ El auto vuelve a la velocidad 0 """
        # auto = Auto()        
        self.auto.acelerar(20)
        
        self.assertEqual(self.auto.velocidad, 20)

        self.auto.detener()

        self.assertEqual(self.auto.velocidad, 0)

    
    def test_elAutoEstaEnMovimiento(self):
        """ El auto esta en movimiento si la velocidad es mayor que 0 """
        self.auto.acelerar(1)

        self.assertTrue(self.auto.enMovimiento())
        
        
    def test_elAutoPorDefectoNoEstaEnMovimiento(self):
        """ Al instanciar un auto este no se encuentra en movimiento """ 
        self.assertFalse(self.auto.enMovimiento())

        
    


# Runner
if __name__ == '__main__':
    unittest.main()