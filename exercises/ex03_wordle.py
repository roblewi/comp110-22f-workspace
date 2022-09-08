"""a structured wordle."""
__author__ = "730571332"


def contains_char(word: str, letter: str) -> bool:
    """this function will check to see if a letter is in a word"""
    assert len(letter) == 1
    i = len(word)
    while i > 0:
        if word[i-1] == letter:
            return True
        i -= 1
    return False

def emojified(guess: str, secret: str) -> str:
    """this function will return a string of emojis giving the user info on their guess"""
    wBox: str = "\U00002B1C"
    gBox: str = "\U0001F7E9"
    yBox: str = "\U0001F7E8"
    key = ""
    assert len(guess) == len(secret)
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            key += gBox
        elif (contains_char(secret, guess[i])):
            key += yBox
        else:
            key += wBox
        i += 1
    return key