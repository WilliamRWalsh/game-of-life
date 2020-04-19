import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (20, 255, 140)

class Cell(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, x, y, is_alive, width=10, height=10):
        # Call the parent class (Sprite) constructor
        super().__init__()

        if is_alive:
            color = GREEN
        else:
            color = BLACK
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = x * 10
        self.rect.y = y * 10
