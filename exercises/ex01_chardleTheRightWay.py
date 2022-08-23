"""This is my docstring! I am going to attempt chardle."""
__author__ = 730571332

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print(str("Searching for " + letter + " in " + word))

if len(word) != 5:
    print("Error: Word must contain 5 characters")

if len(letter) != 1:
    print("Error: Character must be a single character.")

# j = 0
# k = 0
"""personally i would choose j and k for a task like this but i do not want to get docked points for style and documentation!"""
lettersParsed = 0
lettersInWord = 0

for letterInTheGivenWord in word:
    if letterInTheGivenWord == letter:
        print(letter + " found at index " + str(letterInTheGivenWord))
        # k += 1
        lettersInWord += 1
    # j += 1
    lettersParsed += 1

if lettersInWord == 0:
    print("No instances of " + letter + " found in " + word)
elif lettersInWord == 1:
    print(str(lettersInWord) + " instance of " + letter + " found in " + word)
else:
    print(str(lettersInWord) + " instances of " + letter + " found in " + word)