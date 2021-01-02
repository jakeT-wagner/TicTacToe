import pygame

WIDTH, HEIGHT = 450,450
ROWS, COLS = 3,3
SQUARE_SIZE = WIDTH//COLS

OUTLINE = 10
#rgb for easier color access

GRAY = (128,128,128)
BLACK = (0,0,0)

EX = pygame.transform.scale(pygame.image.load('assets/X.png'), (120,120))
OH = pygame.transform.scale(pygame.image.load('assets/O.png'), (120,120))