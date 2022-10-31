"""
Creating a minimax algorithm that can play this version
of tic-tac-toe
"""

import random
from mods.obs import Board, User, Player, CPU, Game
from mods.gfuncs import someone_won, is_available, check_draw

"""
Right now the problem I believe is we are passing the list of whole words into the minimax
functions, and not considering that the bot can only use certain words.
also the bot is happy right now if I win or it wins, need to make it so that it wants to win
"""


def get_best_move(b: Board, words: list[str], player_that_played_last: Player, tot_moves: int) -> (int, int):
    best_score: int = -10
    best_move: int = 0
    b_copy: dict[int, str] = b.board.copy()

    for spot in b_copy.keys():
        if is_available(b=b_copy, key=spot):
            # want to play every possible available move
            b_copy[spot]: str = random.choice(words).center(7, " ")  # for now, it is random
            score: int = minimax(board=b_copy, is_maximizing=False, last_turn=player_that_played_last,
                                 tot_moves=tot_moves, words=words)

            if score > best_score:
                best_score: int = score
                best_move: int = spot
    return best_move, best_score


def minimax(board: Board, is_maximizing: bool, tot_moves: int, last_turn: Player, words: list[str]):
    p, won = someone_won(b=board, player_that_just_played=last_turn)
    if won and isinstance(p, CPU):
        return 1
    if won and isinstance(p, User):
        return -1
    if check_draw(b=board, tot_moves=tot_moves, player_that_played_last=last_turn):
        return 0

    def find_bot_available_words(game: Game, bot: Player):
        w: str = ""
        while w not in bot.get_letters():
            word = random.choice(game.get_words())
            if word in bot.get_letters():
                w += word
        return w

    if is_maximizing:
        best_score: int = -800
        for key in board:
            if is_available(board, key):
                board[key]: str = random.choice(words)
                score: int = minimax(board=board, is_maximizing=is_maximizing, tot_moves=tot_moves, last_turn=last_turn,
                                     words=words)
                # maybe reset the board key to empty? but we are doing this on a copy in the first place so it's probably fine
                if score > best_score:
                    best_score: int = score
        return best_score
    # if not is_maximizing ...
    best_score: int = 800
    for key in board:
        if is_available(board, key):
            board[key]: str = random.choice(words)
            score: int = minimax(board=board, is_maximizing=is_maximizing, tot_moves=tot_moves, last_turn=last_turn,
                                 words=words)
            if score < best_score:
                best_score: int = score
    return best_score
