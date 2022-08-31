"""attempting one shot wordle woohoo"""
__author__ = "730571332"

# defining secret word and asking user for input, then checking to make sure their input is valid
secretWord = "python"
userWord: str = input("What is your " + str(len(secretWord)) + "-letter guess? ")
while len(userWord) != len(secretWord):
    userWord: str = input("That was not " + str(len(secretWord)) + " letters! Try again: ")

# shortened the names of the boxes
wBox: str = "\U00002B1C"
gBox: str = "\U0001F7E9"
yBox: str = "\U0001F7E8"

# making an empty string for the final "box" response and an index being checked, starting at index 0
key = ""
index = 0

# checking each index and matching it against the user's word
while index < len(secretWord):
    if secretWord[index] == userWord[index]:
        key += gBox
    elif userWord[index] in secretWord:
        key += yBox
    else:
        key += wBox
    index += 1

# printing the "boxes" as well as a helpful message!
print(key)
if wBox not in key and yBox not in key:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")