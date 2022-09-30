"""I don't know what I'm going to be doing."""
__author__ = '730571332'

from random import randint

UNICODE_ESCAPE = "\U00000000"


def greet(name: str) -> None:
    # Function that greets the player given a name
    global player
    player = name
    print("")
    print("")
    print("")
    print(f"Welcome, {name}")
    print(f"Today, you will be participating in a randomized game. Enjoy.")

def defuse() -> None:
    return

def safecrack() -> None:
    return


def minefield() -> None:
    # This function will effectively be the "home screen" for the minefield game.
    print("")
    print("~~MINEFIELD~~")
    print("")
    print("You are given a top down view of your partner.")
    print("You need to give them directions to escape the minefield using the directions 'forward', 'left', 'right', or 'backward'.")
    print("'forward' will move your partner forward.'backward' will move them backwards. 'left' or 'right' will turn your partner accordingly.")
    print("Type 'begin' when you are ready. Good luck.")
    print("")
    print("")

    # Checking to make sure user is ready to play.
    ready: str = input("")
    while ready.lower() != "begin":
            ready = input("Still not ready? Just let me know whenever you are by typing 'begin': ")
    print("")
    print("")
    
    # Calling on mfez() to do all the heavy lifting.
    mfez()


def starting_position(start: int) -> None:
    # Prints the first position for the minefield game.
    print("_________                                   END ")
    print("         \                                |     |")
    print(f" {arrows[start]}        \                __________     |     |")
    print("______     \              /          \    |     |")
    print("      \     \            /            \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |")
    print("         \                  /      \            |")
    print("          \                /        \___________|")
    print("           \______________/                      ")


def second_position(start: int) -> None:
    # Prints the second position for the minefield game.
    print("_________                                   END ")
    print("         \                                |     |")
    print(f"       {arrows[start]}  \                __________     |     |")
    print("______     \              /          \    |     |")
    print("      \     \            /            \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |")
    print("         \                  /      \            |")
    print("          \                /        \___________|")
    print("           \______________/                      ")


def third_position(start: int) -> None:
    # Prints the third position for the minefield game.
    print("_________                                   END ")
    print("         \                                |     |")
    print("          \                __________     |     |")
    print("______     \              /          \    |     |")
    print("      \     \            /            \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |")
    print("         \                  /      \            |")
    print(f"          \  {arrows[start]}             /        \___________|")
    print("           \______________/                      ")

def fourth_position(start: int) -> None:
    print("_________                                   END ")
    print("         \                                |     |")
    print("          \                __________     |     |")
    print("______     \              /          \    |     |")
    print("      \     \            /            \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |")
    print("         \                  /      \            |")
    print(f"          \             {arrows[start]}  /        \___________|")
    print("           \______________/                      ")

def fifth_position(start: int) -> None:
    print("_________                                   END ")
    print("         \                                |     |")
    print("          \                __________     |     |")
    print("______     \              /          \    |     |")
    print(f"      \     \            /  {arrows[start]}         \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |")
    print("         \                  /      \            |")
    print("          \                /        \___________|")
    print("           \______________/                      ")

def sixth_position(start: int) -> None:
    print("_________                                   END ")
    print("         \                                |     |")
    print("          \                __________     |     |")
    print("______     \              /          \    |     |")
    print(f"      \     \            /         {arrows[start]}  \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |")
    print("         \                  /      \            |")
    print("          \                /        \___________|")
    print("           \______________/                      ")

def seventh_position(start: int) -> None:
    print("_________                                   END ")
    print("         \                                |     |")
    print("          \                __________     |     |")
    print("______     \              /          \    |     |")
    print("      \     \            /            \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |")
    print(f"         \                  /      \  {arrows[start]}         |")
    print("          \                /        \___________|")
    print("           \______________/                      ")

def eighth_position(start: int) -> None:
    # The eighth position of the minefield game.
    print("_________                                   END ")
    print("         \                                |     |")
    print("          \                __________     |     |")
    print("______     \              /          \    |     |")
    print("      \     \            /            \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |")
    print(f"         \                  /      \         {arrows[start]}  |")
    print("          \                /        \___________|")
    print("           \______________/                      ")

def finished_position(saved: str) -> None:
    # The finish screen if you have completed the game!
    print(f"_________                                    {saved}                YOU SAVED YOUR PARTNER!")
    print("         \                                |     |                     CONGRATS!")
    print("          \                __________     |     |")
    print("______     \              /          \    |     |")
    print("      \     \            /            \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |                THANKS FOR PLAYING :)")
    print("         \                  /      \            |                      - robert")
    print("          \                /        \___________|")
    print("           \______________/                      ")

def finished_position_secret(saved: str) -> None:
    # The finish screen if you have completed the game!
    print(f"_________                                    {saved}                YOU SAVED YOUR PARTNER! (WHILE DOING IT ALL BACKWARDS!)")
    print("         \                                |     |                  CONGRATS! YOU ARE A SUPER SMART HUMAN BEING! :)")
    print("          \                __________     |     |")
    print("______     \              /          \    |     |                    <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3")
    print("      \     \            /            \   |     |")
    print("       \     \          /     ____     \__|     |")
    print("        \     \________/     /    \             |                THANKS FOR PLAYING :)")
    print("         \                  /      \            |                      - robert")
    print("          \                /        \___________|")
    print("           \______________/                      ")


def mfez() -> None:
    # Initializing a 'playing' variable to keep track of whether or not player has failed.
    playing: bool = True

    # Initializing choice.
    global choice
    choice = randint(0,8)

    # List of arrows.
    right_arrow = "\U000027A1"
    right_up_arrow = "\U00002197"
    up_arrow = "\U00002B06"
    left_up_arrow = "\U00002196"
    left_arrow = "\U00002B05"
    left_down_arrow = "\U00002199"
    down_arrow = "\U00002B07"
    right_down_arrow = "\U00002198"

    # Used to change arrows in the picture easily
    global arrows
    arrows = [right_arrow, right_up_arrow, up_arrow, left_up_arrow, left_arrow, left_down_arrow, down_arrow, right_down_arrow]

    i = 0
    j = 0

    while i < 8 and playing:

        # Lots of technical stuff
        if i == 0:
            necessary_choice = 0
            position = starting_position
        elif i == 1:
            necessary_choice = 7
            position = second_position
        elif i == 2:
            necessary_choice = 0
            position = third_position
        elif i == 3:
            necessary_choice = 1
            position = fourth_position
        elif i == 4:
            necessary_choice = 0
            position = fifth_position
        elif i == 5:
            necessary_choice = 7
            position = sixth_position
        elif i == 6:
            necessary_choice = 0
            position = seventh_position
        elif i == 7:
            necessary_choice = 2
            position = eighth_position
        
        necessary_secret = necessary_choice + 4
        if necessary_secret > 7:
            necessary_secret -= 8

        # Resets not_forward after every usage
        not_forward = True
        not_backward = True
        while not_forward and not_backward:
            # Clearing the terminal
            print("")
            print("")
            print("")
            print("")
            print("")

            # Printing the map at the first position
            position(choice)

            # Getting a first instruction from the user
            movement: str = input("Command: ")
            
            # Making sure the user enters a valid direction
            while movement.lower() != "forward" and movement.lower() != "right" and movement.lower() != "left" and movement.lower() != "backward":
                movement: str = input("That is not a valid command. Try again: ")
            
            # Changing arrow accordingly
            if movement.lower() == "left":
                choice += 1
                if choice > 7:
                    choice -= 8
            if movement.lower() == "right":
                choice -= 1
                if choice < 0:
                    choice += 8

            # Checking to see if the user still has not entered 'forward'
            not_forward: bool = movement.lower() != "forward"
            not_backward: bool = movement.lower() != "backward"

        # The only way the user is correct is if the correct arrow is selected when 'forward' is entered or the ~secret~ is activated
        # Otherwise, ask the user to restart
        if (movement == 'forward' and choice != necessary_choice) or (movement == 'backward' and choice != necessary_secret):
            print("Your instructions were incorrect. Your partner perished in the minefield. Try again.")
            playing = False
        
        # Counter for secret path
        if movement == 'backward' and playing == True:
            j += 1
        i += 1
    if j == 8:
        print("")
        print("")
        print("")
        print("")
        print("")
        finished_position_secret("\U0001F31F")
    else:
        print("")
        print("")
        print("")
        print("")
        print("")
        finished_position("\U00002B50")


def main() -> None:
    # Initializing global variables inside main.
    global points
    # Greeting the player
    greet(input("What's your name? "))
    minefield()

    return


if __name__ == "__main__":
    main()