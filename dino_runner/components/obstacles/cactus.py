import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
        def __init__(self, image) -> None:
                self.type = random.randint(0,len(image)-1)
                super().__init__(image, obstacleType=self.type)
                self.rect.y = 325
                
                

class CactusLarge(Obstacle):
        def __init__(self, image) -> None:
                self.type = random.randint(0,len(image)-1)
                super().__init__(image, obstacleType=self.type)            
                self.rect.y = 300