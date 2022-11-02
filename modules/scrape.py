from requests import get, ConnectionError, HTTPError
from bs4 import BeautifulSoup
import random


# only ran this code a few times before eventually saving the data into a txt file
def get_request(url: str) -> BeautifulSoup:
    h: dict[str] = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }
    try:
        r = get(url, headers=h)
        soup: BeautifulSoup = BeautifulSoup(r.text, features="html.parser")
        return soup
    except ConnectionError or HTTPError as e:
        raise e("Error retrieving list of words. Wait a minute, check internet and try again.")


# found a cool website that has a massive list of words
def save_words() -> None:
    all_w: list[str] = [word.text for word in get_request("https://www.mit.edu/~ecprice/wordlist.10000")][0].split("\n")
    random.shuffle(all_w)
    ws: list[str] = [word for word in all_w if 3 <= len(
        word) <= 7]  # this is pretty inefficient, narrows it down to words at least 3 chars long or larger than 7

    f = open("data/Words.txt", "w")
    for w in ws:
        f.write(w + "\n")
    f.close()


if __name__ == "__main__":
    save_words()
