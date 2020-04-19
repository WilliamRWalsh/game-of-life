from board import Board
import pygame
from graphics import Graphics

board = Board()
graphics = Graphics(board)

is_running = True
while is_running:
    # Board Logic
    board.update()
    # Update Graphics
    is_running = graphics.update(board)

pygame.quit()