import unittest
import pygame
from waltsadventure import Player  

class TestYourClass(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.x = 100
        self.y = 100
        self.instance = YourClass(self.x, self.y)
        
    def test_update(self):
        
        self.instance.update(0)
       
        self.assertEqual(self.instance.rect.x, self.x)
        self.assertEqual(self.instance.rect.y, self.y)
      
        with self.assertRaises(pygame.sprite.Sprite):
            self.instance.update(-1)
           
        with self.assertRaises(pygame.sprite.Sprite):
            self.instance.update(-2)

   
    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
