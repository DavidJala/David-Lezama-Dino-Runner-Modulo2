import pygame
import random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, SHIELD_TYPE



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
                if game.player.type != SHIELD_TYPE:
                    pygame.time.delay(1000)
                    game.death_count += 1
                    game.playing = False
                    break
                else :
                    self.obstacles.remove(obstacle)
            # self.collision(game=game,obstacle=obstacle)
                
    # def collision(self,obstacle,game)-> None:
    #     obstacle.update(game.game_speed,self.obstacles)
    #     if game.player.dino_rect.colliderect(obstacle.rect):
    #         if game.player.type != SHIELD_TYPE:
    #             pygame.time.delay(1000)
    #             game.death_count += 1 
    #             game.playing = False
    #         else:
    #             self.obstacles.remove(obstacle)

            
    def draw(self,screen) -> None:
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []
            
            
            
            
            
            
            

