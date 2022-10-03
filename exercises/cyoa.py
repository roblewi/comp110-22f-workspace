"""Making a bunch of minigames for ex06!"""
__author__ = '730571332'

from random import randint

# Declaring some global variables.
points: int = 0
player: str = ""
arrows: list[str] = []


def greet() -> None:
    """Function that greets the player given a name."""
    global player
    player = input("What's your name? ")

    # Clearing the terminal.
    print("\n\n\n\n\n\n\n\n\n\n\n\n")

    # Welcoming user.
    print(f"Welcome, {player}!")
    print("You can pick a game to get instructions. To win, you must purchase the winners trophy from the shop.")
    
    # Instructions.
    print("Make sure to run this program in fullscreen to avoid visual bugs.\n")


def minefield() -> None:
    """This function will effectively be the "home screen" for the Minefield game."""
    print("\n~~MINEFIELD~~\n")
    print(f"Welcome to Minefield, {player}. You are given a top down view of your partner.")
    print("You need to give them directions to escape the minefield using the directions 'forward', 'left', 'right', or 'backward'.")
    print("'forward' will move your partner forward.'backward' will move them backwards. 'left' or 'right' will turn your partner accordingly.")
    print("To get the most amount of points, complete your mission by doing it as absurdly as possible.")
    print("Type 'begin' when you are ready. Good luck.\n\n")

    # Checking to make sure user is ready to play.
    ready: str = input("")
    while ready.lower() != "begin":
        ready = input("Still not ready? Just let me know whenever you are by typing 'begin': \n\n")
    
    # Calling on minefield_backend() to do all the heavy lifting.
    minefield_backend()


def starting_position(start: int) -> None:
    """Prints the first position for the minefield game."""
    print("_________                                   END ")
    print("         \\                                |     |")
    print(f" {arrows[start]}        \\                __________     |     |")
    print("______     \\              /          \\    |     |")
    print("      \\     \\            /            \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |")
    print("         \\                  /      \\            |")
    print("          \\                /        \\___________|")
    print("           \\______________/                      ")


def second_position(start: int) -> None:
    """Prints the second position for the minefield game."""
    print("_________                                   END ")
    print("         \\                                |     |")
    print(f"       {arrows[start]}  \\                __________     |     |")
    print("______     \\              /          \\    |     |")
    print("      \\     \\            /            \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |")
    print("         \\                  /      \\            |")
    print("          \\                /        \\___________|")
    print("           \\______________/                      ")


def third_position(start: int) -> None:
    """Prints the third position for the minefield game."""
    print("_________                                   END ")
    print("         \\                                |     |")
    print("          \\                __________     |     |")
    print("______     \\              /          \\    |     |")
    print("      \\     \\            /            \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |")
    print("         \\                  /      \\            |")
    print(f"          \\  {arrows[start]}             /        \\___________|")
    print("           \\______________/                      ")


def fourth_position(start: int) -> None:
    """Prints the fourth position for the minefield game."""
    print("_________                                   END ")
    print("         \\                                |     |")
    print("          \\                __________     |     |")
    print("______     \\              /          \\    |     |")
    print("      \\     \\            /            \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |")
    print("         \\                  /      \\            |")
    print(f"          \\             {arrows[start]}  /        \\___________|")
    print("           \\______________/                      ")


def fifth_position(start: int) -> None:
    """Prints the fifth position for the minefield game."""
    print(r"_________                                   END ")
    print("         \\                                |     |")
    print("          \\                __________     |     |")
    print("______     \\              /          \\    |     |")
    print(f"      \\     \\            /  {arrows[start]}         \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |")
    print("         \\                  /      \\            |")
    print("          \\                /        \\___________|")
    print("           \\______________/                      ")


def sixth_position(start: int) -> None:
    """Prints the sixth position for the minefield game."""
    print("_________                                   END ")
    print("         \\                                |     |")
    print("          \\                __________     |     |")
    print("______     \\              /          \\    |     |")
    print(f"      \\     \\            /         {arrows[start]}  \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |")
    print("         \\                  /      \\            |")
    print("          \\                /        \\___________|")
    print("           \\______________/                      ")


def seventh_position(start: int) -> None:
    """Prints the seventh position for the minefield game."""
    print("_________                                   END ")
    print("         \\                                |     |")
    print("          \\                __________     |     |")
    print("______     \\              /          \\    |     |")
    print("      \\     \\            /            \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |")
    print(f"         \\                  /      \\  {arrows[start]}         |")
    print("          \\                /        \\___________|")
    print("           \\______________/                      ")


def eighth_position(start: int) -> None:
    """Prints the eighth position of the minefield game."""
    print("_________                                   END ")
    print("         \\                                |     |")
    print("          \\                __________     |     |")
    print("______     \\              /          \\    |     |")
    print("      \\     \\            /            \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |")
    print(f"         \\                  /      \\         {arrows[start]}  |")
    print("          \\                /        \\___________|")
    print("           \\______________/                      ")


def finished_position(saved: str) -> None:
    """The finish screen if you have completed the game!"""
    print(f"_________                                    {saved}                YOU SAVED YOUR PARTNER!")
    print("         \\                                |     |                     CONGRATS!")
    print("          \\                __________     |     |")
    print("______     \\              /          \\    |     |")
    print("      \\     \\            /            \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |                THANKS FOR PLAYING :)")
    print("         \\                  /      \\            |                      - robert")
    print("          \\                /        \\___________|")
    print("           \\______________/                      ")


def finished_position_secret(saved: str) -> None:
    """The finish screen if you have completed the game backwards!"""
    print(f"_________                                    {saved}                YOU SAVED YOUR PARTNER! (WHILE DOING IT ALL BACKWARDS!)")
    print("         \\                                |     |                           CONGRATS! YOU ARE SUPER COOL! B)")
    print("          \\                __________     |     |")
    print("______     \\              /          \\    |     |                    <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3")
    print("      \\     \\            /            \\   |     |")
    print("       \\     \\          /     ____     \\__|     |")
    print("        \\     \\________/     /    \\             |                THANKS FOR PLAYING :)")
    print("         \\                  /      \\            |                      - robert")
    print("          \\                /        \\___________|")
    print("           \\______________/                      ")


def minefield_backend() -> None:
    """The main program of the Minefield game."""
    global arrows

    # List of arrows.
    RIGHT_ARROW: str = "\U000027A1"
    UP_RIGHT_ARROW: str = "\U00002197"
    UP_ARROW: str = "\U00002B06"
    UP_LEFT_ARROW: str = "\U00002196"
    LEFT_ARROW: str = "\U00002B05"
    DOWN_LEFT_ARROW: str = "\U00002199"
    DOWN_ARROW: str = "\U00002B07"
    DOWN_RIGHT_ARROW: str = "\U00002198"

    # Initializing a 'playing' variable to keep track of whether or not player has failed.
    playing: bool = True

    # Initializing choice.
    choice: int = randint(0, 7)

    # Used to change arrows in the picture easily.
    arrows = [RIGHT_ARROW, UP_RIGHT_ARROW, UP_ARROW, UP_LEFT_ARROW, LEFT_ARROW, DOWN_LEFT_ARROW, DOWN_ARROW, DOWN_RIGHT_ARROW]

    # Declaring the types of a few variables I will be using.
    i: int = 0
    j: int = 0
    necessary_choice: int = 0

    while i < 8 and playing:

        # Changing the correct time to use 'forward' depending on where the partner is.
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

        # Resets not_forward and not_backward after every usage.
        not_forward: bool = True
        not_backward: bool = True

        while not_forward and not_backward:
            # Clearing the terminal.
            print("\n\n\n\n\n")

            # Printing the map at the given position.
            position(choice)

            # Getting a first instruction from the user.
            movement: str = input("Command: ")
            
            # Making sure the user enters a valid direction
            while movement.lower() != "forward" and movement.lower() != "right" and movement.lower() != "left" and movement.lower() != "backward":
                movement = input("That is not a valid command. Try again: ")
            
            # Changing arrow accordingly.
            if movement.lower() == "left":
                choice += 1
                if choice > 7:
                    choice -= 8
            if movement.lower() == "right":
                choice -= 1
                if choice < 0:
                    choice += 8

            # Checking to see if the user still has not entered 'forward'.
            not_forward = movement.lower() != "forward"
            not_backward = movement.lower() != "backward"

        # The only way the user is correct is if the correct arrow is selected when 'forward' is entered or the ~secret~ is activated.
        # Otherwise, ask the user to restart
        if (movement == 'forward' and choice != necessary_choice) or (movement == 'backward' and choice != necessary_secret):
            print("Your instructions were incorrect. Your partner perished in the minefield.")
            playing = False
        
        # Counter for secret path.
        if movement == 'backward' and playing:
            j += 1

        # Avoiding the end of the world.
        i += 1
    
    # User gets a lot of bonus points if they went backwards through the whole game.
    if j == 8:
        SHOOTING_STAR = "\U0001F31F"
        print("\n\n\n\n\n")
        finished_position_secret(SHOOTING_STAR)
        # Bonus points!
        global points
        points += 1200
    
    # User gets a few bonus points for every time they went backwards, if they did not go backwards the whole time.
    elif j > 0 and playing:
        points += (100 * j)
    
    # If user did not go backwards at all during gameplay.
    else:
        if playing:
            STAR = "\U00002B50"
            print("\n\n\n\n\n")
            finished_position(STAR)
            # Bonus points!
            points += 500


def codebreaker() -> None:
    """This function will effectively be the "home screen" for the Codebreaker game."""
    print("\n~~CODEBREAKER~~\n")
    print(f"Welcome to Codebreaker, {player}. There is a lock that requires a hidden code.")
    print("When you guess a character correctly in the correct position, it shows up in purple.")
    print("When you guess a character correctly but in the wrong posiiton, it shows up in orange.")
    print("If the character you guess is not in the secret code, it shows up in white.")
    print("Guess a 6-letter combination of letters A-F and numbers 1-9 like this: 'A1B2C3'.")
    print("To get the most amount of points, complete your mission by doing it as quickly as possible.")
    print("You have 10 attempts. Type 'begin' when you are ready. Good luck.\n\n")

    # Checking to make sure user is ready to play.
    ready: str = input("")
    while ready.lower() != "begin":
        ready = input("Still not ready? Just let me know whenever you are by typing 'begin': \n\n")
    
    # Calling on minefield_backend() to do all the heavy lifting.
    codebreaker_backend()


def codebreaker_backend() -> None:
    """The main code for the Codebreaker game."""
    # The possibilities to choose from.
    possible_code_letters: list[str] = ['a', 'b', 'c', 'd', 'e', 'f']
    possible_code_nums: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # Creating the random code (frn = first random number).
    frn = possible_code_nums[randint(0, 8)]
    frl = possible_code_letters[randint(0, 5)]
    srn = possible_code_nums[randint(0, 8)]
    while srn == frn:
        srn = possible_code_nums[randint(0, 8)]
    srl = possible_code_letters[randint(0, 5)]
    while srl == frl:
        srl = possible_code_letters[randint(0, 5)]
    trn = possible_code_nums[randint(0, 8)]
    while trn == frn or trn == srn:
        trn = possible_code_nums[randint(0, 8)]
    trl = possible_code_letters[randint(0, 5)]
    while trl == frl or trl == srl:
        trl = possible_code_letters[randint(0, 5)]
    
    # Creating a list of secret codes to easier determine how the player did.
    secret_code_list = [frl, frn, srl, srn, trl, trn]
    secret_code = frl + str(frn) + srl + str(srn) + trl + str(trn)

    # Making secret_code != user_guess == True.
    user_guess: str = ""

    # Initializing an attempts variable to track how many tries it takes the user.
    attempts: int = 0

    while secret_code != user_guess and attempts < 11:
        # Obtaining a guess from the user.
        user_guess = input("Make your guess: ")

        # Making sure guess is six letters long so that we don't reach an IndexError.
        while len(user_guess) != 6:
            user_guess = input("Your guess must be six characters long. Try again: ")

        # Making shorthands for boolean expressions to make it easier to access them in the future. (Icnv = first character not valid).
        Icnv = user_guess[0].lower() not in possible_code_letters
        IIcnv = user_guess[1] not in possible_code_nums
        IIIcnv = user_guess[2].lower() not in possible_code_letters
        IVcnv = user_guess[3] not in possible_code_nums
        Vcnv = user_guess[4].lower() not in possible_code_letters
        VIcnv = user_guess[5] not in possible_code_nums

        # Checking that guess follows format.
        while Icnv or IIcnv or IIIcnv or IVcnv or Vcnv or VIcnv:
            user_guess = input("Your guess must follow the format 'A1B2C3'. Try again: ")
            while len(user_guess) != 6:
                user_guess = input("Your guess must be six characters long. Try again: ")

            # Allowing the while loop to reevaluate the validity of characters.
            Icnv = user_guess[0].lower() not in possible_code_letters
            IIcnv = user_guess[1] not in possible_code_nums
            IIIcnv = user_guess[2].lower() not in possible_code_letters
            IVcnv = user_guess[3] not in possible_code_nums
            Vcnv = user_guess[4].lower() not in possible_code_letters
            VIcnv = user_guess[5] not in possible_code_nums

        # Creating a consistent user_guess to display.
        user_guess_to_display: str = ""
        i = 0
        while i < len(user_guess):
            if i % 2 == 0:
                user_guess_to_display += f"{(user_guess[i]).upper()}  "
            else:
                user_guess_to_display += f"{user_guess[i]}  "
            i += 1

        # Emojis for feedback variable.
        PURPLE_BOX: str = "\U0001F7EA"
        ORANGE_BOX: str = "\U0001F7E7"
        WHITE_BOX: str = "\U00002B1C"

        # Keeping track of accuracy of user_guess.
        feedback: str = ""

        # Checking user_guess against secret_code.
        j = 0
        while j < len(user_guess):
            if user_guess[j] == secret_code[j]:
                feedback += f"{PURPLE_BOX} "
            elif user_guess[j] in secret_code_list:
                feedback += f"{ORANGE_BOX} "
            else:
                feedback += f"{WHITE_BOX} "
            j += 1
        print(f"{feedback}\n{user_guess_to_display}")

        # Avoiding infinite attempts.
        attempts += 1
    
    # If the user guesses correctly.
    if secret_code == user_guess:
        print("You guessed the code correctly! Congratulations. Enjoy your points.")

    # If the user guesses incorrectly.
    else:
        print("You failed to guess the code correctly.")
    
    # Formula that I came up with to determine points
    attempt_points = 1000 - (100 * (attempts - 1))

    # Not necessary with my current iteration but if attempts were increased this is helpful to not give the user less than the base guaranteed points from completing the game.
    if attempt_points < 0:
        attempt_points = 0
    global points
    points += (500 + attempt_points)


def name_change(name: str) -> None:
    """Changes the player variable if the user purchases a 'name change' from the shop."""
    global player
    player = name
    print(f"Name changed to '{player}'")


def shop() -> None:
    """Provides the shop experience if the user selects 'shop' from the main screen."""
    global points

    # Welcoming user to shop.
    print(f"Welcome to the shop, {player}!\nYou may purchase whatever your heart desires.\nItems for sale:\n\n")

    # Item: Name change
    print("NAME CHANGE\n1000 points\n\n")
    name_change_cost: int = 1000

    # Item: Winners trophy
    print("WINNERS TROPHY\n10000 points\n\n")
    winners_trophy_cost: int = 10000
    
    # Checks if the user would like to purchase anything.
    buying: str = input("Would you like to buy anything? (Y/N) ")
    while buying.lower() != 'y' and buying.lower() != 'n':
        buying = input(f"Sorry, {player}; I don't understand. Would you like to buy something? (Y/N) ")
    
    # If user indicates they would like to shop.
    if buying.lower() == 'y':
        choice: str = input("What would you like to buy? (C to cancel) ")

        # Allows the user to undo their decision to shop for something.
        if choice.lower() == 'c':
            print("Okay. Transcation cancelled.")
        
        # Allows the user to purchase a name change for 1000 points.
        elif choice.lower() == "name change":
            # Making sure the user has points to do so.
            if points >= 1000:
                points -= name_change_cost
                name_change(input(f"What would you like your new name to be, {player}? "))
            else:
                print("You do not have the required points for this.")
        # Allows the user to purchase a winners trophy for 10000 points.
        elif choice.lower() == "winners trophy":
            if points >= 10000:
                points -= winners_trophy_cost
                print("You have obtained the winners trophy! Congratulations! You beat my game!")
                print("                               \U0001F3C6                               ")
                quit()
            else:
                print("You do not have the required points for this.")
    else: 
        print(f"Okay! Hope to see you again soon, {player}!")


def double_or_nothing(wager: int) -> int:
    """Allows the user to play double or nothing with their points."""
    # Initializing while loop
    playing = True
    while playing:
        # Can only play if you have money to wager.
        playing = wager > 0

        # Setting up the situation and engaging the user.
        print("\nHeads, you win. Tails, you lose.")
        coin = input("Choose 'heads' or 'tails': ")
        coin_possibilities = ['heads', 'tails']
        while coin.lower() not in coin_possibilities:
            coin = input(f"Sorry, {player}. That is not a valid choice. Choose 'heads' or 'tails': ")

        # To determine whether the coin lands on 'heads' or 'tails'.
        chance = randint(0, 1)

        # Giving the user feedback on their choice
        print(f"\nIt landed on {coin_possibilities[chance]}!")
        if coin_possibilities[chance] != coin:
            print(f"Sorry {player}! You lost all your points. :(\n")
            wager -= wager
        elif coin_possibilities[chance] == coin:
            print(f"Wow {player}! You doubled your points! :)\n")
            wager += wager
        
        # Giving the option for the user to double down if they win.
        if wager != 0:
            play_again: str = input("Would you like to double down? (Y/N) ")
            while play_again != 'y' and play_again != 'n':
                play_again = input("I don't understand. Would you like to double down? (Y/N) ")
            if play_again.lower() == 'n':
                playing = False
        if wager == 0:
            playing = False
    return wager


def main() -> None:
    """The 'main screen' of the game."""
    # Initializing global variables inside main.
    global points
    points = 0

    # Greeting the player.
    greet()

    user_playing = True
    while user_playing:
        # Asking the user what they want to do.
        user_asks: str = input(f"\nWhat would you like to do, {player}? 'minefield', 'codebreaker', 'show points', 'shop', or 'quit'?\nOr, if you'd like, you can play 'double or nothing' with your points. ")
        user_asks_options = ["minefield", "codebreaker", "show points", "shop", "quit", "double or nothing"]
        while user_asks not in user_asks_options:
            user_asks = input("Sorry, I don't understand. Would you like to go to 'minefield', 'codebreaker', 'show points', 'shop', 'double or nothing', or 'quit'? ")

        if user_asks.lower() == "minefield":
            minefield()
            print("")

        if user_asks.lower() == "codebreaker":
            codebreaker()
            print("")

        if user_asks.lower() == "show points":
            print(f"Your points: {points}")
            print("")

        if user_asks.lower() == "shop":
            shop()

        if user_asks.lower() == "double or nothing":
            if points == 0:
                print("\nYou cannot do a double or nothing with no points! Nice try.\n")
            else:
                points = double_or_nothing(points)
        
        if user_asks.lower() == "quit":
            impressive = ""
            if points >= 5000:
                impressive = "an impressive "
            if points == 0:
                print("You lost! And, on top of that, you got no points! Bummer!")
                quit()
            print(f"You lost! However, you did rack up {impressive}{points} points! Thanks for playing.")
            quit()


if __name__ == "__main__":
    main()
