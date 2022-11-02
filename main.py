"""
Title: CIS 162 Tic-Tac-Toe Project
Purpose: Practice Python Programming
Author: Jensen Holm
Date: 10/13/22
"""

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


def game_loop() -> str:
    game: Game = Game()
    print(game.words)
    while not game:
        print(game)
        print(game.current_turn())
        game.player_turn()
        game.increment_moves()
        clear_output()
    return center_output("")


def play() -> None:
    while True:
        print(game_loop())
        keep_playing: str = input("Enter y to keep playing (anything else to stop): ").strip().lower()
        if keep_playing == "y":
            continue
        break


if __name__ == "__main__":
    play()
