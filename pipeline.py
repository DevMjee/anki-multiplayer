"""Python module to read from Anki deck and extract set of questions and answers and store them"""


def extract(src: str) -> dict[str, str]:
    """Function reads deck txt file and outputs questions and correct answers"""
    ...


def transform(mark_scheme: dict[str, str]) -> dict[str, set[str]]:
    """Function for data cleaning, outputs questions and set of possible answers"""
    ...


def load(qs_and_as: dict[str, set[str]], dest: str) -> None:
    """Function saves question and answer dictionary to destination filepath"""
    ...


if __name__ == '__main__':
    ...
