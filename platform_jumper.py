import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

BACKGROUND_COLOR = (15, 23, 42)    
PLAYER_COLOR = (244, 63, 94)       
PLATFORM_COLOR = (16, 185, 129)    

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Platform Jumper")
clock = pygame.time.Clock()

player_width = 50
player_height = 50
player_x = 100
player_y = 400
player_speed = 5

velocity_y = 0
gravity = 0.6
jump_power = -13
is_grounded = False

try:
    player_image = pygame.image.load("Images/player.png").convert_alpha()
    player_image = pygame.transform.scale(player_image, (player_width, player_height))
except pygame.error:
    player_image = pygame.Surface((player_width, player_height))
    player_image.fill(PLAYER_COLOR)

platforms = [
    pygame.Rect(0, 560, 800, 40),      
    pygame.Rect(150, 450, 150, 20),
    pygame.Rect(400, 360, 180, 20),
    pygame.Rect(200, 250, 150, 20),
    pygame.Rect(550, 180, 150, 20)
]

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and is_grounded:
                velocity_y = jump_power
                is_grounded = False

    keys = pygame.key.get_pressed()
    dx = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = player_speed

    velocity_y += gravity
    dy = velocity_y

    player_x += dx
    if player_x < 0:
        player_x = 0
    elif player_x + player_width > SCREEN_WIDTH:
        player_x = SCREEN_WIDTH - player_width

    player_rect = pygame.Rect(player_x, player_y + dy, player_width, player_height)
    
    is_grounded = False
    for platform in platforms:
        if player_rect.colliderect(platform):
            if velocity_y > 0 and player_y + player_height <= platform.top + 10:
                dy = platform.top - (player_y + player_height)
                velocity_y = 0
                is_grounded = True

    player_y += dy

    screen.fill(BACKGROUND_COLOR)
    
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)
        
    screen.blit(player_image, (player_x, player_y))

    pygame.display.flip()

pygame.quit()
sys.exit()
