import pygame 
import random 


 
from city_scroller_finished import Scroller


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]




pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("CityScroller")


done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(screen, SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(screen, SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(screen, SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)


class runner_sprite(pygame.sprite.Sprite):
    def __init__(self, imaje):
        super().__init__()
        #self.color = color
        #self.size = size 
        self.imaje = imaje
        self.image = pygame.image.load(self.imaje)
        #self.image.fill(self.color)
        self.rect = self.image.get_rect()


    def update(self):
        if self.rect.x < 0:
            random_y = random.randint(0, SCREEN_HEIGHT)
            self.rect.center = (SCREEN_WIDTH, random_y)
        else:
            self.rect.x -= 3



player = runner_sprite("kirbyonstar.png")

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

good_sprites_list = pygame.sprite.Group()
bad_sprites_list = pygame.sprite.Group()

for i in range(60):
    good_sprites = runner_sprite("star.png")
    good_sprites.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
    good_sprites_list.add(good_sprites)
    all_sprites_list.add(good_sprites)

for i in range(40):
    bad_sprites = runner_sprite("redstar.png")
    bad_sprites.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
    bad_sprites_list.add(bad_sprites)
    all_sprites_list.add(bad_sprites)




SCORE = 0
LIVES = 10 

font = pygame.font.SysFont('Calibri', 25, True, False)
 



# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here

    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()

    mousepos = pygame.mouse.get_pos() 
    player.rect.center = mousepos
    
    all_sprites_list.draw(screen)

    for sprites in good_sprites_list:
        sprites.update()

    for sprites in bad_sprites_list:
        sprites.update()

    good_hit_list = pygame.sprite.spritecollide(player, good_sprites_list, True)
    bad_hit_list = pygame.sprite.spritecollide(player, bad_sprites_list, True)


    for block in good_hit_list:
        SCORE += 1
        print(SCORE)
        good_sprites_list.add(good_sprites)
        all_sprites_list.add(good_sprites)

    for block1 in bad_hit_list:
        LIVES -= 1
        print(LIVES)
        bad_sprites_list.add(bad_sprites)
        all_sprites_list.add(bad_sprites)

  

    text = font.render("SCORE: " + str(SCORE), True, WHITE)
    screen.blit(text, [20, 20])

    text1 = font.render("LIVES: " + str(LIVES), True, WHITE)
    screen.blit(text1, [20, 50])

        


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
