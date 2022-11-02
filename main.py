"""
Author: Jensen Holm
Title: Word Tic-Tac-Toe in the terminal
Purpose: CIS162 Project 2
Date: 10/13/22
"""
import random
import os
from mods.obs import Game, User, Player
from mods.gfuncs import get_word, get_index, place_word
from mods.gfuncs import check_draw, someone_won, is_available


# just to keep the output tidy
def clear_screen() -> None:
    if os.name == "nt":  # windows
        os.system("cls")
        print("\n")
        return
    os.system("clear")
    print("\n")  # linux and mac
    return


def main() -> str:
    game: Game = Game()
    while not game:
        print(game.board)

        game.current_player().play_turn(game)

        # increment total moves made to change player turn
        game.increment_moves()
        clear_screen()

    if check_draw(b=game.get_board(), tot_moves=game.tot_moves, players=game.get_players()):
        return "Its a draw. Lame."
    if someone_won(game.get_board(), game.get_players()[0]):
        return "User Wins!"
    if someone_won(game.get_board(), game.get_players()[1]):
        return "CPU Wins!"


if __name__ == "__main__":
    print(main())
