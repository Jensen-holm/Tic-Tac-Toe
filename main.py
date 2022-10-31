"""
Author: Jensen Holm
Title: Word Tic-Tac-Toe in the terminal
Purpose: CIS162 Project 2
Date: 10/13/22
"""
import random
import os
from mods.obs import Game, User
from mods.gfuncs import get_word, get_index, place_word, someone_won, check_draw
from mods.bot import get_best_move


# just to keep the output tidy
def clear_screen() -> None:
    if os.name == "nt":  # windows
        os.system("cls")
        print("\n\n")
        return
    os.system("clear")
    print("\n\n")  # linux and mac
    return


def main() -> None:
    game: Game = Game()
    while not game:
        print(game.board)

        if isinstance(game.player_turn(), User):
            # have the user choose a word after printing the available words
            w: str = get_word(g=game, p=game.player_turn(), op=game.other_player(), tot_moves=game.tot_moves)
            i: int = get_index()

            # have the player 'claim' words with that second letter
            game.player_turn().claim_letter(w[1])

            # place the word on the board and remove it from the words list
            place_word(index=i, g=game, w=w)



        else:
            print("CPU")

        game.increment_moves()


if __name__ == "__main__":
    main()
