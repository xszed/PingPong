from pygame import *

window = display.set_mode((700, 500))
display.set_caption("PingPong")

font.init()
font = font.Font(None,70)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, height, width):
        super().__init__() #making method a supper method
        self.image = transform.scale(image.load(player_image), (height, width)) #sprite image
        self.speed = player_speed #speed

        """Coordinates of the player """
        self.rect = self.image.get_rect() #getting coords
        self.rect.x = player_x #x
        self.rect.y = player_y #y
    
    def reset(self): 
        """showing sprite on the point with setted coordinates"""
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
    
    def update_2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed
    

player_1 = Player("player.png", -50, 150, 3, 200, 250)
player_2 = Player("player.png", 570, 150, 3, 200, 250)

background = transform.scale(image.load("background.jpg"), (700, 500))

game = True
finish = False
clock = time.Clock()
FPS = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


            
    window.blit(background, (0, 0)) 
    player_1.update_1()
    player_2.update_2()
    
    player_1.reset()
    player_2.reset()

    clock.tick(FPS)
    display.update()    
    