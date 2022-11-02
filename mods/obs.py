from dataclasses import dataclass, field
from mods.words import generate_words
from mods.gfuncs import check_draw, someone_won
from mods.gfuncs import place_word, get_index, get_word, is_available
import random


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
    name: str
    wins: int = 0
    draws: int = 0
    losses: int = 0
    streak: int = 0
    letters: list[str] = field(default_factory=lambda: [])

    def claim_letter(self, letter: str) -> None:
        self.letters.append(letter)

    def get_letters(self) -> list[str]:
        return self.letters

    def get_words(self, game_obj) -> list[str]:
        return [word for word in game_obj.get_words() if word[1] in self.get_letters()]


@dataclass
class CPU(Player):
    def __init__(self):
        super().__init__(name="CPU")

    def play_turn(self, game) -> None:
        if game.get_tot_moves() == 1:
            available_words: list[str] = [w for w in game.get_words() if w not in game.other_player().get_words(game)]
            w: str = random.choice(available_words)
            self.claim_letter(w[1])
            i: int = random.choice(
                [key for key in list(game.get_board().keys()) if is_available(game.get_board(), key)])
            place_word(index=i, g=game, w=w)
            return
        available_words: list[str] = self.get_words(game)
        w: str = random.choice(available_words)
        i: int = random.choice(
            [key for key in list(game.get_board().keys()) if not is_available(game.get_board(), key)])
        place_word(index=i, g=game, w=w)


@dataclass
class User(Player):
    def __init__(self):
        super().__init__(name="User")

    def play_turn(self, game) -> None:
        w: str = get_word(g=game)
        if not game.get_tot_moves() or w[1] not in self.get_letters():
            self.claim_letter(w[1])
        i: int = get_index()
        place_word(index=i, g=game, w=w)


@dataclass
class Game:
    players: list[Player] = field(default_factory=lambda: [User(), CPU()])
    tot_moves: int = 0
    board: Board = Board()
    words: list[str] = field(default_factory=lambda: generate_words())

    def get_words(self):
        return self.words

    def get_board(self):
        return self.board.board

    def get_players(self):
        return self.players

    def get_tot_moves(self):
        return self.tot_moves

    def current_player(self):
        return self.get_players()[self.get_tot_moves() % 2]

    def other_player(self):
        return self.get_players()[self.get_tot_moves() - 1]

    # this is how we determine if the game is over or not
    def __bool__(self) -> bool:
        return True if someone_won(self.get_board(), self.current_player()) or \
                       check_draw(self.get_board(), self.get_tot_moves(), self.get_players()) else False

    def increment_moves(self, n=1):
        self.tot_moves += n
