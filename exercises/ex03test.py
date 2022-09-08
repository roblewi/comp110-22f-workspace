"""a structured wordle."""
__author__ = "730571332"

def main():
    """main game function"""
    secretWord = "pytho"
    wBox: str = "\U00002B1C"
    gBox: str = "\U0001F7E9"
    yBox: str = "\U0001F7E8"
    key = ""
    i = 0
    
    while i < 6:
        inputGuess: str = input("Enter a 5 character word: ")
        while len(inputGuess) != len(secretWord):
            inputGuess = input("That wasn't 5 chars! Try again: ")
        """testing index 0"""
        if inputGuess[0] == secretWord[0]:
            key += gBox
        elif inputGuess[0] == secretWord[1]:
            key += yBox
        elif inputGuess[0] == secretWord[2]:
            key += yBox
        elif inputGuess[0] == secretWord[3]:
            key += yBox
        elif inputGuess[0] == secretWord[4]:
            key += yBox
        elif inputGuess[0] == secretWord[5]:
            key += yBox
        else:
            key += wBox
        """testing index 1"""
        if inputGuess[1] == secretWord[0]:
            key += yBox
        elif inputGuess[1] == secretWord[1]:
            key += gBox
        elif inputGuess[1] == secretWord[2]:
            key += yBox
        elif inputGuess[1] == secretWord[3]:
            key += yBox
        elif inputGuess[1] == secretWord[4]:
            key += yBox
        elif inputGuess[1] == secretWord[5]:
            key += yBox
        else:
            key += wBox
        """testing index 2"""
        if inputGuess[2] == secretWord[0]:
            key += yBox
        elif inputGuess[2] == secretWord[1]:
            key += yBox
        elif inputGuess[2] == secretWord[2]:
            key += gBox
        elif inputGuess[2] == secretWord[3]:
            key += yBox
        elif inputGuess[2] == secretWord[4]:
            key += yBox
        elif inputGuess[2] == secretWord[5]:
            key += yBox
        else:
            key += wBox
        """testing index 3"""
        if inputGuess[3] == secretWord[0]:
            key += yBox
        elif inputGuess[3] == secretWord[1]:
            key += yBox
        elif inputGuess[3] == secretWord[2]:
            key += yBox
        elif inputGuess[3] == secretWord[3]:
            key += gBox
        elif inputGuess[3] == secretWord[4]:
            key += yBox
        elif inputGuess[3] == secretWord[5]:
            key += yBox
        else:
            key += wBox
        """testing index 4"""
        if inputGuess[4] == secretWord[0]:
            key += yBox
        elif inputGuess[4] == secretWord[1]:
            key += yBox
        elif inputGuess[4] == secretWord[2]:
            key += yBox
        elif inputGuess[4] == secretWord[3]:
            key += yBox
        elif inputGuess[4] == secretWord[4]:
            key += gBox
        elif inputGuess[4] == secretWord[5]:
            key += yBox
        else:
            key += wBox
        """testing index 5"""
        if inputGuess[5] == secretWord[0]:
            key += yBox
        elif inputGuess[5] == secretWord[1]:
            key += yBox
        elif inputGuess[5] == secretWord[2]:
            key += yBox
        elif inputGuess[5] == secretWord[3]:
            key += yBox
        elif inputGuess[5] == secretWord[4]:
            key += yBox
        elif inputGuess[5] == secretWord[5]:
            key += gBox
        else:
            key += wBox
        
        """avoiding infinite loop woohoo"""
        i += 1
    return key

print(main())
