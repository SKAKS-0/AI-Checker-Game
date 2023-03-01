import pygame
from .constant_vals import WHITE, RED, SIZE_SQUARE, GREY, CROWN


class Piece:
    PADDING = 13
    border = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        self.x = 0
        self.y = 0
        self.position()

    def position(self):

        self.x = SIZE_SQUARE * self.col + SIZE_SQUARE // 2
        self.y = SIZE_SQUARE * self.row + SIZE_SQUARE // 2

    def king(self):
        self.king = True

    def draw(self, win):
        rad = SIZE_SQUARE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), rad + self.border)
        pygame.draw.circle(win, self.color, (self.x, self.y), rad)

        if self.king:
            win.blit(
                CROWN,
                (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2),
            )

    def motion(self, row, col):
        self.row = row
        self.col = col
        self.position()

    def __repr__(self):
        return str(self.color)
