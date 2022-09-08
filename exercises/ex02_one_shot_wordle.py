"""attempting one shot wordle woohoo!"""
__author__ = "730571332"

secretWord = "python"
userWord: str = input(f"What is your {str(len(secretWord))}-letter guess? ")
while len(userWord) != len(secretWord):
    userWord = input(f"That was not {str(len(secretWord))} letters! Try again: ")

wBox: str = "\U00002B1C"
gBox: str = "\U0001F7E9"
yBox: str = "\U0001F7E8"
key = ""
index = 0

while index < len(secretWord):
    if secretWord[index] == userWord[index]:
        key += gBox
    elif userWord[index] in secretWord:
        key += yBox
    else:
        key += wBox
    index += 1
    
print(key)
if wBox not in key and yBox not in key:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")