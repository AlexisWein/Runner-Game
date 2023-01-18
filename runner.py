import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# # create surface with a solid color
# test_surface = pygame.Surface((100,200))
# test_surface.fill('pink')

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black')                #second value is anti-aliasing (smoothing out the text)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))         #this is the order they will appear onscreen
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)                          #maxiumum framerate