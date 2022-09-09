"""A structured wordle."""
__author__ = "730571332"


def contains_char(word: str, letter: str) -> bool:
    """This function will check to see if a letter is in a word."""
    assert len(letter) == 1
    i = len(word)
    while i > 0:
        if word[i - 1] == letter:
            return True
        i -= 1
    return False


def emojified(guess: str, secret: str) -> str:
    """This function will return a string of emojis giving the user info on their guess."""
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


def input_guess(expL: int) -> str:
    """Getting an input for the expected length from the user."""
    userGuess: str = input(f"Enter a {expL} character word: ")
    while len(userGuess) != expL:
        userGuess = input(f"That wasn't {expL} chars! Try again: ")
    return userGuess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secretWord = "coders"
    i = 1
    """Using i < 7 because user only gets 6 votes, not dependent on word length."""
    while i < 7:
        print(f"~ turn {i}/6 ~")
        guessedWord = input_guess(len(secretWord))
        print(emojified(guessedWord, secretWord))
        if guessedWord == secretWord:
            print(f"You won in {i}/6 turns!")
            return None
        i += 1
    print("x/6 - sorry, try again tomorrow!")

"""Mystery code lol."""
if __name__ == "__main__":
    main()