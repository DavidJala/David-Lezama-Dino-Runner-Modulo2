import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS,SMALL_CACTUS
"""
class CactusSmall(Obstacle):
        def __init__(self, image) -> None:
                # self.type = random.randint(0,2)
                self.type = random.randint(0,len(image)-1)
                super().__init__(image, obstacleType=self.type)
                self.rect.y = 325

class CactusLarge(Obstacle):
        def __init__(self, image) -> None:
                self.type = random.randint(0,len(image)-1)
                super().__init__(image, obstacleType=self.type)            
                self.rect.y = 300
"""
class Cactus(Obstacle):
        def __init__(self, cactusType) -> None:
                self.cactus = {
                        "small": [SMALL_CACTUS,325],
                        "large": [LARGE_CACTUS,300]
                }
                image,cactus_pos = self.cactus[cactusType]
                self.type = random.randint(0,2)
                super().__init__(image, obstacleType=self.type)
                self.rect.y = cactus_pos                 
                