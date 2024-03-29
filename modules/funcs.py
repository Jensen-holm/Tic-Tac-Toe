def is_available(b, key: int) -> bool:
    if b[key].strip().isnumeric():  # meaning empty space
        return True
    return False


def check_draw(game) -> bool:
    if game.get_tot_moves() >= 7 and not someone_won(game.get_board(), game.current_turn()):
        return True
    if not game.get_user().get_words(game) or not game.get_cpu().get_words(game):
        return True
    return False


def did_win(b, p_letters, i1, i2, i3) -> bool:
    if any([is_available(b, i1), is_available(b, i2), is_available(b, i3)]):
        return False
    if b[i1].strip()[1] in p_letters and b[i2].strip()[1] in p_letters and b[i3].strip()[1] in p_letters:
        return True
    return False


def someone_won(b, p) -> bool:
    p_letters: list[str] = p.get_letters()
    win_scenarios: set[bool] = {
        did_win(b, p_letters, 1, 2, 3), did_win(b, p_letters, 4, 5, 6), did_win(b, p_letters, 7, 8, 9),
        did_win(b, p_letters, 1, 4, 7), did_win(b, p_letters, 2, 5, 8),
        did_win(b, p_letters, 3, 6, 9), did_win(b, p_letters, 1, 5, 9), did_win(b, p_letters, 3, 5, 7)
    }
    if any(win_scenarios):
        return True
    return False
