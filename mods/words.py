
import random
import string
from mods.data.dir import path_to_word_file

# special function that I wanted to define this way so that I could remember it
# for future projects because it could be pretty useful
def flatten_list_of_dictionaries(dict_lst: list[dict]) -> dict:
    return {k: v for collection in dict_lst for k, v in collection.items()}

def read_word_file():
    with open(path_to_word_file, "r") as f:
        l: list[str] = f.readlines()
        return [line.replace("\n", "") for line in l]

valid_words: list[str] = [word for word in read_word_file() if 3 <= len(word) <= 7]

# this function was causing some problems, need to redo
def generate_words() -> dict[str, str]:
    random.shuffle(valid_words)
    alphabet: list[str] = list(string.ascii_lowercase)
    word_collections: list = []
    for i in range(3):
        w_dict: dict[str, str] = {}
        rand_letter: str = random.choice(alphabet)
        for w in valid_words:
            if w[1] == rand_letter:
                w_dict[w] = w
                if len(w_dict) == 3:
                    break
        word_collections.append(w_dict)
    # flatten the list of dictionaries into one bigger dictionary
    return flatten_list_of_dictionaries(word_collections)
# does every word that matches, need to fix

# to confirm that I was reading the file
if __name__ == "__main__":
    print(read_word_file())
