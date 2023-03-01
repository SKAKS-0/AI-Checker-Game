import pygame

# Dimensions of the checkers of board
WIDTH, HEIGHT = 800, 800
ROWS, COLUMNS = 8, 8
SIZE_SQUARE = WIDTH // COLUMNS

# Color of board
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CROWN = pygame.transform.scale(pygame.image.load("checkers/crown.png"), (44, 25))
