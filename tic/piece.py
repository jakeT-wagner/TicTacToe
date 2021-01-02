import pygame
from .constants import EX, OH, SQUARE_SIZE

class Piece:
    def __init__(self, row, col, team):
        self.row = row
        self.col = col
        self.team = team
        
        if self.team == 0:
            self.image = OH
        else:
            self.image = EX

        self.x, self.y = 0,0
        self.get_x_y()

    def get_x_y(self):
        self.x = self.col*SQUARE_SIZE + SQUARE_SIZE//2
        self.y = self.row*SQUARE_SIZE + SQUARE_SIZE//2
    
    def draw(self, win):
        win.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2) )
