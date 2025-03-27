# -*- coding: utf-8 -*-
import random
import time

"""
Created on Wed Nov 13 16:14:57 2024

Name: CJ Mejia
Starting Date: Nov 13, 2024
Due Date: Nov 24, 2024

Problem Definition: Create a number guessing game in which the user tries to guess a random number within a range based
on the difficulty selected by the user. Everytime the user guesses, the program will tell the user if 
if the number is higher/lower than their guess

There are 3 difficulties:

Easy:
    Range 0-100
    
Medium:
    Range 0-1000

Hard:
    Range 0-10000

After winning (guessing correctly), the user will have the option to replay the game or quit the program.  The user will have unlimited 
chances for guessing until they win. The amount of guesses of the user will be printed after a game into the console.
Once the user quits the program a file will print all of the users scores for each game played during a session in the following format:

'''    

Game: #1
Guesses: <List<#>>
Target: <#>

# of Wrong Guesses: <#>

================

Game: #<#>
Guesses: <List<#>>
Target: <#>

# of Wrong Guesses: <#>

================

'''

If no games were played, output a message that indicates this

Output Guesses in list format without the square brackets. Ex: x, y, z


USER CAN INPUT OUTSIDE OF VALID RANGE WHEN GUESSING BUT WILL "WASTE" A GUESS

Error check inputs to insure every input is an integer

Make sure the program is somewhat visually appealing and user friendly
"""


# method that returns max range based on difficulty: d
def range_max(d):
    """
    Takes the difficulty level 'd' and returns a predetermined max for a range of randomized numbers
    """

    # return 100 if easy
    if d == 1:
        return 100

    # return 1 000 if medium
    elif d == 2:
        return 1000

    # return 10 000 if hard
    elif d == 3:
        return 10000

    # raise exception if value not found
    raise ValueError("difficulty must range from 1-3 1:Easy, 2:Medium, 3:Hard")


# method that runs the game and returns a list of guesses by the player
def guessing_game(d):

    # Print decorations for formatting
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==================================================================="
    )

    # Assign random number to target
    target = random.randint(0, range_max(d))

    # Create list of guesses
    guesses = []

    # Initialize guess
    guess = -1

    # Loop while user has not guessed the number
    while guess != target:

        # Initialize valid guess to being false
        valid_guess = False

        # Loop input while guess is not valid
        while not valid_guess:

            # Input guess
            try:
                guess = int(input("\nTry to Guess the Number! (#): "))
                valid_guess = True

            # Catch an invalid input
            except:
                print("Guess must be an integer")

        # Added guesses to list of guesses
        guesses.append(guess)

        # Check if guess is less than target
        if guess < target:

            # print hint
            print("Target is HIGHER than Guess!")

        # Check if guess is greater than target
        elif guess > target:

            # print hint
            print("Target is LOWER than Guess!")

        # Check if guess == target
        else:

            # print hint
            print(
                "Target was: ",
                target,
                "\n\n~~~~~ YOU WIN!!! ~~~~~\n\nNumber of Guesses: ",
                len(guesses),
            )

    # Return with list of guesses once user wins
    return guesses


# Main menu of game
def main_menu():

    # Variables
    difficulty = -1

    # Dictionary with game # and guesses
    # Format: {<Game#>:<ListOfGuesses>}
    # Ex. games = {1: [1, 2, 3, 4, 8]}
    games = {}

    # Loop while the user doesnt want to quit
    while difficulty != 0:

        # Print options
        print(
            "===================================================================\n\nGuess the Number - Higher or Lower Edition\n\n1. Easy - Range: 0 - 100\n\n2. Medium - Range: 0 - 1 000\n\n3. Hard - Range: 0 - 10 000\n\n0. Quit\n"
        )

        # Inititialize valid_difficulty as False to run while loop
        valid_difficulty = False

        # Loop input if user input is invalid
        while not valid_difficulty:

            # Try to get difficulty from user
            try:
                # prompt difficulty input
                difficulty = int(input("What would you like to do? (#): "))

                # Check if difficulty is 0,1,2,3
                if difficulty not in range(0, 4):

                    # Print clarification message
                    print("Input must be one of the following: 0, 1, 2, 3\n")

                    # Set valid_difficulty to false to reloop
                    valid_difficulty = False

                # Check if difficulty is valid
                else:

                    # Set valid_difficulty True
                    valid_difficulty = True

            # Catch invalid datatype input for difficulty
            except:

                # Print clarification message
                print("Input must be one of the following: 0, 1, 2, 3\n")

                # Set valid_difficulty to false to reloop
                valid_difficulty = False

        # check if user wants to quit game
        if difficulty == 0:
            break

        # Play guessing game and add results of the game to games dictionary
        games[len(games) + 1] = guessing_game(difficulty)

        # Print an end game screen to give time for user to look at game results
        input("\n\n\n===== Press Enter to Continue =====")
        print("\n\n\n\n\n\n\n")

    # Output all the games and output extra prints for details
    output_games(games)
    return None


# Outputs After the Game - Print extra messages before terminating program
def output_games(games):

    # Print extra details
    print("Quitting Game.", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)

    # Notify user their game data was uploaded into a file
    print("\n\nPrinted Games into 'games.txt'")

    # output/print scores to file
    with open("games.txt", "w") as file:

        # insure games length is greater than 0
        if len(games) > 0:

            # loop through every game played during session
            for i in range(1, len(games) + 1):

                # Print to file Note: Target = ListOfGuesses[-1], Target always = Last guess
                file.writelines(
                    f"Game: #{i}\nGuesses: {str(games[i])[1:-1]}\nTarget: {games[i][-1]} \n\n# of Wrong Guesses: {len(games[i])-1}\n\n================\n\n"
                )
        else:
            file.writelines(
                "=============== No Games Available ==============="
            )
    return None


# Run the main menu of the game
main_menu()
