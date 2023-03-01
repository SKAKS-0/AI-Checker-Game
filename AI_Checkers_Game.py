import pygame
from checkers.constant_vals import WIDTH, HEIGHT, SIZE_SQUARE, WHITE, RED
from algorithm.minimax import minimax
from checkers.game import Game
from checkers.board import Board


FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_mouse(pos):
    x, y = pos
    row = y // SIZE_SQUARE
    col = x // SIZE_SQUARE
    return row, col


def main():

    run = True
    clk = pygame.time.Clock()
    game = Game(window)

    while run:

        clk.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():  # check if any events occurred...
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
