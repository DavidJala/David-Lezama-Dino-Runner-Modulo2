import pygame
import random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, HAMMER_TYPE, NAME_BIRD, SHIELD_TYPE



class ObstacleManager:
    def __init__(self) -> None:
        self.obstacles = []
    
    def generate_obstacles(self) -> None:
        bird = Bird(image=BIRD)
        cactusSmall = Cactus(cactusType='small')
        cactusLarge = Cactus(cactusType='large')
        
        obstacles_to_render = [cactusSmall,cactusLarge,bird]
        
        length_obstacles = len(obstacles_to_render)-1
        random_obstcle = random.randint(0,length_obstacles)

        self.obstacles.append(obstacles_to_render[random_obstcle])

    def update(self,game) -> None:
        if len(self.obstacles) == 0:
            self.generate_obstacles()
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type == SHIELD_TYPE:
                    self.obstacles.remove(obstacle)
                    break
                if game.player.type == HAMMER_TYPE:
                    if game.player.attacks <= 0:
                        self.death_dino(game,obstacle)
                        break
                    else:
                        if obstacle.name != NAME_BIRD:
                            self.obstacles.remove(obstacle)
                            game.player.attacks = game.player.attacks - 1 
                        else: 
                            self.death_dino(game,obstacle)
                        break
                self.death_dino(game=game,obstacle=obstacle)
                
              
              
    def death_dino(self,game,obstacle):
                if game.player.hearts == 1:
                    pygame.time.delay(1000)
                    game.death_count += 1
                    game.playing = False
                else:
                    game.player.hearts = game.player.hearts - 1 
                    self.obstacles.remove(obstacle)
    
   


            
    def draw(self,screen) -> None:
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []
            
            
            
            
            
            
            

