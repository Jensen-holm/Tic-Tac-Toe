from dataclasses import dataclass, field
from mods.words import generate_words
from mods.gfuncs import check_draw, someone_won


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


@dataclass
class Player:
    name: str = ""
    wins: int = 0
    draws: int = 0
    losses: int = 0
    streak: int = 0
    letters: list[str] = field(default_factory=lambda: [])

    def claim_letter(self, letter: str) -> None:
        self.letters.append(letter)

    def get_letters(self) -> list[str]:
        return self.letters

    def set_letter(self, letter) -> None:
        self.letters.append(letter)

    # only want to check this after the first turn
    def get_words(self, game_obj) -> list[str]:
        return [word for word in game_obj.get_words() if word[1] in self.get_letters()]


@dataclass
class CPU(Player):
    def __init__(self):
        super().__init__(name="CPU")


@dataclass
class User(Player):
    def __init__(self):
        super().__init__(name="User")


class Game:
    board: Board = Board()
    players: list[Player] = [User(), CPU()]
    words: dict[str] = generate_words()
    tot_moves: int = 0

    def player_turn(self) -> Player:
        return self.players[self.tot_moves % 2]

    def other_player(self):
        return self.players[(self.tot_moves % 2) - 1]

    def __bool__(self) -> bool:
        p, won = someone_won(self.board.board, self.player_turn())
        draw = check_draw(self.board.board, self.tot_moves, self.player_turn())
        return False if draw or not won else True

    def get_players(self) -> list[Player]:
        return self.players

    def get_board(self) -> Board.board:
        return self.board.board

    def get_words(self) -> dict[str, str]:
        return self.words

    def increment_moves(self, n: int = 1):
        self.tot_moves += n
