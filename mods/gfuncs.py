
from mods.obs import Board, Game, Player

def get_index() -> int:
    # get the index
    global inp # setting this as a global variable is not ideal, but had to be done to avoid weird recursion problems
    inp = input("\nEnter board index (1-9): ").strip()
    if not inp.isnumeric():
        print(f"\nInvalid input: '{inp}' is not a valid board index. Please try again.")
        get_index()
    return int(inp)


def get_word(g: Game, p: Player, op: Player, tot_moves: int) -> str:
   while True:
        ws: list[str] = []
        if tot_moves <= 1:
            available_words: list[str]= [word for word in g.get_words() if word[1] not in op.get_letters()]
            for word in available_words:
                ws.append(word)
                print(word)
        else:
            available_words: list[str] = [word for word in g.get_words() if word[1] in p.get_letters()]
            for word in available_words:
                ws.append(word)
                print(word)

        w: str = input("Choose a word: ").strip()
        if w in ws:
            return w
        print("Invalid word try again")

# # place the word on the board
def place_word(index: int, g: Game, w: str) -> None:
    try: # pop will remove it from the game words dict and place it on the board
        g.get_board()[index] = g.get_words().pop(w, None).center(7, " ")
    except KeyError as e: # meaning not in this dict, which would not be good b/c get_word function checks for this problem
        raise e

# function to determine if the game is over or not
# checks one player at a time after their turn
def is_available(b: Board.board, key: int):
    if b[key].strip().isnumeric(): # meaning empty space
        return True
    return False


def did_win(b, i1, i2, i3):
    if any([is_available(b, i1), is_available(b, i2), is_available(b, i3)]):
        return False
    if b[i1].strip()[1] == b[i2].strip()[1] == b[i3].strip()[1]:
        return True
    return False


def check_draw(b: Board.board, tot_moves: int, player_that_played_last) -> bool:
    p, won = someone_won(b, player_that_played_last)
    if tot_moves >= 6 and not won:
        return True
    return False


# function to determine if the game is over or not
# checks one player at a time after their turn
# we want ot be able to tell who won
def someone_won(b: Board.board, player_that_just_played: Player) -> (Player, bool):
    # need to double-check the indexes maybe
    win_scenarios: set[bool] = {
        # check top row, check middle row, check bottom row, check left col
        did_win(b, 1, 2, 3), did_win(b, 4, 5, 6), did_win(b, 7, 8, 9), did_win(b, 1, 4, 7), did_win(b, 2, 5, 8), did_win(b, 3, 6, 9), did_win(b, 1, 5, 9)
    }
    if any(win_scenarios):
        return player_that_just_played, True
    return player_that_just_played, False
