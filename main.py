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
            i: int = get_index()
            game.player_turn().claim_letter(w[1])
            place_word(index=i, g=game, w=w)

        else:  # if it's the bots turn
            if game.tot_moves == 1:
                available_words: list[str] = [w for w in game.get_words() if
                                              w not in game.other_player().get_words(game)]
            else:
                available_words: list[str] = game.player_turn().get_words(game)
            w: str = random.choice(available_words)
            game.player_turn().claim_letter(w[1])

            # minimax to choose the index          # not sure if this is the correct input for 'player that played last'
            best_move = cpu_move(g=game, words=available_words, players=game.get_players())
            place_word(index=best_move, g=game, w=w)

        # increment total moves made
        game.increment_moves()
        clear_screen()

    if check_draw(b=game.get_board(), tot_moves=game.tot_moves, player_that_played_last=game.get_players()[0]):
        print(f"Its a draw. Lame.")
    _, cpu_won = someone_won(b=game.get_board(), p=game.get_players()[1])
    _, user_won = someone_won(b=game.get_board(), p=game.get_players()[0])
    if user_won:
        print(f"User Won!!!")
    if cpu_won:
        print("CPU Won!!!")


if __name__ == "__main__":
    main()
