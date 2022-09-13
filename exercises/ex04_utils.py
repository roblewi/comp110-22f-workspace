"""This code will do something with lists to my understanding."""
__author__ = "730571332"


def all(allInts: list, givenInt: int) -> bool:
    """Will determine if every component of the list matches the givenInt."""
    i = 0
    while i < len(allInts):
        if allInts[i] == givenInt:
            i += 1
        else:
            return False
    return True


def max(maxInts: list) -> int:
    """Returns the largest number in a list."""
    i = 0
    while i < (len(maxInts) - 1):
        if maxInts[i + 1] > maxInts[i]:
            biggestNumber = maxInts[i + 1]
        i += 1
    return biggestNumber


def is_equal(firstList: list, secondList: list) -> bool:
    """Checks whether or not the lists share deep equality."""
    i = 0
    if len(firstList) != len(secondList):
        return False
    while i < len(firstList):
        if firstList[i] == secondList[i]:
            i += 1
        else:
            return False
    return True