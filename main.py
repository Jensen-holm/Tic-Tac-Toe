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
from mods.gfuncs import check_draw, someone_won


# just to keep the output tidy
def clear_screen() -> None:
    if os.name == "nt":  # windows
        os.system("cls")
        print("\n")
        return
    os.system("clear")
    print("\n")  # linux and mac
    return


def main() -> None:
    game: Game = Game()
    while not game:
        print(game.board)

        if isinstance(game.player_turn(), User):
            w: str = get_word(g=game)

            if not game.tot_moves:
                game.player_turn().claim_letter(w[1])

            i: int = get_index()
            place_word(index=i, g=game, w=w)

        else:  # if it's the bots turn
            if game.tot_moves == 1:
                available_words: list[str] = [w for w in game.get_words() if
                                              w not in game.other_player().get_words(game)]
                w: str = random.choice(available_words)
                game.player_turn().claim_letter(w[1])
            else:
                available_words: list[str] = game.player_turn().get_words(game)
                w: str = random.choice(available_words)

            # minimax to choose the index
            best_move = cpu_move(g=game, words=available_words, players=game.get_players())
            place_word(index=best_move, g=game, w=w)

        # increment total moves made
        game.increment_moves()
        # clear_screen()

    if check_draw(b=game.get_board(), tot_moves=game.tot_moves, players=game.get_players()):
        print(f"Its a draw. Lame.")
    if someone_won(game.get_board(), game.get_players()[0]):
        print("user wins")
    if someone_won(game.get_board(), game.get_players()[1]):
        print("cpu wins")


if __name__ == "__main__":
    main()
