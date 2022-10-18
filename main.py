"""
Author: Jensen Holm
Title: Word Tic-Tac-Toe
Purpose: CIS162 Project 2
Date: 10/13/22
"""

from mods.obs import Game, User
from mods.gfuncs import get_word, get_index, place_word, someone_won
from mods.bot import get_best_move

# right now this works, but is infinite and game doesn't end
def main() -> None:
    game: Game = Game()
    total_moves: int = 0
    game_over: bool = False
    while not game_over:
        for player in game.players:
            print("\n" + str(game.board))

            if isinstance(player, User):
                word: str = get_word(g = game)
                index: int = get_index()
                place_word(index = index, w = word, g = game)
            else: # else if it is the CPU ...
                best_move, best_score = get_best_move(game.board, game.get_words(), player, total_moves)
                place_word(index = best_move, g = game, w = word)

            total_moves += 1
            game_over: bool = True if someone_won(b = game.get_board(), player_that_just_played = player)[1] else False

    # print stats like wins and stuff
    print(game)


if __name__ == "__main__":
    main()
