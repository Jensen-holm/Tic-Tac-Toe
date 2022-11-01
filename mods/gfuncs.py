def get_index() -> int:
    while True:
        # get the index
        inp = input("\nEnter board index (1-9): ").strip()
        if inp.isnumeric():
            return int(inp)
        print(f"\nInvalid input: '{inp}' is not a valid board index. Please try again.")


def available_words(game) -> list[str]:
    if not game.tot_moves:
        return game.get_words()
    return [word for word in game.get_words() if word[1] in game.player_turn().get_letters()]


def get_word(g) -> str:
    a_words: list[str] = available_words(game=g)
    for word in a_words:
        print(word)
    while True:
        choice = input("\nChoose a word: ").strip()
        if choice in a_words:
            return choice
        print("\nInvalid word choice. Try again.")


# print the words available

# # place the word on the board
def place_word(index, g, w: str) -> None:
    try:  # pop will remove it from the game words dict and place it on the board
        g.get_board()[index] = g.get_words().pop(w, None).center(7, " ")
    except KeyError as e:  # meaning not in this dict, which would not be good b/c get_word function checks for this problem
        raise e


# function to determine if the game is over or not
# checks one player at a time after their turn
def is_available(b, key: int):
    if b[key].strip().isnumeric():  # meaning empty space
        return True
    return False


def check_draw(b, tot_moves, player_that_played_last) -> bool:
    won = someone_won(b, player_that_played_last)
    if tot_moves >= 6 and not won:
        return True
    return False


def did_win(b, p_letters, i1, i2, i3):
    if any([is_available(b, i1), is_available(b, i2), is_available(b, i3)]):
        return False
    if b[i1].strip()[1] in p_letters and b[i2].strip()[1] in p_letters and b[i3].strip()[1] in p_letters:
        return True
    return False


def someone_won(b, p) -> bool:
    p_letters: list[str] = p.get_letters()
    win_scenarios: set[bool] = {
        # check top row, check middle row, check bottom row, check left col
        did_win(b, p_letters, 1, 2, 3), did_win(b, p_letters, 4, 5, 6), did_win(b, p_letters, 7, 8, 9),
        did_win(b, p_letters, 1, 4, 7), did_win(b, p_letters, 2, 5, 8),
        did_win(b, p_letters, 3, 6, 9), did_win(b, p_letters, 1, 5, 9), did_win(b, p_letters, 3, 5, 7)
    }
    if any(win_scenarios):
        return True
    return False
