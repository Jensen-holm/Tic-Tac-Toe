"""
Creating a minimax algorithm that can play this version
of tic-tac-toe was actually really hard.
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
            print(score)
            b_copy[spot] = orig  # not sure if we actually have to get rid of it since we are using a copy

            if score > best_score:
                best_score = score
                best_move = spot
    print(best_score)
    return best_move


def minimax(game: Game, b: Board.board, w: str, is_maximizing: bool, players: list[Player], depth=0):
    if someone_won(b, players[1]):  # bot
        return 1
    if someone_won(b, players[0]):  # user
        return -1
    if check_draw(b, game.tot_moves, players):
        return 0

    if is_maximizing:
        best_score: int = -1000
        for spot in b:
            if is_available(b, spot):
                orig = b[spot]
                b[spot] = w
                score: int = minimax(game, b, w, False, players)
                b[spot] = orig

                if score > best_score:
                    best_score = score
        return best_score
    best_score: int = 800
    for spot in b:
        if is_available(b, spot):
            orig = b[spot]
            b[spot] = w
            score: int = minimax(game, b, w, True, players)
            b[spot] = orig

            if score < best_score:
                best_score = score
    return best_score
