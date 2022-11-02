"""
Title: CIS 162 Tic-Tac-Toe Project
Purpose: Practice Python Programming
Author: Jensen Holm
Date: 10/13/22
"""

from funcs import someone_won, check_draw
from players import User, CPU
from game import Game
import os


def clear_output() -> None:
    if os.name == "nt":  # windows
        os.system("cls")
        return
    os.system("clear")  # linux or mac
    return


def center_output(string: str) -> str:
    cols, _ = os.get_terminal_size()
    return string.center(cols)


def game_loop() -> (str, Game):
    game: Game = Game()

    while not game:
        print(game)
        game.player_turn()
        game.increment_moves()
        clear_output()

    if someone_won(game.get_board(), game.current_turn()):
        game.current_turn().increment_wins()
        game.current_turn().increment_losses()
        return center_output(""), game

    game.current_turn().increment_draws()
    game.other_player().increment_draws()
    return center_output(""), game


def play() -> None:
    games: list[Game] = []
    while True:
        result, game = game_loop()
        games.append(game)
        keep_playing: str = input("Enter y to keep playing (anything else to stop): ").strip().lower()
        if keep_playing == "y":
            continue
        break
    print(f"Thanks for playing word Tic-Tac-Toe!\n -- Your Stats --\nWins: ")


if __name__ == "__main__":
    play()
