

"""
Creating a minimax algorithm that can play this version
of tic-tac-toe
"""

import random
from mods.obs import Board, User, Player, CPU
from mods.gfuncs import someone_won, is_available, check_draw


def get_best_move(b: Board, words: dict[str, str], player_that_played_last: Player, tot_moves: int) -> (int, int):
    best_score: int = -10
    best_move: int = 0
    b_copy: dict[int, str] = b.board.copy()

    for spot in b_copy.keys():
        if is_available(b = b_copy, key = spot):
            # want to play every possible available move
            b_copy[spot]: str = random.choice(list(words.keys())).center(7, " ") # for now, it is random
            score: int = minimax(board=b_copy, is_maximizing=False, last_turn=player_that_played_last, tot_moves=tot_moves, words=words)

            if score > best_score:
                best_score: int = score
                best_move: int = spot
    return best_move, best_score


def minimax(board: Board, is_maximizing: bool, tot_moves: int, last_turn: Player, words: dict[str, str]):
    p, won = someone_won(b=board, player_that_just_played=last_turn)
    if won and isinstance(p, CPU):
        return 1
    if won and isinstance(p, User):
        return -1
    if check_draw(b = board, tot_moves = tot_moves, player_that_played_last = last_turn):
        return 0
    if is_maximizing:
        best_score: int = -800
        for key in board:
            if is_available(board, key):
                board[key]: str = random.choice(list(words.keys()))
                score: int =  minimax(board=board, is_maximizing=is_maximizing, tot_moves=tot_moves, last_turn=last_turn, words=words)
                # maybe reset the board key to empty? but we are doing this on a copy in the first place so it's probably fine
                if score > best_score:
                    best_score: int = score
        return best_score
    # if not is_maximizing ...
    best_score: int = 800
    for key in board:
        if is_available(board, key):
            board[key]: str = random.choice(list(words.keys()))
            score: int = minimax(board=board, is_maximizing=is_maximizing, tot_moves=tot_moves, last_turn=last_turn, words=words)
            if score < best_score:
                best_score: int = score
    return best_score
