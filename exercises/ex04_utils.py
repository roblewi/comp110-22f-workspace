"""This code will do something with lists to my understanding."""
__author__: str = "730571332"


def all(allInts: list[int], givenInt: int) -> bool:
    """Will determine if every component of the list matches the givenInt."""
    i: int = 0
    if len(allInts) == 0:
        return False
    while i < len(allInts):
        if allInts[i] == givenInt:
            i += 1
        else:
            return False
    return True


def max(maxInts: list[int]) -> int:
    """Returns the largest number in a list."""
    biggestNumber = [float('-inf')]
    i: int = 0
    while i < len(maxInts):
        if maxInts[i] > biggestNumber[0]:
            biggestNumber.pop()
            biggestNumber.append(maxInts[i])
        i += 1
    return int(biggestNumber[0])


def is_equal(firstList: list[int], secondList: list[int]) -> bool:
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