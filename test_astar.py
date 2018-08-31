import unittest
from random import randint
from a_star import Area, a_star

class AstarTest(unittest.TestCase):
    def setUp(self):
        x = randint(2,31)
        y = randint(2,31)

        self.matriz = (x,y)
        self.origem = (randint(0, x), randint(0, y))
        self.destino = (randint(0, x), randint(0, y))
        
    
    def tearDown(self):
        print(self.matriz, self.origem, self.destino)


    def testArea(self):
        self.area = Area(self.origem, self.destino, self.matriz)

        self.assertEqual(self.origem, self.area.origem)


    def test_a_star(self):
        self.area = Area(self.origem, self.destino, self.matriz)
        self.assertNotEqual('Não foi possível encontrar a rota!',a_star(self.area))


if __name__ == '__main__':
        unittest.main()
