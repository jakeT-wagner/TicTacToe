import pygame
from tic.constants import WIDTH, HEIGHT, SQUARE_SIZE
from tic.board import Board
import time

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacToe')

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col

def main():
    board = Board(WIN)
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)
        
        if board.check_winner() != None:
            print(f"team {board.check_winner()} is the winner!")
            time.sleep(1.5)
            running  = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                board.make_move(row,col)

        board.update()

    pygame.quit()

main()