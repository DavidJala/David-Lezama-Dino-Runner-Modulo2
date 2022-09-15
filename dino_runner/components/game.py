import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,FONT_STYLE
from dino_runner.components.dinosaour import Dinosaour
from dino_runner.components.obstacles.obstacleManger import ObstacleManager

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
        self.obstacles_manager = ObstacleManager()
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

    def run(self):
        # Game loop: events - update - draw
        self.obstacles_manager.reset_obstacles()
        self.playing = True
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

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacles_manager.draw(screen=self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def print_on_screen(self,text,width,height,size_font):
        font = pygame.font.Font(FONT_STYLE,size_font)
        text =  font.render(text,True,(0,0,0))
        text_rec = text.get_rect()
        text_rec.center = (width,height)
        self.screen.blit(text,text_rec)

    def draw_score(self):
        self.print_on_screen(height=50,text=f'Best Points {self.best_score}',width=950,size_font=10)
        self.print_on_screen(height=50,text=f'Points {self.score}',width=1050,size_font=10)

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
                self.game_speed = 20
                self.score = 0
                self.run()

    def show_menu(self):
        self.screen.fill((255,255,255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2 
        if self.death_count == 0:
            self.print_on_screen(text='Press any Key to start',height=half_screen_height,width=half_screen_width,size_font=40)
        else :
            self.print_on_screen(text="Game Over",height=half_screen_height-60,width=half_screen_width,size_font=40)
            self.print_on_screen(text=f"- Your Deaths : {self.death_count}",height=half_screen_height-20,width=half_screen_width,size_font=20)
            self.print_on_screen(text=f"- Your current socre :  {self.score}",height=half_screen_height,width=half_screen_width,size_font=20)
            self.print_on_screen(text=f"-------------------------------------",height=half_screen_height+20,width=half_screen_width,size_font=20)
            self.print_on_screen(text=f"- Your best_score: {self.best_score}",height=half_screen_height+40,width=half_screen_width,size_font=20)
        pygame.display.update()
        pygame.display.flip()
        self.handler_events_on_menu()