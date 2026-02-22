"""Python module to read from Anki deck and extract set of questions and answers and store them"""
from bs4 import BeautifulSoup as bs


def extract(src: str) -> dict[str, str]:
    """Function reads deck txt file and outputs questions and correct answers"""
    # read text file
    with open(src) as file:
        cards = file.read()

    # create html soup object from raw text to easily search contents
    card_soup = bs(cards, 'html.parser')

    print(card_soup)


def transform(mark_scheme: dict[str, str]) -> dict[str, set[str]]:
    """Function for data cleaning, outputs questions and set of possible answers"""
    ...


def load(qs_and_as: dict[str, set[str]], dest: str) -> None:
    """Function saves question and answers dictionary to destination filepath"""
    ...


if __name__ == '__main__':
    src = 'data/Master Quiz 26 Sept.txt'  # assume source is downloaded as txt file
    extract(src)
