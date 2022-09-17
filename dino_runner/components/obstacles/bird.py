import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self,image) -> None:
        self.image = image
        self.type = random.randint(0,len(image)-1)
        super().__init__(image,obstacleType=self.type,name="bird")
        self.rect.y = 250
        self.step_index = 0
    
    def draw(self, screen):
        if self.step_index > 8:
            self.step_index = 0
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        screen.blit(self.image,self.rect)
        self.step_index += 1
