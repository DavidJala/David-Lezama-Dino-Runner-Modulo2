from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER_TYPE,HAMMER


class Hammer(PowerUp):
    def __init__(self):
        self.position_y = 310
        super().__init__(HAMMER, HAMMER_TYPE, self.position_y)