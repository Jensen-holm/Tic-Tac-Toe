"""
Author: Jensen Holm
Title: Word Tic-Tac-Toe
Purpose: CIS162 Project 2
Date: 10/13/22
"""
import random
import os
from mods.obs import Game
from mods.gfuncs import get_word, get_index, place_word, someone_won, check_draw
from mods.bot import get_best_move


#
# # just to keep the output tidy
# def clear_screen() -> None:
#     if os.name == "nt":  # windows
#         os.system("cls")
#         return
#     os.system("clear")  # linux and mac
#     return
#


def main() -> None:
    game: Game = Game()
    while not game:
        print(game.board)

        game.increment_moves(n=1)


if __name__ == "__main__":
    main()
