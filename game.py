# 1-Import library
import pygame
from pygame.locals import *

# 2 – Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width,
height))

# 3 – Load images
player = pygame.image.load("Users\jayesh\Desktop\dude.png")
    while 1:

    screen.fill(0)

    screen.blit(player, (100,100))

    pygame.display.flip()

# 8 – Loop through the events
for event in pygame.event.get():
# Check if the event is the X
    button
if event.type==pygame.QUIT:
# If it is quit the game
    pygame.quit()
exit(0)
