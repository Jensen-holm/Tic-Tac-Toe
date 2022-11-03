from dataclasses import dataclass, field
from modules.words import generate_words
from modules.players import Player, User, CPU
from modules.funcs import check_draw, someone_won


@dataclass
class Game:
    board: dict[int, str] = field(default_factory=lambda: {
        1: "1".center(7), 2: "2".center(7), 3: "3".center(7),
        4: "4".center(7), 5: "5".center(7), 6: "6".center(7),
        7: "7".center(7), 8: "8".center(7), 9: "9".center(7)
    })
    words: list[str] = field(default_factory=lambda: generate_words())
    players: list[Player] = field(default_factory=lambda: [User(), CPU()])
    tot_moves: int = 0

    def __bool__(self) -> bool:
        return True if someone_won(self.get_board(), self.current_turn()) or check_draw(self) else False

    def __repr__(self) -> str:
        r: str = ""
        for i in range(1, len(self.board) + 1):  # b/c the board indexes starts at 1 not 0
            r += (self.board[i] + " " + "|")
            if not i % 3:
                r += "\n"
        return r

    def get_board(self) -> dict[int, str]:
        return self.board

    def get_tot_moves(self) -> int:
        return self.tot_moves

    def current_turn(self) -> Player:
        return self.players[self.tot_moves % 2]

    # not sure if we will need this one
    def other_player(self) -> Player:
        return self.players[(self.tot_moves % 2) - 1]

    def increment_moves(self, n=1) -> None:
        self.tot_moves += n

    def player_turn(self) -> None:
        self.current_turn().play_turn(self)

    def get_words(self) -> list[str]:
        return self.words

    def get_user(self) -> Player:
        return self.players[0]

    def get_cpu(self) -> Player:
        return self.players[1]
