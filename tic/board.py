import pygame
from .constants import ROWS, COLS, GRAY,BLACK, SQUARE_SIZE, OUTLINE
from .piece import Piece

class Board:
    def __init__(self, win):
        self.grid = []
        self.win = win
        self.turn = 1 #0 will be O and 1 will be X
        self.last_row = -1
        self.last_col = -1
        self.initiate_board()
        self._draw()
    
    def initiate_board(self):
        for row in range(ROWS):
            self.grid.append([])
            for _ in range(COLS):
                self.grid[row].append(0)
    
    def draw_cross(self):
        self.win.fill(BLACK)
        for i in range(1,ROWS):
            pygame.draw.line(self.win, GRAY, (0,i*SQUARE_SIZE), (ROWS*SQUARE_SIZE, i * SQUARE_SIZE), OUTLINE )
            pygame.draw.line(self.win, GRAY, (i * SQUARE_SIZE, 0), (i*SQUARE_SIZE, COLS*SQUARE_SIZE), OUTLINE )
    
    def _draw(self):
        self.draw_cross()
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col] != 0 :
                    self.grid[row][col].draw(self.win)
    
    def make_move(self, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = Piece(row,col,self.turn)
            self.last_row = row
            self.last_col = col
            self.switch_turn()

    def switch_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def update(self):
        self._draw()
        pygame.display.update()

    def check_winner(self): #very disgusting I know, just watned to be done as I knew this game was quite simple 
        if self.last_row != -1:
            player = self.grid[self.last_row][self.last_col].team
            count = 0
            #check the column of the most recently played piece for a winner
            for i in range(3):
                if self.grid[i][self.last_col] != 0:
                    if self.grid[i][self.last_col].team == player:
                        count += 1
                    else:
                        count = 0
                    if count >= 3:
                        return player
                else:
                    count = 0
            count = 0
            #check the row
            for i in range(3):
                if self.grid[self.last_row][i] != 0:
                    if self.grid[self.last_row][i].team == player:
                        count += 1
                    else:
                        count = 0
                    if count >= 3:
                        return player
                else:
                    count = 0
            count = 0
            #positive diagonal(x = y 1,1 2,2 etc)
            if self.last_col == self.last_row:
                for i in range(3):
                    if self.grid[i][i] != 0:
                        if self.grid[i][i].team == player:
                            count += 1
                        else:
                            count = 0
                        if count >= 3:
                            return player
                    else:
                        count = 0
            count = 0

            #negative diagonal 
            if self.last_col + self.last_row == 2:
                for i in range(3):
                    if self.grid[2-i][i] != 0:
                        if self.grid[2-i][i].team == player:
                            count += 1
                        else:
                            count = 0
                        if count >= 3:
                            return player
                    else:
                        count = 0
                    

       
        '''
        for i in range(ROWS):
            if self.grid[i][0] != 0 and self.grid[i][1] != 0 and self.grid[i][2] != 0:
                if (self.grid[i][0].team == self.grid[i][1].team == self.grid[i][2].team):
                    if self.grid[i][0].team == 0:
                        return "Os"
                    else:
                        return "Xs"
            if self.grid[0][i] != 0 and self.grid[1][i] != 0 and self.grid[2][i] != 0:
                if (self.grid[0][i].team == self.grid[1][i].team == self.grid[2][i].team):
                    if self.grid[0][i].team == 0:
                        return "Os"
                    else:
                        return "Xs"
            if i == 1:
                if (self.grid[i-1][i-1] != 0 and self.grid[i][i] != 0 and self.grid[i+1][i+1] != 0):
                    if self.grid[i-1][i-1].team == self.grid[i][i].team == self.grid[i+1][i+1].team:
                        if self.grid[i][i].team == 0:
                            return "Os"
                        else:
                            return "Xs"     
                elif self.grid[i+1][i-1] != 0 and self.grid[i][i] != 0 and self.grid[i-1][i+1] != 0:
                    if self.grid[i+1][i-1].team == self.grid[i][i].team == self.grid[i-1][i+1].team:
                        if self.grid[i][i].team == 0:
                            return "Os"
                        else:
                            return "Xs"                     
        return None
        '''

    
        
                