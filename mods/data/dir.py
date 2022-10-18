
import os

# point of this is to make it so that it doesn't matter what
# cpu you run this program on, it will find the file path of the
# words text file
path_to_word_file: str = os.path.dirname(__file__) + "/Words.txt"

if __name__ == "__main__":
    # different across computers
    print(path_to_word_file)
