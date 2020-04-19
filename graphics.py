import pygame, random
from cell import Cell
from board import Board

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Graphics:
    def __init__(self, board: Board):
        pygame.init()
        size = (board.width*10, board.width*10)
        self.screen = pygame.display.set_mode(size)
        self.clock=pygame.time.Clock()
        self.cell_sprites = self._sprites_from_board(board.board)

    def update(self, board: Board):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return False

        self.cell_sprites = self._sprites_from_board(board.board)  
        self.cell_sprites.update()
        self.screen.fill(BLACK)
        self.cell_sprites.draw(self.screen)
        
        # Refresh
        pygame.display.flip()
        self.clock.tick(30)

        return True

    # Very slow way to do this b/c I'm creating a new obj every cycle
    def _sprites_from_board(self, board: Board):
        cell_sprites = pygame.sprite.Group()
        for x, row in enumerate(board):
            for y, is_alive in enumerate(row):
                cell_sprites.add(Cell(x, y, is_alive))
        return cell_sprites