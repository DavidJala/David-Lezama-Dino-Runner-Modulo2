import pygame 


from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite

class PowerUp(Sprite):
    def __init__(self, image, type,position_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = position_y

        self.start_time = 0
        self.width = self.image.get_width()

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)