import pygame
import random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import CactusSmall, CactusLarge
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS,BIRD



class ObstacleManager:
    def __init__(self) -> None:
        self.obstacles = []
    
    def generate_obstacles(self) -> None:
        bird = Bird(image=BIRD)
        cactusSmall = CactusSmall(SMALL_CACTUS)
        cactusLarge = CactusLarge(LARGE_CACTUS)
        
        obstacles_to_render = [cactusSmall,cactusLarge,bird]
        
        length_obstacles = len(obstacles_to_render)-1
        random_obstcle = random.randint(0,length_obstacles)

        self.obstacles.append(obstacles_to_render[random_obstcle])

    def update(self,game) -> None:
        if len(self.obstacles) == 0:
            self.generate_obstacles()
        
        for obstacle in self.obstacles:
            self.collision(game=game,obstacle=obstacle)
                
    def collision(self,obstacle,game)-> None:
        obstacle.update(game.game_speed,self.obstacles)
        if game.player.dino_rect.colliderect(obstacle.rect):
            pygame.time.delay(1000)
            print("F Dinosour dead ")
            game.playing = False

            
    def draw(self,screen) -> None:
        for obstacle in self.obstacles:
            obstacle.draw(screen)

