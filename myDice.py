import random as diceroll

# Python function to prompt and return user's guess with input validation
def getUserGuess(lower_bound, upper_bound):
    while True:
        try:
            # Prompt the user for a guess
            userGuess = int(input(f"Guess the dice roll value ({lower_bound} to {upper_bound}): "))
            
            # Check if the guess is within the valid range
            if userGuess < lower_bound or userGuess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
            else:
                return userGuess  # Exit the loop if the input is valid

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# ############################## MAIN application code ######################
# Simulate a dice being rolled, random result between 1 to 100 (inclusive)
###########################################################################
lower_bound = 1
upper_bound = 100
randomDiceRollResult = diceroll.randint(lower_bound, upper_bound)

# Set the maximum number of allowed guesses
max_trials = 5

yourGuess = -1
attempts = 0

print(f"Welcome to the Dice Guessing Game!")
print(f"Guess the number between {lower_bound} and {upper_bound}.")

# Game loop with maximum attempts
while attempts < max_trials:
    attempts += 1
    yourGuess = getUserGuess(lower_bound, upper_bound)
    
    if yourGuess == randomDiceRollResult:
        print("Congratulations its a correct guess ! You win!")
        break  # Exit the loop if the guess is correct
    else:
        # Provide a hint based on the guess
        if yourGuess < randomDiceRollResult:
            print("Wrong guess! Try a higher number.")
        elif yourGuess > randomDiceRollResult:
            print("Wrong guess! Try a lower number.")
        
        
    
# If the user reaches the max attempts without guessing correctly
if yourGuess != randomDiceRollResult:
    print(f"Sorry, you've used all {max_trials} attempts. The correct number was {randomDiceRollResult}.")
