

"""
Creating a minimax algorithm that can play this version
of tic-tac-toe
"""

import random
from mods.obs import Board, User, Player
from mods.gfuncs import someone_won, is_available, check_draw


def get_best_move(b: Board, words: dict[str, str], player_that_played_last: Player, tot_moves: int) -> (int, int):
    best_score: int = -10
    best_move: int = 0
    b_copy: dict[int, str] = b.board.copy()

    for spot in b_copy.keys():
        if not is_available(b = b_copy, key = spot):
            # want to play every possible available move
            b_copy[spot]: str = random.choice(words) # for now, it is random
            score: int = minimax(b_copy, False, player_that_played_last, tot_moves, words)

            if score > best_score:
                best_score: int = score
                best_move: int = spot

    return best_move, best_score


# would need to specify a depth argument if it were more complex than tic-tac-toe
def minimax(b: Board.board, is_maximizing: bool, player_that_played_last: Player, tot_moves: int, words: dict[str, str]):
    # check if the move the cpu tried ended the game or not
    p, won = someone_won(b, player_that_played_last)
    if won and isinstance(p, User):
        return -10
    if won:
        return 10
    if check_draw(b, tot_moves, player_that_played_last):
        return 0
    # if the move tried didn't result in ending the game
        # if the bot is not maximizing
    if not is_maximizing:
        best_score: int = 10
        word: str = ""
        for spot in b:
            if not is_available(b=b, key=spot):
                word: str = random.choice(words)
                b[spot]: str = word
                score: int = minimax(b, True, player_that_played_last, tot_moves, words)

                if score > best_score:
                    best_score: int = score

    # if IT IS maximizing
    best_score: int = -10
    for spot in b:
        if not is_available(b=b, key=spot):
            # want to play every possible available move
            word: str = random.choice(words)
            b[spot]: str = word # for now, it is random
            score: int = minimax(b, False, player_that_played_last, tot_moves, words)

            if score > best_score:
                best_score: int = score

    return best_score, word
