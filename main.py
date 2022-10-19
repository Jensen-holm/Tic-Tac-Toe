"""
Author: Jensen Holm
Title: Word Tic-Tac-Toe
Purpose: CIS162 Project 2
Date: 10/13/22
"""
import random
import os
from mods.obs import Game, User
from mods.gfuncs import get_word, get_index, place_word, someone_won
from mods.bot import get_best_move


def clear_screen() -> None:
    if os.name == "nt": #windows
        os.system("cls")
        return 0
    os.system("clear") # linux and mac
    return 0

# right now this works, but is infinite and game doesn't end
def main() -> None:
    game: Game = Game()
    total_moves: int = 0
    winner: str = ""
    game_over: bool = False
    while not game_over:
        for player in game.players:
            print("\n" + str(game.board))

            if isinstance(player, User):
                word: str = get_word(g=game)
                index: int = get_index()
                place_word(index=index, w=word, g=game)
            else:  # else if it is the CPU ...
                best_move, best_score = get_best_move(game.board, game.get_words(), player, total_moves)
                word: str = random.choice(list(game.get_words().keys()))
                place_word(index=best_move, g=game, w=word)

            clear_screen()
            total_moves += 1
            p, won = someone_won(b=game.get_board(), player_that_just_played=player)
            if won:
                print(f"{p.name} Wins!")
                game_over: bool = True

    # print stats like wins and stuff


if __name__ == "__main__":
    main()
