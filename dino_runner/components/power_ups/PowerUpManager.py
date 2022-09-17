import  random
import  pygame
from dino_runner.components.power_ups.Hammer import Hammer

from dino_runner.components.power_ups.Heart import Heart
from dino_runner.components.power_ups.shild import Shield
from dino_runner.utils.constants import HEART_TYPE, SHIELD_TYPE


class PowerUpManager:
        def __init__(self) -> None:
            self.power_ups = [] 
            self.when_appears = 0
            self.duration = random.randint(3,6)

        def generate_power_up(self,score):
            shield = Shield()
            heart = Heart()
            hammer = Hammer()

            power_ups_to_render = [heart,shield,hammer]
        
            length_powers = len(power_ups_to_render)-1
            random_power_up = random.randint(0,length_powers)

            if len(self.power_ups) == 0 and self.when_appears == score:
                self.when_appears += random.randint(100,150)
                self.power_ups.append(power_ups_to_render[random_power_up])

        def update(self,game,player):
            self.generate_power_up(score=game.score)
            for power_up in self.power_ups: 
                power_up.update(game.game_speed,self.power_ups)
                if game.player.dino_rect.colliderect(power_up.rect):
                    if power_up.type == SHIELD_TYPE:
                        power_up.start_time = pygame.time.get_ticks()
                        game.player.has_power_up = True
                        game.player.type = power_up.type
                        game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                        self.power_ups.remove(power_up)
                    elif power_up.type == HEART_TYPE:
                        game.player.hearts = game.player.hearts + 2
                        self.power_ups.remove(power_up)
                    else:
                        game.player.type = power_up.type
                        self.power_ups.remove(power_up)
                        game.player.attacks = game.player.attacks + 3 

        def reset_power_ups(self):
            self.power_ups = []
            self.when_appears  = random.randint(100,150)

        def draw(self,screen):
            for power_up in self.power_ups:
                power_up.draw(screen)