"""i will now attempt chardle."""
__author__ = "730571332"

userWord: str = input("Enter a 5-character word: ")
if len(userWord) != 5:
    print("Error: Word must contain 5 characters")
    exit()
userLetter: str = input("Enter a single character: ")
if len(userLetter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + userLetter + " in " + userWord)

letterCount = 0

"""and now, hell"""
if userWord[0] == userLetter:
    print(userLetter + " found at index 0")
    letterCount += 1

if userWord[1] == userLetter:
    print(userLetter + " found at index 1")
    letterCount += 1

if userWord[2] == userLetter:
    print(userLetter + " found at index 2")
    letterCount += 1

if userWord[3] == userLetter:
    print(userLetter + " found at index 3")
    letterCount += 1

if userWord[4] == userLetter:
    print(userLetter + " found at index 4")
    letterCount += 1
    
if letterCount == 0:
    print("No instances of " + userLetter + " found in " + userWord)
elif letterCount == 1:
    print("1 instance of " + userLetter + " found in " + userWord)
else:
    print(str(letterCount) + " instances of " + userLetter + " found in " + userWord)