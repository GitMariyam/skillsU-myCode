import random as diceroll

# Python function to prompt and return users guess
def getUserGuess ():
    userGuess = int(input ("what do you think the dice rolled value is from (1 to 6) ?"))
    # What could go potentionally wrong here?
    if not (1 <= userGuess <= 6):
        print("Wrong value: Please enter a number between 1 and 6.")
    else:
        return userGuess


############################## MAIN application code ######################
# Simulate a dice being rolled, random result bwtween 1 to 6 (inclusive)
###########################################################################
randomDiceRollResult = diceroll.randint(1,6)

#print (f"The answer is: {randomDiceRollResult}")

#yourGuess= -1
while (randomDiceRollResult != yourGuess ):
    
    yourGuess = getUserGuess()

    if (yourGuess == randomDiceRollResult):
        print ("correct .. You win!")
        break
    else:
        print ("nope!, try again")

# How could I give the user a max of 5 tries only for a bigger range of numbers like 1 to 100?
# How would I hint to the user that their guess should be lower or higher?
# How do I allow the user to give up and ask for the answer?