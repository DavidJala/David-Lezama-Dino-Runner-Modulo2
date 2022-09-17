
import random

from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

class Shield(PowerUp):
    def __init__(self):
        self.position_y = random.randint(125,175)
        super().__init__(SHIELD, SHIELD_TYPE,self.position_y)