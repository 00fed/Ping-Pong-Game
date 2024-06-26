import pygame,sys, random
from pygame.math import Vector2

class Rackets:
   def __init__(self):
      self.pos1 = Vector2(1,cell_number/2-2) 
      self.pos2 = Vector2(cell_number-2,cell_number/2-2)
      self.racketspeed = 0.5
      self.y = random.choice([0.85,0.86,0.87,0.88,0.89,0.9])
   def draw_racket(self):
        racket_rect1 = pygame.Rect(int(self.pos1.x * cell_size), int(self.pos1.y * cell_size), cell_size, cell_size * 4)
        pygame.draw.rect(screen, (255,255,255), racket_rect1)
        racket_rect2 = pygame.Rect(int(self.pos2.x * cell_size), int(self.pos2.y * cell_size), cell_size, cell_size * 4)
        pygame.draw.rect(screen, (255,255,255), racket_rect2)
   def move_racket1(self):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_w] and self.pos1.y > 0:
         self.pos1.y -= self.racketspeed
      elif keys[pygame.K_s] and self.pos1.y < cell_number - 4: 
         self.pos1.y += self.racketspeed
   def move_racket2(self):
      #keys = pygame.key.get_pressed()
      #if keys[pygame.K_w] and self.pos1.y > 0:
       #  self.pos1.y -= self.racketspeed
      #elif keys[pygame.K_s] and self.pos1.y < cell_number - 4:
       #  self.pos1.y += self.racketspeed
          
          self.pos2 = Vector2(cell_number-2 , main.ball.pos.y * self.y)
   def reset_rackets(self):
      self.pos1 = Vector2(1,cell_number/2-2) 
      self.pos2 = Vector2(cell_number-2,cell_number/2-2)
      self.racketspeed = 0.5
      self.y = random.choice([0.85,0.86,0.87,0.88,0.89,0.9])

class Ball:
   def __init__(self):
      self.pos = Vector2(cell_number/2 , cell_number/2)
      x = random.choice([-1, 1])
      y = random.choice([-1, 1])
      self.direction = Vector2(x,y).normalize()
      self.ballspeed = 0.5

   def draw_ball(self):
      ball_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
      screen.blit( ball_sprite, ball_rect)
      
   def move_ball(self, racket1_rect, racket2_rect):
      self.pos.x += self.direction.x * self.ballspeed
      self.pos.y += self.direction.y * self.ballspeed/2
      ball_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
      if self.pos.y <= 0 or self.pos.y >= cell_number - 1:
            self.direction.y = -self.direction.y
      if ball_rect.colliderect(racket1_rect) or ball_rect.colliderect(racket2_rect):
            self.direction.x = -self.direction.x
            self.ballspeed += 0.1
   def reset_ball(self):
      self.pos = Vector2(cell_number/2 , cell_number/2)
      x = random.choice([-1, 1])
      y = random.choice([-1, 1])
      self.direction = Vector2(x,y).normalize()
      self.ballspeed = 0.5      

   
class Main:
   def __init__(self):
      self.racket = Rackets()
      self.ball = Ball()
      self.a = 0
      self.b = 0
   def update(self):
      self.draw_elements()
      self.move_elements()
      self.score_control()
   def draw_elements(self):
      self.racket.draw_racket()
      self.ball.draw_ball()
   def move_elements(self):
      self.racket.move_racket1()
      self.racket.move_racket2()
      racket1_rect = pygame.Rect(int(self.racket.pos1.x * cell_size), int(self.racket.pos1.y * cell_size), cell_size, cell_size * 4)
      racket2_rect = pygame.Rect(int(self.racket.pos2.x * cell_size - cell_size), int(self.racket.pos2.y * cell_size), cell_size, cell_size * 4)
      self.ball.move_ball(racket1_rect, racket2_rect)
   def reset(self):
      self.ball.reset_ball()
      self.racket.reset_rackets()
   def score_control(self):
       score_surface1 = game_font.render(str(self.a),True,(255,255,255))
       score_surface2 = game_font.render(str(self.b),True,(255,255,255))
       score1_rect = score_surface1.get_rect(center = (int(15* cell_size),int(5 * cell_size)))
       score2_rect = score_surface2.get_rect(center = (int(25* cell_size),int(5 * cell_size)))
       screen.blit(score_surface1,score1_rect)
       screen.blit(score_surface2,score2_rect)
       if self.ball.pos.x <= 0:
          self.b += 1
          self.reset()
       if self.ball.pos.x >= cell_number - 1:
          self.a += 1
          self.reset()
       if self.a == 10:
          win_statement = game_font.render(str("Player 1 won the game, if you want to continue press SPACE"),True,(255,255,255))
          win_rect = win_statement.get_rect(center = (int(20* cell_size),int(20* cell_size)))
          screen.blit(win_statement,win_rect)
          self.Pause()
       if self.b == 10:
          win_statement2 = game_font.render(str("Player 2 won the game, if you want to continue press SPACE"),True,(255,255,255))
          win_rect2 = win_statement2.get_rect(center = (int(20* cell_size),int(20* cell_size)))
          screen.blit(win_statement2,win_rect2)
          self.Pause()
   def Pause(self):
      self.racket.racketspeed = 0
      self.ball.ballspeed = 0
      keys = pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
        self.reset()
        self.a = 0
        self.b = 0
      
       
        

       
          

pygame.init()

pygame.display.set_caption("PingPong")
cell_size = 20
cell_number = 40
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
Screen_Update = pygame.USEREVENT
clock = pygame.time.Clock()
main = Main()
ball_sprite = pygame.image.load('Graphics/ball.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
menu_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', cell_size * 5)
Play = menu_font.render(str('Play'),True,(255,255,255))
Quit = menu_font.render(str('Quit'),True,(255,255,255))
play_rect = Play.get_rect(center = (int(20* cell_size),int(15 * cell_size)))
quit_rect = Quit.get_rect(center = (int(20* cell_size),int(25 * cell_size)))

while True:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
         
      
       
        
            
            
        
    screen.fill((0,0,0))
    #screen.blit(Play, play_rect)
    #screen.blit(Quit, quit_rect)
    main.update()     
    pygame.display.update()
    clock.tick(60)