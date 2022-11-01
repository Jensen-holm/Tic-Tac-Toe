"""
Creating a minimax algorithm that can play this version
of tic-tac-toe
"""

import random
from mods.obs import Board, User, Player, CPU, Game
from mods.gfuncs import someone_won, is_available, check_draw


def cpu_move(g: Game, words: list[str], players: list[Player]) -> str:
    best_score: int = -1000
    best_move = 0
    b_copy: dict[str, str] = g.get_board().copy()

    for spot in b_copy:
        if is_available(b_copy, spot):
            w: str = random.choice(words)
            orig = b_copy[spot]
            b_copy[spot] = w
            score: int = minimax(game=g, b=b_copy, w=w, is_maximizing=False, players=players)
            b_copy[spot] = orig  # not sure if we actually have to get rid of it since we are using a copy

            if score > best_score:
                best_score = score
                best_move = spot
    return best_move


def minimax(game: Game, b: Board.board, w: str, is_maximizing: bool, players: list[Player], depth=0):
    _, user_won = someone_won(b, players[0])
    _, cpu_won = someone_won(b, players[1])

    if cpu_won:
        return 100
    if user_won:
        return -100
    if check_draw(b, game.tot_moves, players[0]):  # worried about passing this same index each time
        return 0

    if is_maximizing:
        best_score: int = -1000
        for spot in b:
            if is_available(b, spot):
                orig = b[spot]
                b[spot] = w
                score: int = minimax(game, b, w, is_maximizing, players)
                b[spot] = orig
                print(spot, score)

                if score > best_score:
                    best_score = score
        return best_score

    best_score: int = 1000
    for spot in b:
        if is_available(b, spot):
            orig = b[spot]
            b[spot] = w
            score: int = minimax(game, b, w, True, players)
            b[spot] = orig

            if score < best_score:
                best_score = score
    return best_score
