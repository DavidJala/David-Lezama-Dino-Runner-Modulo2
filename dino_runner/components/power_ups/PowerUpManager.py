import  random
import  pygame

from dino_runner.components.power_ups.shild import Shield



class PowerUpManager:
        def __init__(self) -> None:
            self.power_ups = [] 
            self.when_appears = 0
            self.duration = random.randint(3,6)

        def generate_power_up(self,score):
            shield = Shield()
            if len(self.power_ups) == 0 and self.when_appears == score:
                self.when_appears += random.randint(200,300)
                self.power_ups.append(shield)

        def update(self,game,player):
            self.generate_power_up(score=game.score)
            for power_up in self.power_ups: 
                power_up.update(game.game_speed,self.power_ups)
                if game.player.dino_rect.colliderect(power_up.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.type = power_up.type
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)

        def reset_power_ups(self):
            self.power_ups = []
            self.when_appears  = random.randint(100,110)

        def draw(self,screen):
            for power_up in self.power_ups:
                power_up.draw(screen)