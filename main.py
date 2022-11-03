"""
Title: CIS 162 Tic-Tac-Toe Project
Purpose: Practice Python Programming
Author: Jensen Holm
Date: 11/02/22
"""

from modules.funcs import someone_won
from modules.game import Game
import os


def clear_output() -> None:
    if os.name == "nt":  # windows
        os.system("cls")
        print("\n")
        return
    os.system("clear")  # linux or mac
    print("\n")
    return


def center_multiline_output(string: str) -> None:
    cols, _ = os.get_terminal_size()
    for thing in string.split("\n"):
        print(thing.center(cols))


def game_loop() -> Game:
    game: Game = Game()
    clear_output()
    while not game:
        center_multiline_output(str(game))
        game.player_turn()
        game.increment_moves()
        clear_output()

    if someone_won(game.get_board(), game.current_turn()):
        center_multiline_output(f"{game.current_turn().get_name()} Wins!\n")
        game.current_turn().increment_wins()
        game.other_player().increment_losses()
        return game

    center_multiline_output("Its a draw, embarrassing.\n")
    game.current_turn().increment_draws()
    game.other_player().increment_draws()
    return game


def play() -> None:
    games: list[Game] = []
    while True:
        games.append(game_loop())
        keep_playing: str = input(
            "Enter y to keep playing (anything else to stop): ").strip().lower()
        if keep_playing == "y":
            continue
        break

    wins, losses, draws = sum([g.get_user().get_wins() for g in games]), \
        sum([g.get_user().get_losses() for g in games]), \
        sum([g.get_user().get_draws() for g in games])

    center_multiline_output(
        f"\nThanks for playing!!\n\n"
        f" -- Your Stats --\n"
        f"Wins: {wins}\n"
        f"Losses: {losses}\n"
        f"Draws: {draws}\n"
    )


if __name__ == "__main__":
    play()
