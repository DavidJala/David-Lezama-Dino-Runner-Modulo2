import pygame


from dino_runner.components.dinosaour import Dinosaour
from dino_runner.components.obstacles.obstacleManger import ObstacleManager
from dino_runner.components.power_ups.PowerUpManager import PowerUpManager
from dino_runner.components.power_ups.shild import Shield
from dino_runner.utils.constants import (BG, DEATH_DINO, DEFAULT_TYPE, FONT_STYLE, FPS, GAME_OVER, HEART,
                                         ICON, SCREEN_HEIGHT, SCREEN_WIDTH,
                                         TITLE)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaour()
        self.shield = Shield()
        self.obstacles_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.score = 0            
        self.running = True
        self.death_count = 0
        self.best_score = 0
 
    def execute(self):
        while self.running:
                if not self.playing:
                    self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def reset_game(self):
        self.game_speed = 20
        self.score = 0
        self.playing = True

        self.obstacles_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        

    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacles_manager.update(game=self)
        self.power_up_manager.update(game=self,player=self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.draw_hearts()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.obstacles_manager.draw(screen=self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks() ) / 1000, 2)
            if time_to_show >= 0:
                self.print_on_screen(text=f'{self.player.type.capitalize()} enabled for {time_to_show} seconds',position_x=500,position_y=50,size_font=18)
            else :
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def print_on_screen(self,text,position_x,position_y,size_font):
        font = pygame.font.Font(FONT_STYLE,size_font)
        text =  font.render(text,True,(0,0,0))
        text_rec = text.get_rect()
        text_rec.center = (position_x,position_y)
        self.screen.blit(text,text_rec)

    def draw_score(self):
        self.print_on_screen(position_y=50,position_x=900,size_font=15,text=f'Best Score : {self.best_score}')
        self.print_on_screen(position_y=50,position_x=1050,size_font=15,text=f'Score : {self.score}')
    
    def draw_accout(self):
        pass

    def draw_hearts(self):
        self.screen.blit(HEART,(20,40)) 
        self.print_on_screen(text=f"{self.player.hearts}",position_x=60,position_y=50,size_font=20)

    def update_score(self):
            self.score += 1
            if self.score % 100 == 0 and self.game_speed < 2000:
               self.game_speed += 5
            if self.score > self.best_score:
                self.best_score = self.score

    def handler_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255,255,255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2 

        if self.death_count == 0:
            self.screen.blit(ICON, (half_screen_width-20, half_screen_height-150))
            self.print_on_screen(text='Press any Key to start',position_y=half_screen_height,position_x=half_screen_width,size_font=40)
        else :
            self.screen.blit(DEATH_DINO,(half_screen_width-80,half_screen_height))
            self.screen.blit(GAME_OVER,(half_screen_width-200,half_screen_height-100))
            self.print_on_screen(text=f"Score :  {self.score}",position_y=half_screen_height-30,position_x=half_screen_width,size_font=30)
            self.print_on_screen(text=f"Deaths : {self.death_count}",position_y=50,position_x=100,size_font=30)
            self.print_on_screen(text=f"Best score: {self.best_score}",position_y=50,position_x=SCREEN_WIDTH-150,size_font=30)

        pygame.display.update()
        pygame.display.flip()
        self.handler_events_on_menu()
