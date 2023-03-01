from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax(pos, depth, max_p, game):

    if depth == 0 or pos.winner() != None:
        return pos.evaluate(), pos

    if max_p:
        maxeval = float("-inf")
        best_path = None
        for move in get_all_moves(pos, WHITE, game):
            eval = minimax(move, depth - 1, False, game)[0]
            maxeval = max(maxeval, eval)
            if maxeval == eval:
                best_path = move
        return maxeval, best_path

    else:
        mineval = float("-inf")
        best_path = None
        for move in get_all_moves(pos, RED, game):
            eval = minimax(move, depth - 1, True, game)[0]
            mineval = min(mineval, eval)
            if mineval == eval:
                best_path = move

        return mineval, best_path


def get_all_moves(pos, color, game):

    moves = []
    for piece in pos.all_pieces(color):
        valid_Move = pos.get_valid_moves(piece)
        for move, skip in valid_Move.items():
            # draw_moves(game, pos, piece)
            temp_board = deepcopy(pos)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


def simulate_move(piece, move, board, game, skip):
    board.motion(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


"""def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()"""
