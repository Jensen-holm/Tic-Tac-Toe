"""
Author: Jensen Holm
Title: Word Tic-Tac-Toe in the terminal
Purpose: CIS162 Project 2
Date: 10/13/22
"""
import random
import os
from mods.obs import Game, User
from mods.gfuncs import get_word, get_index, place_word
from mods.bot import cpu_move


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
            w: str = get_word(g=game)
            i: int = get_index()
            # have the player 'claim' words with that second letter
            game.player_turn().claim_letter(w[1])
            # place the word on the board and remove it from the words list
            place_word(index=i, g=game, w=w)

        else: # if it's the bots turn
            # random available word
            if game.tot_moves == 1:
                available_words: list[str] = [word for word in game.get_words() if
                                              word[1] not in game.other_player().get_letters()]
                w: str = random.choice(available_words)
                game.player_turn().claim_letter(w[1])
            else:
                available_words: list[str] = [word for word in game.get_words() if
                                              word[1] in game.player_turn().get_letters()]
                w: str = random.choice(available_words)

                # minimax to choose the index          # not sure if this is the correct input for 'player that played last
                best_move: str = cpu_move(g=game, w=w, players=game.get_players())
                print(best_move)

        # increment total moves made
        game.increment_moves()

    print(f"\n{game.other_player().name} WINS!!")


if __name__ == "__main__":
    main()
