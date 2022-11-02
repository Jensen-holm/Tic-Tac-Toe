"""
Title: CIS 162 Tic-Tac-Toe Project
Purpose: Practice Python Programming
Author: Jensen Holm
Date: 10/13/22
"""

from modules.funcs import someone_won
from modules.game import Game
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
        game.other_player().increment_losses()
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
    wins = sum([g.get_user().get_wins() for g in games])
    losses = sum([g.get_user().get_losses() for g in games])
    draws = sum([g.get_user().get_draws() for g in games])
    print(f"\nThanks for playing!!\n -- Your Stats --\nWins: {wins}\nLosses: {losses}\nDraws: {draws}")


if __name__ == "__main__":
    play()
