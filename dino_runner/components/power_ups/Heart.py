import random

from dino_runner.utils.constants import HEART, HEART_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Heart(PowerUp):
    def __init__(self):
        self.position_y = random.randint(280,310)
        super().__init__(HEART, HEART_TYPE,self.position_y)