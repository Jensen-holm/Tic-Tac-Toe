from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    wins: int = 0
    losses: int = 0
    draws: int = 0
    streak: int = 0
    letters: list[str] = field(default_factory=lambda: [])

    def claim_letter(self, letter: str) -> None:
        self.letters.append(letter)

    def get_letters(self) -> list[str]:
        return self.letters

    def get_words(self, game_obj) -> list[str]:
        return [word for word in game_obj.get_words() if word[1] in self.get_letters()]

    def place_word(self, index, g, w: str) -> None:
        g.get_board()[index] = g.get_words().pop(w, None).center(7, " ")


@dataclass
class User(Player):
    def __init__(self):
        super().__init__(name="User")

    def get_word(self, g) -> str:
        a_words: list[str] = self.get_words(game_obj=g)
        for word in a_words:
            print(word)
        while True:
            choice = input("\nChoose a word: ").strip()
            if choice in a_words:
                return choice
            print("\nInvalid word choice. Try again.")

    def get_index(self) -> int:
        while True:
            # get the index
            inp = input("\nEnter board index (1-9): ").strip()
            if inp.isnumeric():
                return int(inp)
            print(f"\nInvalid input: '{inp}' is not a valid board index. Please try again.")

    def play_turn(self, game) -> None:
        w: str = self.get_word(game)
        i: int = self.get_index()
        self.place_word(i, game, w)


@dataclass
class CPU(Player):
    def __init__(self):
        super().__init__(name="CPU")

    def play_turn(self):
        return
