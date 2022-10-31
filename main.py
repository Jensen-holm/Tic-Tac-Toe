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
    total_moves: int = 0
    game_over: bool = False
    while not game_over:

        for i, player in enumerate(game.players):
            print("\n" + str(game.board))
            other_player = [p for p in game.players if p != player][0]

            if player.name == "User":
                print("users turn")
                word: str = get_word(p=player, g=game, op=other_player, tot_moves=total_moves)

                if not total_moves or total_moves == 1:
                    player.claim_letter(word[1])

                index: int = get_index()
                place_word(index=index, w=word, g=game)

            else:
                print("cpu turn")
                print(player.get_words(game_obj=game))
                # this is an issue, the words that we are letting the cpu select from
                best_move, best_score = get_best_move(b=game.board,
                                                      words=player.get_words(game_obj=game),
                                                      player_that_played_last=player,
                                                      tot_moves=total_moves)
                word: str = random.choice(player.get_words(game_obj=game))
                place_word(index=best_move, g=game, w=word)

            # clear_screen()
            total_moves += 1
            # for some reason it has only been checking the cpu

            # check for draw
            if check_draw(b=game.board.board, tot_moves=total_moves, player_that_played_last=player):
                print(f"It's a draw!!")
                game_over: bool = True

            p, won = someone_won(b=game.get_board(), player_that_just_played=player)


            if won:
                print(f"{p.name} Wins!")
                game_over: bool = True


if __name__ == "__main__":
    main()
