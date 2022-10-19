
from dataclasses import dataclass
from mods.words import generate_words


class Board:
    board: dict[int] = {
        1: "1".center(7), 2: "2".center(7), 3: "3".center(7),
        4: "4".center(7), 5: "5".center(7), 6: "6".center(7),
        7: "7".center(7), 8: "8".center(7), 9: "9".center(7)
    }

    def get_board(self) -> dict[int]:
        return self.board

    def __repr__(self) -> str:
        r: str = ""
        for i in range(len(self.board)):
            i += 1  # index of dict starts at one
            r += (self.board[i] + " " + "|")
            if not i % 3:
                r += "\n"
        return r


# Player objects
@dataclass
class Player:
    name: str = ""
    wins: int = 0
    draws: int = 0
    losses: int = 0
    streak: int = 0
    letters = []

    def claim_letter(self, letter: str) -> None:
        self.letters.append(letter)
    
    def get_letters(self) -> list[str]:
        return self.letters


class CPU(Player):
    def __init__(self):
        super().__init__(name="CPU")

class User(Player):
    def __init__(self):
        super().__init__(name="User")


class Game:
    board: Board = Board()
    players: list[Player] = [User(), CPU()]
    words: dict[str] = generate_words()

    def get_players(self) -> list[Player]:
        return self.players

    def get_board(self) -> Board.board:
        return self.board.board

    def get_words(self) -> dict[str, str]:
        return self.words
